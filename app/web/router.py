from fastapi.routing import APIRouter

from app.web import docs
api_router = APIRouter()
api_router.include_router(docs.router)
