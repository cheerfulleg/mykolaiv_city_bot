from app.base_service import BaseService
from config.settings import database


class UserService(BaseService):
    collection = database.get_collection("users")


class ApplicationService(BaseService):
    collection = database.get_collection("applications")


class PollAnswerService(BaseService):
    collection = database.get_collection("poll_answers")
