from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.src.database.base import Base, int_pk, created_at, updated_at


class UserModel(Base):
    __tablename__ = 'users'

    id: Mapped[int_pk]
    login: Mapped[str]
    password: Mapped[str]




