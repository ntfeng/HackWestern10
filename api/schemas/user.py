from pydantic import BaseModel, Field, EmailStr
from typing import List
from datetime import datetime
from pydantic import BaseModel, Field, EmailStr
from typing import List
from datetime import datetime
class AppAccess(BaseModel):
    app_id: int
    access_level: str

class UserSchema(BaseModel):
    userid: int = Field(..., description="The unique identifier for the user")
    app_access_list: List[AppAccess] = Field(..., description="List of apps with access levels")
    password: str = Field(..., description="Password for the user account")
    first_name: str = Field(..., description="User's first name")
    last_name: str = Field(..., description="User's last name")
    email: EmailStr = Field(..., description="User's email address")
    creation_date: datetime = Field(default_factory=datetime.now, description="Account creation date")

    class Config:
        schema_extra = {
            "example": {
                "userid": 12345,
                "app_access_list": [
                    {"app_id": 1, "access_level": "R"},
                    {"app_id": 2, "access_level": "W"}
                ],
                "password": "securepassword123",
                "first_name": "John",
                "last_name": "Doe",
                "email": "johndoe@example.com",
                "creation_date": "2023-11-24T12:00:00"
            }
        }
class UserInDB(UserSchema):
    hashed_password: str

class UserInResponse(BaseModel):
    userid: int
    app_access_list: List[AppAccess]
    first_name: str
    last_name: str
    email: EmailStr
    creation_date: datetime