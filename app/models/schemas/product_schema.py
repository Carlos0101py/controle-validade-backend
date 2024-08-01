from app.db_config import ma
from app.models.tables.product import Product
from app.models.schemas.situation_schema import SituationSchema
from app.models.schemas.status_schema import StatusSchema
from app.models.schemas.user_schema import UserSchema


class ProductSchema(ma.SQLAlchemyAutoSchema):
    situation = ma.Nested(SituationSchema)
    status = ma.Nested(StatusSchema)
    user = ma.Nested(UserSchema)
    class Meta:
        model = Product
        load_instance = True