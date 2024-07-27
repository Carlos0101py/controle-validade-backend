from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from sqlalchemy import String
import uuid
from datetime import datetime

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()

class Base(db.Model):
    
    __abstract__ = True

    id = db.Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)