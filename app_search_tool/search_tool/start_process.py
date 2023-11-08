from .utils_gcp.gcp_pub_sub import GCP

def chosen_one_candidate(request):

    message_start_process = {
        "database": "selection_process_db",
        "candidateId": request.json['candidateId'],
        "projectId": request.json['projectId'],
        "companyId": request.json['companyId'],
    }
    try:
        publicar = GCP()
        publicar.publisher_message(message_start_process)
    except Exception as e:
        print({"message": f"{e}"})
    return {"message": "Candidate has started the process"}, 200

