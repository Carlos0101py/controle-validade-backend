from app.db_config import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship, backref
from sqlalchemy import String, Text, Double, ForeignKey, INTEGER, DateTime
from uuid import uuid4


class Product(Base):
    name: Mapped[str] = mapped_column(String(100), unique=False, nullable=False)
    description: Mapped[str] = mapped_column(Text, unique=False, nullable=True)
    manufacture_at: Mapped[DateTime] = mapped_column(DateTime, unique=False, nullable=False)
    expiry_at: Mapped[DateTime] = mapped_column(DateTime, unique=False, nullable=False)
    product_code: Mapped[str] = mapped_column(String(90), unique=False, nullable=False)
    batch: Mapped[str] = mapped_column(String(60), unique=True, nullable=False)
    stockQuantity: Mapped[Double] = mapped_column(Double, unique=False, nullable=False) 
    supplier: Mapped[str] = mapped_column(String(100), unique=False, nullable=False)
    situation: Mapped[int] = mapped_column(INTEGER, ForeignKey("situation_product.id"), unique=False, nullable=False)
    status: Mapped[int] = mapped_column(INTEGER, ForeignKey("status_product.id"), unique=False, nullable=False)
    user_id: Mapped[str] = mapped_column(String(100), ForeignKey("user.id"), unique=False, nullable=False)
    category_id: Mapped[str] = mapped_column(String(100), ForeignKey("category.id"), unique=False, nullable=False)

    def __ini__(self, name:str, description:str, manufacture_at:DateTime, expiry_at:DateTime,
                product_code:str, batch:str, stockQuantity:Double, supplier:str,
                category_id:str, user_id:str, situation:int, status:int):
        self.name = name
        self.description = description
        self.manufacture_at = manufacture_at
        self.expiry_at = expiry_at
        self.Product_code = product_code
        self.batch = batch
        self.stockQuantity = stockQuantity
        self.supplier = supplier
        self.user_id = user_id
        self.category_id = category_id
        self.situation = situation
        self.status = status