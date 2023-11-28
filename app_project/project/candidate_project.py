import logging
import json
from .models import (
    Projects,
    db,
    ProjectsSchema,
    ProjectEmployeesCompanie,
    CandidateProject
)


def flow_selection_process(value, app):
    logging.warning(f'PROJECT! {value}')
    with app.app_context():
        add_candidate_project(value)
    pass


def add_candidate_project(value):
    logging.warning(f'SAVE CANDIDATE PROJECT!')
    if value.get('where') == 'candidate-chosen-one':
        projectId = value.get('projectId', -1)
        if projectId >= 1 and value.get('basicinfo'):
            new_candidate = CandidateProject(
                project_id=value.get('projectId', -1),
                candidate_id=value.get('candidateId', -1),
                data=json.dumps(value.get("basicinfo"))
            )
            db.session.add(new_candidate)
            db.session.commit()
    pass
