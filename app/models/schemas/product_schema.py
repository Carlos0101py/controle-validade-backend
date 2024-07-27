from app.db_config import ma
from app.models.tables.product import Product


class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        load_instance = True