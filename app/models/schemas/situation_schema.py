from app.db_config import ma
from app.models.tables.situation_product import Situation_product


class SituationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Situation_product
        load_instance = True
        exclude=['updated_at', 'created_at']