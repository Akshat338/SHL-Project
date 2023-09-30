"""
Pydantic Model for Project API's
"""
from typing import List, Optional
from pydantic import BaseModel, Extra

BASIC_PROJECT_MODEL_EXAMPLE = {
    "project_title": "Project 1",
    "project_technologies": "Python, HTML, CSS, Machine Learning, Deep Learning",
    "technical_skillset_frontend": "HTML, CSS, JavaScript",
    "technical_skillset_backend": "Python",
    "technical_skillset_databases": "",
    "technical_skillset_infrastructure": "",
    "other_information_availability": "Available to join immediately",
}


class ProjectDetailsModel(BaseModel):
    """Project Skeleton Pydantic Model"""

    project_title: str
    project_technologies: str
    technical_skillset_frontend: str
    technical_skillset_backend: str
    technical_skillset_databases: str
    technical_skillset_infrastructure: str
    other_information_availability: str

    class Config:
        from_attributes = True
        # extra = Extra.forbid


class GetProjectResponseModel(BaseModel):
    """Project Response Pydantic Model"""

    success: Optional[bool] = True
    message: Optional[str] = "Successfully fetched the project"
    data: Optional[ProjectDetailsModel]

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "success": True,
                "message": "Successfully fetched the project",
                "data": BASIC_PROJECT_MODEL_EXAMPLE,
            }
        }


class GetAllProjectsResponseModel(BaseModel):
    """Project Response Pydantic Model"""

    success: Optional[bool] = True
    message: Optional[str] = "Successfully fetched the project"
    data: Optional[List[ProjectDetailsModel]]

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "success": True,
                "message": "Successfully fetched the project",
                "data": [BASIC_PROJECT_MODEL_EXAMPLE],
            }
        }
