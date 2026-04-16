from uuid import UUID

from pydantic import BaseModel


class GroupCreate(BaseModel):
    name: str
    address_sid: UUID

class GroupGet(BaseModel):
    GroupsList: list
    AddressName: str

class GroupUpdate(BaseModel):
    name: str | None = None
    is_active: bool | None = None

class GroupRegistration(BaseModel):
    address_sid: UUID