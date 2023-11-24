from .models import Contract, db
CONTRACT = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sapien metus, consequat malesuada dolor vitae, tincidunt pellentesque urna. Suspendisse potenti. Pellentesque sit amet sapien consequat, porttitor odio nec, finibus sapien. Suspendisse sed nisi turpis. Nam ornare malesuada velit, a placerat dui molestie in. Suspendisse eu urna congue leo aliquam euismod. In faucibus odio at sapien ultricies tempor. Nunc fringilla commodo euismod. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec egestas massa ligula, at ultricies sem tincidunt eget.

Duis lobortis molestie orci, nec consectetur sapien placerat cursus. Nulla eu odio ac felis porta consectetur a eu velit. Quisque eget consequat nunc. Duis a nisi sem. Interdum et malesuada fames ac ante ipsum primis in faucibus. In sodales eu nisi id bibendum. Suspendisse elementum mi sit amet sagittis sollicitudin. Nunc quam felis, suscipit a pulvinar sed, sagittis in ipsum. Curabitur ut pellentesque est, vitae aliquam magna. Integer lorem mi, volutpat vel tempor venenatis, tempus at risus.

Proin odio neque, posuere eget ligula posuere, rhoncus lobortis dui. Duis auctor id est vel ornare. Mauris commodo dolor in tortor sodales hendrerit in ac ipsum. Duis urna sapien, eleifend in risus hendrerit, volutpat maximus nisl. Aenean nec purus non risus condimentum cursus at vitae quam. Aliquam eget diam vel nibh tempor mattis eu nec nibh. Sed in metus ut justo ultricies rutrum. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Sed turpis sem, ultricies eget ornare ut, imperdiet vel elit. Suspendisse semper feugiat ullamcorper. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Ut cursus libero sit amet imperdiet dictum.

Morbi porttitor lacinia posuere. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Integer vitae arcu nisl. Maecenas ac metus tellus. Etiam lacinia dictum eros vitae consequat. Donec quis quam sapien. Nam elementum dui purus, ullamcorper dignissim sapien maximus vel. Quisque id urna vitae lectus iaculis convallis quis sed velit. Morbi tempor consequat eros in pellentesque. Suspendisse quis pulvinar tellus, at eleifend erat. In varius hendrerit sem, in scelerisque tortor volutpat et. Quisque vel magna est. Donec egestas tincidunt consectetur. Sed viverra eros lectus, imperdiet molestie est tempor et. Pellentesque id bibendum nibh. Sed venenatis erat id viverra blandit.

Cras consequat, nibh nec tempus feugiat, diam nibh feugiat ligula, lacinia pulvinar libero leo non velit. Nullam eu finibus urna. Sed dignissim ac sem ac posuere. Praesent sit amet odio ac est porttitor ornare ut at augue. Vestibulum aliquam rutrum fermentum. Praesent vitae mauris nibh. Duis eleifend mauris sit amet nisl condimentum, vitae efficitur metus venenatis. In odio turpis, ornare non dignissim ac, condimentum lobortis neque.
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