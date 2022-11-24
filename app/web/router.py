from fastapi.routing import APIRouter
from app.web import docs
from app.web import profile

api_router = APIRouter()
api_router.include_router(docs.router)
api_router.include_router(profile.router, prefix='/user/profile', tags=['User Profile'])
