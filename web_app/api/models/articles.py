from sqlalchemy import String, Text
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from api.models._base import Base


class Article(Base):
    __tablename__ = "articles"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(300))
    content: Mapped[str] = mapped_column(Text())

