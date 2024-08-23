from app.db_config import Base
from app.models.tables.user_has_group import user_has_group
from app.models.tables.product_has_group import product_has_group
from sqlalchemy.orm import Mapped, mapped_column, relationship, backref
from sqlalchemy import String, Text, Double, ForeignKey, INTEGER, DateTime
from uuid import uuid4


class Group(Base):
    __tablename__ = 'group'
    
    name: Mapped[str] = mapped_column(String(100), unique=False, nullable=False)
    creator_id: Mapped[str] = mapped_column(String(100), unique=False, nullable=False)
    users = relationship("User", secondary=user_has_group, back_populates="groups")
    products = relationship("Product", secondary=product_has_group, back_populates="groups")

    def __init__(self, name:str, creator_id:str):
        self.name = name
        self.creator_id = creator_id