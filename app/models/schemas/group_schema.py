from app.db_config import ma
from app.models.tables.group import Group


class GroupSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Group
        load_instance = True