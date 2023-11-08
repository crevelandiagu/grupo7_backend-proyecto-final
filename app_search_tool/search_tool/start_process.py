from .utils_gcp.gcp_pub_sub import GCP
import logging

def chosen_one_candidate(request):

    message_start_process = {
        "where": "candidate-chosen-one",
        "candidateId": request.json['candidateId'],
        "projectId": request.json['projectId'],
        "companyId": request.json['companyId'],
    }
    logging.warning(f'Watch!')
    try:
        logging.warning(f'Watch! send')
        publicar = GCP()
        publicar.publisher_message(message_start_process)
    except Exception as e:
        logging.warning(f'Watch! NO SEND')
        print({"message": f"{e}"})
    return {"message": "Candidate has started the process"}, 200

