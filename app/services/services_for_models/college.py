from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories import college_repository
from typing import List

class CollegeServices:
    async def get_colleges_array(self, session: AsyncSession) -> List[str]:
        existing_college = await college_repository.get_all(session)
        college_names = [college.name for college in existing_college]

        return college_names

    async def get_colleges_by_registration(self, session: AsyncSession) -> List[dict]:
        existing_college = await college_repository.get_all(session)

        result = []
        for college in existing_college:
            result.append({
                "sid": college.sid,
                "name": college.name,
            })

        return result