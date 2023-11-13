import logging
from apscheduler.schedulers.background import BackgroundScheduler
from .utils_gcp.gcp_pub_sub import GCP
from .views import projects


__all__ = ['projects']


def subscriber_message(app):
    logging.warning(f'Watch! GCP')
    leer = GCP()
    leer.subscriber_message(app)
