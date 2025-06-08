from sqlalchemy.ext.asyncio import AsyncSession

from backend.src.database.base import Base, engine, session_factory
from backend.src.database.models.users import UserModel
from backend.src.database.models.news import NewsModel
from backend.src.database.models.photos import PhotoModel
from backend.src.database.models.players import PlayerModel
from backend.src.database.models.matches import MatchModel



async def recreate():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def add_all():
    async with session_factory() as session:
        user = UserModel(login="string", password="string")
        session.add(user)
        await session.commit()
