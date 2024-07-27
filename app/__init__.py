from flask import Flask
from flask_mysqldb import MySQL
from .db_config import db, migrate, ma
from dotenv import load_dotenv
from app.controllers.routes.user_routes import user_route
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

    return app