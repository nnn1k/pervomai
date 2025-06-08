from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.src.database.base import Base, int_pk, created_at, updated_at


class MatchModel(Base):
    __tablename__ = 'matches'

    id: Mapped[int_pk]
    time: Mapped[datetime]
    opponent: Mapped[str]
    stadion: Mapped[str]
    result: Mapped[str]
