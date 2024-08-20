from flask import Flask
from flask_mysqldb import MySQL
from .db_config import db, migrate, ma
from dotenv import load_dotenv
from app.controllers.routes.user_routes import user_route
from app.controllers.routes.category_route import category_route 
from app.controllers.routes.product_route import product_route
from app.controllers.routes.group_route import group_route
import os


load_dotenv()

def create_app():

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    app.register_blueprint(user_route)
    app.register_blueprint(category_route)
    app.register_blueprint(product_route)
    app.register_blueprint(group_route)

    return app