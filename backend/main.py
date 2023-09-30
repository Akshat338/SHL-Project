"""
  Project Management Service
"""
import uvicorn
from fastapi import FastAPI
from routes import project
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/ping")
def health_check() -> dict:
    """
    Endpoint to check the service health
    """
    return {
        "success": True,
        "message": "Successfully reached Project Management Service",
        "data": {},
    }


api = FastAPI(title="Project Service APIs", version="latest")

api.include_router(project.router)

app.mount("/project-management/api/v1", api)

if __name__ == "__main__":
    uvicorn.run("main:app", log_level="debug", reload=True)
