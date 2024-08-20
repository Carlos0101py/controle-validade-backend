from app.db_config import db
from app.models.tables.group import Group
from app.models.tables.user_has_group import user_has_group
from flask import jsonify, request, Blueprint
from app.models.schemas.group_schema import GroupSchema
from werkzeug.security import generate_password_hash, check_password_hash
import os, jwt


group_route = Blueprint('group_route', __name__)

@group_route.route('/api/v1/create_group', methods=["POST"])
def create_group():
    if request.method == 'POST':
        try:
            body = request.get_json()
            name = body['name']
            creator_id = body['creator']

            new_group = Group(name=name, creator_id=creator_id)
            db.session.add(new_group)
            db.session.commit()

            user_has_group_entry = {
                'user_id': creator_id,
                'group_id': new_group.id
            }
            db.session.execute(user_has_group.insert().values(user_has_group_entry))
            db.session.commit()

            return jsonify({
                'status': 'ok',
                'message': 'Gropo criado com sucesso!'
            }), 201

        except Exception as error:
            return jsonify({
                    'status': 'error',
                    'message': 'An error has occurred!'
                }), 500