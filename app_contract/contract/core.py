from .models import Contract, db


def get_contract_text(request, user):
    candidateId = request.view_args.get('id_candidate', -1)
    companyId = request.view_args.get('id_company', -1)

    if user == 'candidate':
        progress_status = Contract.query.filter(
            Contract.candidateId == candidateId
        ).first()
    elif user == 'company':
        progress_status = Contract.query.filter(Contract.companyId == companyId).order_by(Contract.id.desc()).first()
    if progress_status:
        CONTRACT = made_contract(progress_status)
        return {"contract": CONTRACT}, 200
    return {"message": "We don\'t have contracts yet"}, 200


def sign_contract_user(request):
    return {"message": "The contract was signed successfully"}, 200

def create_contract_user(request):
    new_contract = Contract(
        candidateId=request.json.get('candidateId'),
        projectId=request.json.get('projectId'),
        companyId=request.json.get('companyId'),
        candidate_name=request.json.get('candidate_name'),
        project_name=request.json.get('project_name'),
        company_name=request.json.get('company_name'),
    )
    db.session.add(new_contract)
    db.session.commit()
    return {"message": "Contract made"}, 200


def made_contract(progress_status):
    CONTRACT = ''
    if progress_status:
        CONTRACT = '''
        CONTRATO DE TRABAJO ENTRE (Company ABC) Y ({candidate_name}) Entre las partes, por un lado ({candidate_name}), domiciliado en la ciudad de Bogota, representante legal de {company_name}, con NIT 12345678 Para el proyecto {project}, quien en adelante y para los efectos del presente contrato se denomina como EL EMPLEADOR, y por el otro, (nombre completo del trabajador), domiciliado en la ciudad de (lugar actual de domicilio), quien en adelante y para los efectos del presente contrato se denomina como EL TRABAJADOR, ambos mayores de edad (las partes deben ser mayores de 18 años; especialmente el trabajador, salvo que se trate de un menor de edad con permiso de trabajo expedido por el Inspector del Trabajo), identificados como aparece al pie de las firmas, hemos acordado suscribir este contrato de trabajo
        '''.format(candidate_name=progress_status.candidate_name,
                   company_name=progress_status.company_name,
                   project=progress_status.project_name
                   )

    return CONTRACT


