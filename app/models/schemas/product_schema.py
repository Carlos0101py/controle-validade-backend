from app.db_config import ma
from app.models.tables.product import Product
from app.models.schemas.category_schema import CategorySchema
from app.models.schemas.status_schema import StatusSchema
from app.models.schemas.user_schema import UserSchema


class ProductSchema(ma.SQLAlchemyAutoSchema):
    status_product = ma.Nested(StatusSchema)
    user = ma.Nested(UserSchema)
    category = ma.Nested(CategorySchema)
    class Meta:
        model = Product
        load_instance = True