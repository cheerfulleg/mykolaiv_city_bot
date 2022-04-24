from pydantic import BaseModel, Field

from app.mixins import MongoMixin, TimestampMixin, PyObjectId


class UserModel(MongoMixin):
    is_admin: bool = Field(default=False)
    first_name: str = Field(...)
    last_name: str = Field(...)
    district: str = Field(...)
    address: str = Field(...)
    phone: int = Field(...)
    telegram_id: int = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "is_admin": False,
                "first_name": "Jane",
                "last_name": "Doe",
                "address": "Magic Str",
                "phone": 380981234567,
                "telegram_id": 380983134
            }
        }


class UserAddressModel(BaseModel):
    address: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "address": "Magic Str"
            }
        }


class ApplicationModel(TimestampMixin, MongoMixin):
    id: PyObjectId = Field(..., alias="_id")
    telegram_id: int = Field(...)
    content: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "telegram_id": 380983134,
                "content": "My awesome application"
            }
        }


class PollAnswer(TimestampMixin, MongoMixin):
    telegram_id: int = Field(...)
    question: str = Field(...)
    answer: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "telegram_id": 380983134,
                "question": "Poll question",
                "answer": "variant 1"
            }
        }


class PollAnswerOut(PollAnswer):
    id: PyObjectId = Field(..., alias="_id")

    class Config:
        schema_extra = {
            "example": {
                "_id": "626434e4f3e946a5a988ba56",
                "telegram_id": 380983134,
                "question": "Poll question",
                "answer": "variant 1"
            }
        }
