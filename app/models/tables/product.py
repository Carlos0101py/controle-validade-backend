from app.db_config import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship, backref
from sqlalchemy import String, Text, Double, ForeignKey
from uuid import uuid4


class Product(Base):
    name: Mapped[str] = mapped_column(String(100), unique=False, nullable=False)
    description: Mapped[str] = mapped_column(Text, unique=False, nullable=True)
    manufacture_at: Mapped[str] = mapped_column(String(45), unique=False, nullable=False)
    expiry_at: Mapped[str] = mapped_column(String(45), unique=False, nullable=False)
    Product_code: Mapped[str] = mapped_column(String(90), unique=False, nullable=False)
    batch: Mapped[str] = mapped_column(String(60), unique=True, nullable=False)
    stockQuantity: Mapped[Double] = mapped_column(Double, unique=False, nullable=False) 
    supplier: Mapped[str] = mapped_column(String(100), unique=False, nullable=False)
    user_id: Mapped[str] = mapped_column(String(100), ForeignKey("user.id"), unique=False, nullable=False)
    category_id: Mapped[str] = mapped_column(String(100), ForeignKey("category.id"), unique=False, nullable=False)

    def __ini__(self, name:str, description:str, manufacture_at:str, expiry_at:str,
                Product_code:str, batch:str, stockQuantity:Double, supplier:str,
                category_id:str, user_id:str):
        self.name = name
        self.description = description
        self.manufacture_at = manufacture_at
        self.expiry_at = expiry_at
        self.Product_code = Product_code
        self.batch = batch
        self.stockQuantity = stockQuantity
        self.supplier = supplier
        self.user_id = user_id
        self.category_id = category_id