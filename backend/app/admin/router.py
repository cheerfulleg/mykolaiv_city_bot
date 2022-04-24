from typing import Optional

from fastapi import APIRouter, Body, HTTPException
from pydantic import Field
from starlette import status
from starlette.responses import JSONResponse

from app.admin.models import PostModel, PostModelOut, PollModel, PollModelOut
from app.admin.service import PostService, PollService
from app.users.models import ApplicationModel
from app.users.service import UserService, ApplicationService

admin_router = APIRouter()


@admin_router.post(
    "/post", response_description="Create new post",
    response_model=PostModelOut,
    status_code=status.HTTP_201_CREATED
)
async def create_post(post: PostModel = Body(...), district: Optional[str] = None):
    """
    Create new post, return created post and list of related users (telegram_ids)
    """
    post_obj = await PostService.create(post.dict())
    if district:
        users_by_district = await UserService.filter({"district": district.lower()})
    else:
        users_by_district = await UserService.all()
    telegram_ids = [user['telegram_id'] for user in users_by_district]
    return PostModelOut(**post_obj, related_telegram_ids=telegram_ids)


@admin_router.post(
    "/poll",
    response_description="Create poll",
    response_model=PollModelOut,
    status_code=status.HTTP_201_CREATED
)
async def create_poll(poll: PollModel = Body(...)):
    poll_obj = await PollService.create(poll.dict())
    users = await UserService.all()
    telegram_ids = [user['telegram_id'] for user in users]
    return PollModelOut(**poll_obj, related_telegram_ids=telegram_ids)


@admin_router.get(
    "/check/{telegram_id}",
    response_description="Check if user have admin rights",
    status_code=status.HTTP_200_OK
)
async def is_admin(telegram_id: int = Field(...)):
    user = await UserService.get({"telegram_id": telegram_id})
    if user.get("is_admin"):
        return JSONResponse({"is_admin": True})
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Restricted")


@admin_router.get(
    "/applications",
    response_description="Get last five user applications",
    response_model=list[ApplicationModel],
    status_code=status.HTTP_200_OK
)
async def get_user_applications():
    """
    Hardcoded to receive five last applications
    """
    applications = await ApplicationService.all()
    return applications[-5:]
