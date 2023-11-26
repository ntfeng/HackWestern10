#import fastapi dependencies
from fastapi import APIRouter, Depends, HTTPException, status
from database import Database
router = APIRouter(
    tags=['demo_utils']
)

db = Database().db

@router.post("/add_users")
#takes a user schema
async def add_users(user: UserSchema):
    #add the user to the database
    return db.create_user(user.dict())


@router.post("/add_applications")


    