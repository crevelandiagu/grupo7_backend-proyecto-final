import os
import json
from google.auth import jwt
from google.cloud import pubsub_v1
from ..candidate_selection import flow_selection_process

class GCP:
    def __init__(self):
        self.PROJECT_ID = os.getenv('PROJECT_ID', 'abc-jobs-grupo7')
        self.KEY_GCP = os.getenv('GCP_JSON', '')
        self.audience = "https://pubsub.googleapis.com/google.pubsub.v1.Subscriber"
        self.publisher_audience = "https://pubsub.googleapis.com/google.pubsub.v1.Publisher"

    def auth_gcp(self, audience, publisher_audience):
        service_account_info = json.loads(self.KEY_GCP, strict=False)
        audience = audience
        credentials = jwt.Credentials.from_service_account_info(
            service_account_info, audience=audience
        )
        publisher_audience = publisher_audience
        credentials_pub = credentials.with_claims(audience=publisher_audience)
        return credentials_pub


    def publisher_message(self, message: dict):
        credentials_pub = self.auth_gcp(self.audience, self.publisher_audience)
        publisher = pubsub_v1.PublisherClient(credentials=credentials_pub)
        topic_path = publisher.topic_path(self.PROJECT_ID, "test1")

        # The message must be a bytestrin and dict
        data = message
        message = json.dumps(data).encode("utf-8")

        # When you publish a message, the client returns a future.
        future1 = publisher.publish(topic_path, message)
        print(future1.result())

    def subscriber_message(self, app):
        credentials_pub = self.auth_gcp(self.publisher_audience, self.audience)
        subscriber = pubsub_v1.SubscriberClient(credentials=credentials_pub)
        subscription_path = subscriber.subscription_path(self.PROJECT_ID, "selection_process")

        def callback(message: pubsub_v1.subscriber.message.Message) -> None:
            print("message:")
            print(message.data)
            value = json.loads(message.data)
            flow_selection_process(value, app)
            print(value)
            message.ack()
        streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
        print(f"Listening for messages on {subscription_path}..\n")
        with subscriber:
            try:
                # When `timeout` is not set, result() will block indefinitely,
                streaming_pull_future.result()
            except TimeoutError:
                streaming_pull_future.cancel()  # Trigger the shutdown.
                streaming_pull_future.result()


if __name__ == "__main__":
    '''Example publisher message'''
    # publicar = GCP()
    # publicar.publisher_message({"A": 1, "C": 9})
    pass
