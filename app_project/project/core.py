import json
from .models import (
    Projects,
    db,
    ProjectsSchema,
    ProjectEmployeesCompanie,
    CandidateProject
)
from .utils_gcp.gcp_pub_sub import GCP


projectsSchema = ProjectsSchema()


#@jwt_required
def create_company_project(request):

    data_project = dict(request.json)
    projectName = data_project.get('projectName', "")
    description = data_project.get('description', "")

    if (len(projectName) == 0):
        return {"message": "Missing project name"}, 412

    try:
        companyId = int(data_project.get("companyId", ""))
    except Exception as e:
        return {"message": "Wrong company id value"}, 412

    new_project = Projects(
        projectName=projectName,
        description=description,
        companyId=companyId,
        status="BASE"
    )
    try:
        db.session.add(new_project)
        db.session.commit()
    except Exception as e:
        print(e)
        return {"message": "Internal server error"}, 500
    
    return {"message": f"Project {projectName} successfully created"}, 201


#@jwt_required
def get_company_projects(request):

    try:
        companyId = int(request.args.get('companyId', ""))
    except:
        return {"message": "Company Id missing or sent with wrong format"}, 400    
    
    try:
        companyProjects = Projects.query.filter(Projects.companyId == companyId).all()
    except Exception as e:
        return {"message": "Internal server error"}, 500

    # if (len(companyProjects) == 0):
    #     return {"message": "No projects found"}, 404

    projectsList = [projectsSchema.dump(proj) for proj in companyProjects]

    for projects_list in projectsList:
        project_com = dict(projects_list)
        list_candi = project_com.get('candidate_project_id')
        list_a = []
        for j in list_candi:
            inf_candidate = CandidateProject.query.filter(CandidateProject.project_id == j).first()
            data_candidate = json.loads(inf_candidate.data)
            data_candidate['candidate_id'] = inf_candidate.candidate_id
            list_a.append(data_candidate)
        projects_list.update({'candidate_project_id': list_a})

    return projectsList, 200

def associate_employee_projects(request):

    new_project = ProjectEmployeesCompanie(
        project_id=request.json["projectId"],
        employees_id=request.json["employeeId"]
    )
    db.session.add(new_project)
    db.session.commit()
    try:
        publicar = GCP()
        publicar.publisher_message(
            {
                "where": "employee-projects",
                "project_id": request.json["projectId"],
                "employees_id": request.json["employeeId"]
            }
        )
    except Exception as e:
        print(e)
    return {"message": f"employee was link with the project"}, 200

