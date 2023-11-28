from .models import Contract, db
CONTRACT = '''
CONTRATO DE TRABAJO ENTRE (Company ABC) Y (${id}) Entre las partes, por un lado (nombre completo del empleador), domiciliado en la ciudad de (lugar actual de domicilio), representante legal de (nombre de la empresa), con NIT (número de NIT) (en caso que el empleador sea una persona jurídica), quien en adelante y para los efectos del presente contrato se denomina como EL EMPLEADOR, y por el otro, (nombre completo del trabajador), domiciliado en la ciudad de (lugar actual de domicilio), quien en adelante y para los efectos del presente contrato se denomina como EL TRABAJADOR, ambos mayores de edad (las partes deben ser mayores de 18 años; especialmente el trabajador, salvo que se trate de un menor de edad con permiso de trabajo expedido por el Inspector del Trabajo), identificados como aparece al pie de las firmas, hemos acordado suscribir este contrato de trabajo
'''


def get_contract_text(request, user):
    candidateId = request.view_args.get('id_candidate', -1)
    companyId = request.view_args.get('id_company', -1)

    if user == 'candidate':
        progress_status = Contract.query.filter(
            Contract.candidateId == candidateId
        ).first()
        if progress_status:
            return {"contract": CONTRACT}, 200
    elif user == 'company':
        progress_status = Contract.query.filter(
            Contract.companyId == companyId
        ).first()
        if progress_status:
            return {"contract": CONTRACT}, 200


def sign_contract_user(request):

    return {"message": "The contract was signed successfully"}, 200

def create_contract_user(request):
    new_contract = Contract(
        candidateId=request.json.get('candidateId'),
        projectId=request.json.get('projectId'),
        companyId=request.json.get('companyId')
    )
    db.session.add(new_contract)
    db.session.commit()
    return {"message": "Contract made"}, 200