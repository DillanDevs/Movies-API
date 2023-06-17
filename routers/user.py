from fastapi import APIRouter
from fastapi.responses import JSONResponse
from utils.jwt_manager import create_token
from schemas.user import User

user_router = APIRouter()



@user_router.post("/login", tags=["Authentication"])
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "123456":
        token = create_token(user.dict()) 
        return JSONResponse(status_code=200,content=token)