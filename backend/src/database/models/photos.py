from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.src.database.base import Base, int_pk, created_at, updated_at
from datetime import date


class PhotoModel(Base):
    __tablename__ = 'photos'

    id: Mapped[int_pk]
    title: Mapped[str]
    description: Mapped[str]
    date: Mapped[date]
    category: Mapped[str]
    image_url: Mapped[str] = mapped_column(nullable=True)