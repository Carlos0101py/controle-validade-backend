from app.db_config import Base, db
from sqlalchemy.orm import Mapped, mapped_column, relationship, backref
from sqlalchemy import Column, String, Table, Text, Double, ForeignKey, INTEGER, DateTime
from uuid import uuid4


product_has_group = Table(
    'product_has_group', db.metadata,
    Column('product_id', String(100), ForeignKey('product.id'), primary_key=True),
    Column('group_id', String(100), ForeignKey('group.id'), primary_key=True)
)