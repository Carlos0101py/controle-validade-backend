from app.db_config import Base, db
from sqlalchemy.orm import Mapped, mapped_column, relationship, backref
from sqlalchemy import Column, String, Table, Text, Double, ForeignKey, INTEGER, DateTime
from uuid import uuid4


user_has_group = Table(
    'user_has_group', db.metadata,
    Column('user_id', String(100), ForeignKey('user.id'), primary_key=True),
    Column('group_id', String(100), ForeignKey('group.id'), primary_key=True)
)
