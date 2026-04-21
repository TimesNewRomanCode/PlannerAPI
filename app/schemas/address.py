import uuid

from pydantic import BaseModel

class AddressCreate(BaseModel):
    pass

class AddressUpdate(BaseModel):
    pass

class AddressRegistration(BaseModel):
    college_sid: uuid.UUID