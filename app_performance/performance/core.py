import requests
import json
from datetime import datetime
from .models import Performance, db


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
            candidate_id=request.json["candidateId"],
            company_id=request.json["companyId"],
            project_id=request.json["projectId"],
            score=request.json["score"],
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