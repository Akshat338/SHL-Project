""" Project endpoints """
from models import Project, Base
from sqlalchemy import func
from sqlalchemy.orm import Session
from config import ERROR_RESPONSES
from db import SessionLocal, engine
from fastapi import APIRouter, HTTPException, Query, Depends
from schemas.project_schema import (GetProjectResponseModel,
                                    GetAllProjectsResponseModel)

Base.metadata.create_all(bind=engine)

router = APIRouter(tags=["Project"], responses=ERROR_RESPONSES)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get(
    "/projects/{title}",
    name="Get a particular project",
    response_model=GetProjectResponseModel,
)
def get_project(title: str, db: Session = Depends(get_db)):
    """
    Get details of a specific project.

    Parameters:
    - title (str): The title of the project.

    Returns:
    - dict: Details of the project.
    """
    try:
        project = db.query(Project).filter(
            Project.project_title == title).first()
        if project is None:
            raise HTTPException(status_code=404, detail="Project not found")
        return {
            "success": True,
            "message": "Successfully fetched the project",
            "data": project,
        }
    except HTTPException as http_exception:
        return {
            "success": False,
            "message": f"Error: {http_exception.detail}",
            "data": None,
        }
    except Exception as exception:
        return {
            "success": False,
            "message": f"Unexpected error: {str(exception)}",
            "data": None,
        }


@router.get("/projects",
            name="Get all Projects",
            response_model=GetAllProjectsResponseModel)
def get_all_projects(
        skip: int = Query(0, alias="page", ge=0),
        limit: int = Query(10, le=1000),
        db: Session = Depends(get_db),
):
    """
    Get details of all projects with pagination.

    Parameters:
    - skip (int): Number of items to skip.
    - limit (int): Maximum number of items to return.

    Returns:
    - List[dict]: List of project details.
    """
    try:
        result = db.query(Project).offset(skip).limit(limit).all()
        return {
            "success": True,
            "message": "Successfully fetched the projects",
            "data": result,
        }
    except Exception as exception:
        return {
            "success": False,
            "message": f"Unexpected error: {str(exception)}",
            "data": None,
        }


@router.get("/projects/search",
            name="Search Projects",
            response_model=GetAllProjectsResponseModel)
def search_projects(
        query: str = Query(..., title="Search Query"),
        db: Session = Depends(get_db),
):
    """
    Search projects based on a query.

    Parameters:
    - query (str): The search query.

    Returns:
    - List[dict]: List of project details matching the search query.
    """
    try:
        result = db.query(Project).filter(
            func.lower(Project.project_title).contains(
                func.lower(query))).all()
        return {
            "success": True,
            "message": f"Successfully fetched projects matching '{query}'",
            "data": result,
        }
    except Exception as exception:
        return {
            "success": False,
            "message": f"Unexpected error: {str(exception)}",
            "data": None,
        }
