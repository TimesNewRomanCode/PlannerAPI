import uuid
from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.s3 import get_image_from_s3
from app.repositories import user_repository, group_repository


class ScheduleService:
    async def get_photo_by_user_sid_and_date(self, session: AsyncSession, user_sid: uuid, date: datetime):
        user = await user_repository.get_all_by_user_sid(
            session, user_sid
        )
        day_month = int(date.strftime("%d%m"))
        key_for_s3 = f"{user.college_name}/{user.address_name}/{day_month}/{user.group_name}.png"
        group_name = user.group_name
        photo = get_image_from_s3(key_for_s3, group_name)
        return photo


    async def get_photo_by_group_sid_and_date(self, session: AsyncSession, group_sid: uuid, date: datetime):
        group = await group_repository.get_all_by_group_sid(
            session, group_sid
        )
        day_month = int(date.strftime("%d%m"))
        key_for_s3 = f"{group.college_name}/{group.address_name}/{day_month}/{group.name}.png"
        group_name = group.name
        photo = get_image_from_s3(key_for_s3, group_name)
        return photo

