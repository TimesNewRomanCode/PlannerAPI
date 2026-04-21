from pydantic import BaseModel

class CollegeGet(BaseModel):
    sid: list
    name: str

class CollegeUpdate(BaseModel):
    pass

class CollegeCreate(BaseModel):
    pass
