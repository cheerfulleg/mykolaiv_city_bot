from pydantic import Field

from app.mixins import TimestampMixin, MongoMixin, PyObjectId


class PostModel(TimestampMixin, MongoMixin):
    telegram_id: int = Field(...)
    content: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "telegram_id": 380983134,
                "content": "My awesome application"
            }
        }


class PostModelOut(PostModel):
    id: PyObjectId = Field(..., alias="_id")
    related_telegram_ids: list[int]

    class Config:
        schema_extra = {
            "example": {
                "_id": "626434e4f3e946a5a988ba56",
                "timestamp": "2022-04-22T15:12:49.077000",
                "telegram_id": 380983134,
                "content": "My awesome post",
                "related_telegram_ids": [380983134]
            }
        }


class PollModel(MongoMixin, TimestampMixin):
    telegram_id: int = Field(...)
    question: str = Field(...)
    answers: list[str]

    class Config:
        schema_extra = {
            "example": {
                "telegram_id": 380983134,
                "question": "Poll question",
                "answers": [
                    "answer 1",
                    "answer 2",
                    "answer 3",
                ]
            }
        }


class PollModelOut(PollModel):
    id: PyObjectId = Field(..., alias="_id")
    related_telegram_ids: list[int]

    class Config:
        schema_extra = {
            "example": {
                "_id": "626434e4f3e946a5a988ba56",
                "timestamp": "2022-04-22T15:12:49.077000",
                "telegram_id": 380983134,
                "question": "Poll question",
                "answers": [
                    "answer 1",
                    "answer 2",
                    "answer 3",
                ],
                "related_telegram_ids": [380983134]
            }
        }
