from app.base_service import BaseService
from config.settings import database


class PostService(BaseService):
    collection = database.get_collection("posts")


class PollService(BaseService):
    collection = database.get_collection("polls")
