
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories import group_repository, address_repository
from typing import List

from app.schemas.group import GroupCreate

class GroupService:

    async def get_groups_array(self, session: AsyncSession, address_name) -> List[str]:
        existing_groups = await group_repository.get_group_by_address(session, address_name)
        group_names = [group.name for group in existing_groups]

        return group_names


    async def get_groups_array_by_address_sid(self, session: AsyncSession, address_sid) -> List[str]:
        existing_groups = await group_repository.get_group_by_address_sid(
            session, address_sid
        )
        result = []
        for group in existing_groups:
            result.append({
                "sid": group.sid,
                "name": group.name,
            })

        return result

    async def get_groups_array_by_address_name(self, session: AsyncSession, address_name) -> List[str]:
        existing_groups = await group_repository.get_group_by_address_name(
            session, address_name
        )
        group_names = [group.name for group in existing_groups]

        return group_names

    async def update_groups(self, session: AsyncSession, address_name: str, groups: List[str]):
        group_names = await self.get_groups_array_by_address_name(session, address_name)
        address = await address_repository.get_address_by_name(session, address_name)
        missing_groups = [
            group_name for group_name in groups if group_name not in group_names
        ]
        for group_name in missing_groups:
            await group_repository.create(
                session,
                obj_in=GroupCreate(name=group_name, address_sid=address.sid),
                with_commit=False,
            )
            print(f"Добавлена группа: {group_name}")

        await session.commit()



