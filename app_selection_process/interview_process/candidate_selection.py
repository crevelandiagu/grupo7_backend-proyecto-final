import logging
import json
import random
from .models import (
    Assement,
    db,
    SelectionProcess
)


def flow_selection_process(value, app):
    logging.warning(f'PROJECT! {value}')
    with app.app_context():
        add_candidate_project(value)
    pass


def add_candidate_project(value):
    logging.warning(f'SAVE CANDIDATE ASSASMENT!')
    if value.get('where') == 'candidate-chosen-one':
        projectId = value.get('projectId', -1)
        companyProjects = Assement.query.filter(
            Assement.project_id == projectId,
            Assement.company_id == value.get('companyId', -1)
        ).first()
        if projectId >= 1 and not companyProjects:
            add_selection_process(value)
            new_candidate_assement = Assement(
                candidate_id=value.get('candidateId', -1),
                company_id=value.get('companyId', -1),
                project_id=value.get('projectId', -1),
                data=json.dumps(value.get("basicinfo")),
                assement_id=random.randint(1, 2)
            )
            db.session.add(new_candidate_assement)
            db.session.commit()
    pass

def add_selection_process(value):
    new_process = SelectionProcess(
        pogress_status="tecnical_test",
        company_id=value.get('companyId', -1),
        candidate_id=value.get('candidateId', -1),
        proyect=value.get('projectId', -1),
        score=0
    )
    db.session.add(new_process)
    db.session.commit()

