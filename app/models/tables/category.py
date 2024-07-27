from app.db_config import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship, backref
from sqlalchemy import String, Text, Double, ForeignKey
from uuid import uuid4


class Category(Base):
    name:Mapped[str] = mapped_column(String(45), unique=True, nullable=False)
    product = relationship('Product', backref='category')

    def __init__(self, name:str):
        self.name = name