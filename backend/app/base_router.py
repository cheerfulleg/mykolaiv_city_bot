from fastapi import APIRouter

from app.admin.router import admin_router
from app.users.router import user_router

base_router = APIRouter()

base_router.include_router(user_router, prefix="/user", tags=["User endpoints"])
base_router.include_router(admin_router, prefix="/admin", tags=["Admin endpoints"])