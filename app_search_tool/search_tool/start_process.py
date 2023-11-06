from .utils_gcp.gcp_pub_sub import GCP

def chosen_one_candidate(request):

    message_start_process = {
        "database": "selection_process_db",
        "candidateId": request.json['candidateId'],
        "proyectId": request.json['proyectId'],
        "companyId": request.json['companyId'],
    }
    try:
        publicar = GCP()
        publicar.publisher_message(message_start_process)
        return {"message": "OK"}, 200
    except Exception as e:
        return {"message": f"{e}"}, 400

