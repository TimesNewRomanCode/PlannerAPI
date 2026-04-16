from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories import address_repository
from typing import List

class AddressServices:
    async def get_address_by_college_name(self, session: AsyncSession, college_name) -> List[str]:
        existing_address = await address_repository.get_address_by_college(
            session, college_name
        )
        address_names = [address.name for address in existing_address]

        return address_names

    async def get_addresses_array_by_college_sid(self, session: AsyncSession, college_sid) -> List[str]:
        existing_address = await address_repository.get_addresses_array_by_sid(
            session, college_sid
        )
        result = []
        for address in existing_address:
            result.append({
                "sid": address.sid,
                "name": address.name,
            })

        return result

