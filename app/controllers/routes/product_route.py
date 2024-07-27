from app.db_config import db
from app.models.tables.product import Product
from flask import jsonify, request, Blueprint
from app.models.schemas.product_schema import ProductSchema
from werkzeug.security import generate_password_hash, check_password_hash


product_route = Blueprint('product_route', __name__)