#import fast api dependencies
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
#import schemas
from schemas.user import UserSchema, UserInResponse

from authentication.endpoints import oauth2_scheme, authenticate_user, create_access_token, verify_token


#initialize router
router = APIRouter(
    tags=['Authentication']
)



@router.get("/users/me/", response_model=UserInResponse)
async def read_users_me(token: str = Depends(oauth2_scheme)):
    username = verify


#export router
appliction_route = router
