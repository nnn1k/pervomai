from fastapi import APIRouter

from backend.views.admin import router as admin_router
from backend.views.test import router as test_router

backend_router = APIRouter(
    prefix='/api'
)

backend_router.include_router(admin_router)
backend_router.include_router(test_router)