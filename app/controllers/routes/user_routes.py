from app.db_config import db
from app.models.tables.user import User
from flask import jsonify, request, Blueprint
from app.models.schemas.user_schema import UserSchema
from werkzeug.security import generate_password_hash, check_password_hash


user_route = Blueprint('user_route', __name__)