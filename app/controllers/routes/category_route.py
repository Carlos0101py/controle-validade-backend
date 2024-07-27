from app.db_config import db
from app.models.tables.category import Category
from flask import jsonify, request, Blueprint
from app.models.schemas.category_schema import CategorySchema
from werkzeug.security import generate_password_hash, check_password_hash


category_route = Blueprint('category_route', __name__)