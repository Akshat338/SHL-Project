"""SQLAlchemy Model"""
from sqlalchemy import Column, String
from db import Base


class Project(Base):
    __tablename__ = "projects"

    project_title = Column(String(255), primary_key=True, index=True)
    project_technologies = Column(String(255))
    technical_skillset_frontend = Column(String(255))
    technical_skillset_backend = Column(String(255))
    technical_skillset_databases = Column(String(255))
    technical_skillset_infrastructure = Column(String(255))
    other_information_availability = Column(String(255))
