from app.db_config import db
from app.models.tables.group import Group
from app.models.tables.user_has_group import user_has_group
from app.models.tables.product_has_group import product_has_group
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


@group_route.route('/api/v1/add_new_member', methods=["POST"])
def add_new_member():
    if request.method == 'POST':
        try:
            body = request.get_json()
            user_id = body['user_id']
            group_id = body['group_id']

            user_has_group_entry = {
                'user_id': user_id,
                'group_id': group_id 
            }
            db.session.execute(user_has_group.insert().values(user_has_group_entry))
            db.session.commit()

            return jsonify({
                'status': 'ok',
                'message': 'Novo membro adicionado com sucesso!'
            }), 201
        
        except Exception as error:
            print(error)
            return jsonify({
                    'status': 'error',
                    'message': 'An error has occurred!'
                }), 500
        

# @group_route.route('/api/v1/add_new_product', methods=["POST"])
# def add_new_member():
#     if request.method == 'POST':
#         try:
#             body = request.get_json()
#             product_id = body['product_id']
#             group_id = body['group_id']

#             product_has_group_entry = {
#                 'product_id': product_id,
#                 'group_id': group_id 
#             }
#             db.session.execute(product_has_group.insert().values(product_has_group_entry))
#             db.session.commit()

#             return jsonify({
#                 'status': 'ok',
#                 'message': 'Novo mebro adicionado com sucesso!'
#             }), 201
        
#         except Exception as error:
#             print(error)
#             return jsonify({
#                     'status': 'error',
#                     'message': 'An error has occurred!'
#                 }), 500
