from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.src.database.base import Base, int_pk, created_at, updated_at


class PlayerModel(Base):
    __tablename__ = 'players'

    id: Mapped[int_pk]
    name: Mapped[str]
    surname: Mapped[str]
    number: Mapped[int]
    position: Mapped[str]
    image_url: Mapped[str] = mapped_column(nullable=True)
