import uuid

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.common.db.base_repository import BaseRepository
from app.models import Group, Address, User

from app.schemas.group import GroupUpdate, GroupCreate


class GroupRepository(BaseRepository[Group, GroupCreate, GroupUpdate]):
    @staticmethod
    async def get_group_by_address(session: AsyncSession, address_name: str):
        query = (
            select(Group)
            .join(Address, Address.sid == Group.address_sid)
            .where(Address.name == address_name)
            .order_by(Group.name.asc())
        )
        result = await session.execute(query)
        return result.scalars().all()

    @staticmethod
    async def get_group_by_address_sid(session: AsyncSession, address_sid: uuid.UUID):
        query = (
            select(Group)
            .join(Address, Address.sid == Group.users)
            .where(Address.sid == address_sid)
            .order_by(Group.name.asc())
        )
        result = await session.execute(query)
        return result.scalars().all()


    @staticmethod
    async def get_group_by_address_name(session: AsyncSession, address_name: str):
        query = (
            select(Group)
            .join(Address)
            .where(Address.name == address_name)
            .order_by(Group.name.asc())
        )
        result = await session.execute(query)
        return result.scalars().all()

    @staticmethod
    async def get_all_by_group_sid(session: AsyncSession, group_sid: uuid):
        stmt = (
            select(Group)
            .options(
                joinedload(Group.address)
                .joinedload(Address.college),
            )  # todo посмотреть как правильно
            .where(Group.sid == group_sid)
        )
        result = await session.execute(stmt)
        return result.scalar_one_or_none()


group_repository = GroupRepository(Group)
