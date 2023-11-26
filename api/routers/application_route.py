from fastapi import APIRouter
from yourapp.database import Database
from yourapp.schemas import ApplicationSchema, ApplicationInResponse

router = APIRouter()
db = Database()

@router.post("/applications/", response_model=ApplicationInResponse)
def create_application(app: ApplicationSchema):
    app_id = db.create_application(app.dict())
    return {**app.dict(), "app_id": app_id}