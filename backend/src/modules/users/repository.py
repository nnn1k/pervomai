from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from backend.src.database.models.users import UserModel


class UserRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_user(self, **kwargs) -> UserModel:
        stmt = (
            select(UserModel)
            .filter_by(**kwargs)
        )
        result = await self.session.execute(stmt)
        return result.scalars().first()

    async def login(self, login: str, password: str) -> UserModel:
        stmt = (
            select(UserModel)
            .filter_by(login=login, password=password)
        )
        result = await self.session.execute(stmt)
        return result.scalars().first()

