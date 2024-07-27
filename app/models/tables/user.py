from app.db_config import Base
from app.models.tables.product import Product
from sqlalchemy.orm import Mapped, mapped_column, relationship, backref
from sqlalchemy import String, Text
from uuid import uuid4


class User(Base):
    name: Mapped[str] = mapped_column(String(100), unique=False, nullable=False)
    username: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(320), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(Text, unique=False, nullable=False)
    product = relationship('Product', backref='user')
    
    def __init__(self, name:str, username:str, email:str, password_hash:str):
        self.name = name
        self.username = username
        self.email = email
        self.password_hash = password_hash
