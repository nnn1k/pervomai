from datetime import date

from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.src.database.base import Base, int_pk, created_at, updated_at


class NewsModel(Base):
    __tablename__ = 'news'

    id: Mapped[int_pk]
    title: Mapped[str] = mapped_column(nullable=True)
    description: Mapped[str] = mapped_column(nullable=True)
    date: Mapped[date]
    image_url: Mapped[str] = mapped_column(nullable=True)

