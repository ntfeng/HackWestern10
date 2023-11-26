from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ApplicationSchema(BaseModel):
    app_id: int = Field(..., description="Unique identifier for the application")
    app_name: str = Field(..., description="Name of the application")
    container_port: int = Field(..., description="Docker container port")
    description: Optional[str] = Field(None, description="Description of the application")
    creation_date: datetime = Field(default_factory=datetime.now, description="Application creation date")

    class Config:
        schema_extra = {
            "example": {
                "app_id": 1001,
                "app_name": "Example App",
                "container_port": 8080,
                "description": "A sample application",
                "creation_date": "2023-11-24T12:00:00"
            }
        }

class ApplicationInResponse(BaseModel):
    app_id: int
    app_name: str
    container_port: int
