from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

class ScheduleMe(BaseModel):
    user_sid: UUID
    date: datetime

class ScheduleAlien(BaseModel):
    group_sid: UUID
    date: datetime

class ScheduleGroup(BaseModel):
    user_sid: UUID