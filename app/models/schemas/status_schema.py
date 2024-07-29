from app.db_config import ma
from app.models.tables.status_product import Status_product


class StatusSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Status_product
        load_instance = True