from app.db_config import db
from app.models.tables.user import User
from flask import jsonify, request, Blueprint
from app.models.schemas.user_schema import UserSchema
from werkzeug.security import generate_password_hash, check_password_hash


user_route = Blueprint('user_route', __name__)

@user_route.route('/api/v1/create_user', methods=["POST"])
def create_user():
    if request.method == 'POST':
        try:
            body = request.get_json()
            name = body['name']
            username = body['username']
            email = body['email']
            password = body['password']
            re_password = body['re_password']

            if password != re_password:
                return jsonify({
                    'status': 'error',
                    'message': 'Atenção, Senhas não coencidem'
                }), 400
            
            password_hash = generate_password_hash(password)

            user = User(name=name, username=username, email=email, password_hash=password_hash)
            db.session.add(user)
            db.session.commit()
            db.session.close()

            return jsonify({
                'status': 'ok',
                'message': 'Usuário cadastrado com secesso, obrigado!'
            }), 201
        
        except Exception as error:
            return jsonify({
                    'status': 'error',
                    'message': 'An error has occurred!'
                }), 500
        

@user_route.route('/api/v1/get_one_user', methods=["GET"])
def get_one_user():
    if request.method == 'GET':
        try:
            body = request.get_json()
            username = body['username']
            user = User.query.filter_by(username=username).first()
            user_schema = UserSchema()
            payload = user_schema.dump(user)

            if user == None:
                return jsonify({
                    'status': 'error',
                    'message': 'Usuário não existe!'
                }), 404
            
            return jsonify({
                'status': 'ok',
                'user': payload
            })
        
        except:
            return jsonify({
                    'status': 'error',
                    'message': 'An error has occurred!'
                }), 500


@user_route.route('/api/v1/get_users', methods=["GET"])
def get_users():
    if request.method == 'GET':
        try:
            users = User.query.all()
            user_schema = UserSchema(many=True)
            payload = user_schema.dump(users)

            if not users:
                return jsonify({
                    'status': 'error',
                    'message': 'Não existe usuários cadastrados!'
                }), 404

            return jsonify({
                'users': payload
            }), 200
        
        except:
            return jsonify({
                    'status': 'error',
                    'message': 'An error has occurred!'
                }), 500