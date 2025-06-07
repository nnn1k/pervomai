from backend.src.database.base import Base, engine
from backend.src.database.models.users import UserModel

async def recreate():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
