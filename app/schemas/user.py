import uuid
from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    sid: uuid.UUID
    group_sid: uuid.UUID
    username: str | None = Field(
        default=None,
        min_length=3,
        max_length=50,
        description="Имя пользователя от 3 до 50 символов"
    )
    is_active: bool | None


class UserUpdate(BaseModel):
    group_sid: uuid.UUID
    username: str | None
    is_active: bool | None

class UserRegistration(BaseModel):
    username: str
    group_sid: uuid.UUID

