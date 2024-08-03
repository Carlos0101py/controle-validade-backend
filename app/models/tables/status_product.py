from app.db_config import db, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship, backref
from sqlalchemy import String, Text, Double, ForeignKey, INTEGER
from uuid import uuid4


class Status_product(Base):
    # id: Mapped[int] = mapped_column(INTEGER, primary_key=True ,unique=True, nullable=False, autoincrement=True)
    name: Mapped[str] = mapped_column(String(45), unique=True, nullable=False)
    product = relationship('Product', backref='status_product')

    def __init__(self, name:str):
        self.name = name