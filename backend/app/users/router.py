from fastapi import APIRouter, Body, HTTPException
from pydantic import Field
from starlette import status

from app.users.models import UserModel, UserAddressModel, ApplicationModel, PollAnswerOut, PollAnswer
from app.users.service import UserService, ApplicationService, PollAnswerService

user_router = APIRouter()


@user_router.post("", response_description="Add new user", response_model=UserModel,
                  status_code=status.HTTP_201_CREATED)
async def create_user(user: UserModel = Body(...)):
    if await UserService.get({"telegram_id": user.telegram_id}):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists")
    return await UserService.create(user.dict())


@user_router.get("/{telegram_id}/address", response_description="Get user address", response_model=UserAddressModel,
                 status_code=status.HTTP_200_OK)
async def get_user_address(telegram_id: int = Field(...)):
    user = await UserService.get({"telegram_id": telegram_id})
    return UserAddressModel(address=user.get("address"))


@user_router.put("/{telegram_id}/address", response_description="Update user address", response_model=UserAddressModel,
                 status_code=status.HTTP_200_OK)
async def get_user_address(telegram_id: int = Field(...), address: UserAddressModel = Body(...)):
    user = await UserService.update({"telegram_id": telegram_id}, address.dict())
    return UserAddressModel(address=user.get("address"))


@user_router.post("/application", response_description="Create application", response_model=ApplicationModel,
                  status_code=status.HTTP_201_CREATED)
async def create_application(application: ApplicationModel = Body(...)):
    return await ApplicationService.create(application.dict())


@user_router.post("/poll-answer", response_description="Create poll answer", response_model=PollAnswerOut,
                  status_code=status.HTTP_201_CREATED)
async def create_poll_answer(poll_answer: PollAnswer = Body(...)):
    return await PollAnswerService.create(poll_answer.dict())
