import logging
import json
import random
import time
from .factory import get_project
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
    pass


def add_selection_process(value):

    logging.warning(f'SAVE DATABASES!')
    time.sleep(3)
    candidateId = value.get('candidateId', -1)
    projectId = value.get('projectId', -1)
    companyId = value.get('companyId', -1)

    data_proyect = get_project(companyId, projectId, candidateId)
    new_candidate_assement = Assement(
        candidate_id=candidateId,
        candidate_name=data_proyect.get('candidateName', 'none'),
        project_id=projectId,
        project_name=data_proyect.get('projectName', 'none'),
        company_id=companyId,
        company_name=data_proyect.get('companyName', 'none'),
        test_id=random.randint(1, 2),
        status="tecnical_test"
    )
    db.session.add(new_candidate_assement)
    db.session.commit()

    new_process = SelectionProcess(
        candidate_id=candidateId,
        candidate_name=data_proyect.get('candidateName', 'none'),
        project_id=projectId,
        project_name=data_proyect.get('projectName', 'none'),
        company_id=companyId,
        company_name=data_proyect.get('companyName', 'none'),
        score=0,
        pogress_status="tecnical_test"
    )
    db.session.add(new_process)
    db.session.commit()

