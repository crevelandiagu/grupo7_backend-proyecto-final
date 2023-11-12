import requests
import json
from datetime import datetime
from .models import (
    Performance,
    db,
    PerformanceaSchema,
)


def make_evaluation_performance(request):
    metrics = json.dumps(
        {"communication": "80/100",
         "company values": "80/100",
         "leadership": "70/100",
         "overall performance": "60/100"
         }
    )
    feedback = 'good job'
    try:
        new_performance = Performance(
            candidateId=request.json["candidateId"],
            companyId=request.json["companyId"],
            projectId=request.json["projectId"],
            score=request.json["score"],
            employeeId=request.json.get('employeeId', 0),
            feedback=feedback,
            metrics=metrics
        )
        db.session.add(new_performance)
        db.session.commit()
        return {"message": "Performance successfully added",
                "id": new_performance.id,
                "createdAt": datetime.now().isoformat()
                }, 200
    except Exception as e:
        print(e)
        return {"message": f"Missing: {e}"}, 400


def get_performance_candidate(request):
    """
    :type request: object
    """
    projectsSchema = PerformanceaSchema()
    id_candidate = request.view_args.get('id_candidate', -1)
    list_performance = Performance.query.filter(Performance.candidateId == id_candidate).all()
    projectsList = [projectsSchema.dump(performance) for performance in list_performance]
    return projectsList, 200
