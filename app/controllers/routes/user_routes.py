from app.db_config import db
from app.models.tables.user import User
from flask import jsonify, request, Blueprint
from app.models.schemas.user_schema import UserSchema
from werkzeug.security import generate_password_hash, check_password_hash
import os, jwt


user_route = Blueprint('user_route', __name__)

@user_route.route('/api/v1/create_user', methods=["POST"])
def create_user():

    """
    Create a new user.
    ---
    parameters:
      - name: body
        in: body
        required: true
        description: JSON body with user details
        schema:
          type: object
          required:
            - name
            - username
            - email
            - password
            - re_password
          properties:
            name:
              type: string
              description: The name of the user
            username:
              type: string
              description: The username for the account
            email:
              type: string
              description: The email of the user
            password:
              type: string
              description: The password for the account
            re_password:
              type: string
              description: Confirmation of the password
    responses:
      201:
        description: User successfully created
      400:
        description: Passwords do not match
      500:
        description: Internal server error
    """

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
        

@user_route.route('/api/v1/login', methods=["POST"])
def authenticate_user():

    """
    Login to the system.
    ---
    parameters:
      - name: body
        in: body
        required: true
        description: JSON body with username and password
        schema:
          type: object
          required:
            - username
            - password
          properties:
            username:
              type: string
              description: The username for the account
            password:
              type: string
              description: The password for the account
    responses:
      200:
        description: user successfully logged in
      404:
        description: invalid user information
      500:
        description: Internal server error
    """

    if request.method == 'POST':
        try:
            body = request.get_json()
            username = body['username']
            password = body['password']

            user = User.query.filter_by(username=username).first()

            if user == None:
                return jsonify({
                    'status': 'error',
                    'message': f'Nome de usuário: {username} não esta cadastrado, por favor, verifique as informações!'
                }), 404

            check_password = check_password_hash(user.password_hash, password)

            if check_password:
                secret_key = os.getenv('SECRET_KEY')
                auth_token = jwt.encode({'email': user.email, 'user_id': user.id}, secret_key)

                return jsonify({
                    'status': 'ok',
                    'message': 'Usuário autenticado com sucesso!',
                    'token': auth_token
                }), 200
            
            else:
                return jsonify({
                    "status": 'error',
                    'message': 'Senha incorreta!'
                }), 400

        except:
            return jsonify({
                    'status': 'error',
                    'message': 'An error has occurred!'
                }), 500
        

@user_route.route('/api/v1/get_one_user', methods=["GET"])
def get_one_user():

    """
    Get a user by username.
    ---
    parameters:
      - name: username
        in: query
        required: true
        description: The username of the user to retrieve
        schema:
          type: string
    responses:
      200:
        description: User details successfully retrieved
        content:
          application/json:
            schema:
              type: object
              properties:
                status:
                  type: string
                  example: 'ok'
                user:
                  type: object
                  properties:
                    created_at:
                      type: string
                      format: date-time
                      example: '2024-09-01T03:42:54'
                    email:
                      type: string
                      example: 'string'
                    id:
                      type: string
                      format: uuid
                      example: '36aaa52a-041f-4946-a716-d6b904a232b6'
                    name:
                      type: string
                      example: 'string'
                    updated_at:
                      type: string
                      format: date-time
                      example: '2024-09-01T03:42:54'
                    username:
                      type: string
                      example: 'string'
      400:
        description: Bad request, invalid query parameters
        content:
          application/json:
            schema:
              type: object
              properties:
                status:
                  type: string
                  example: 'error'
                message:
                  type: string
                  example: 'Invalid request'
      404:
        description: User not found
        content:
          application/json:
            schema:
              type: object
              properties:
                status:
                  type: string
                  example: 'error'
                message:
                  type: string
                  example: 'Usuário não existe!'
      500:
        description: Internal server error
        content:
          application/json:
            schema:
              type: object
              properties:
                status:
                  type: string
                  example: 'error'
                message:
                  type: string
                  example: 'An error has occurred!'
    """

    if request.method == 'GET':
        try:
            username = request.args.get('username')

            if not username:
                return jsonify({
                    'status': 'error',
                    'message': 'Username parameter is required'
                }), 400
            
            user = User.query.filter_by(username=username).first()
            user_schema = UserSchema()
            payload = user_schema.dump(user)

            if user is None:
                return jsonify({
                    'status': 'error',
                    'message': 'Usuário não existe!'
                }), 404
            
            return jsonify({
                'status': 'ok',
                'user': payload
            }), 200
    
        except Exception as e:
            return jsonify({
                'status': 'error',
                'message': 'An error has occurred!'
            }), 500


@user_route.route('/api/v1/get_users', methods=["GET"])
def get_users():

    """
    Get all users.
---
responses:
  200:
    description: List of users successfully retrieved
    content:
      application/json:
        schema:
          type: object
          properties:
            users:
              type: array
              items:
                type: object
                properties:
                  created_at:
                    type: string
                    format: date-time
                    example: '2024-09-01T03:42:54'
                  email:
                    type: string
                    example: 'string'
                  id:
                    type: string
                    format: uuid
                    example: '36aaa52a-041f-4946-a716-d6b904a232b6'
                  name:
                    type: string
                    example: 'string'
                  updated_at:
                    type: string
                    format: date-time
                    example: '2024-09-01T03:42:54'
                  username:
                    type: string
                    example: 'string'
  404:
    description: No users found
    content:
      application/json:
        schema:
          type: object
          properties:
            status:
              type: string
              example: 'error'
            message:
              type: string
              example: 'Não existe usuários cadastrados!'
  500:
    description: Internal server error
    content:
      application/json:
        schema:
          type: object
          properties:
            status:
              type: string
              example: 'error'
            message:
              type: string
              example: 'An error has occurred!'
        """

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
        

@user_route.route('/api/v1/delete_user', methods=["DELETE"])
def delete_user():

    """
    Delete a user.
---
parameters:
  - name: body
    in: body
    required: true
    description: JSON body with username and password for authentication
    schema:
      type: object
      required:
        - user_name
        - password
      properties:
        user_name:
          type: string
          description: The username of the user to delete
        password:
          type: string
          description: The password of the user to authenticate the deletion
responses:
  200:
    description: User successfully deleted or incorrect password
    content:
      application/json:
        schema:
          type: object
          properties:
            status:
              type: string
              example: 'ok'
            message:
              type: string
              example: 'Usuário deletado com sucesso!' # or 'Senha incorreta!' if password is wrong
  404:
    description: User not found
    content:
      application/json:
        schema:
          type: object
          properties:
            status:
              type: string
              example: 'error'
            message:
              type: string
              example: 'Usuário não existente!'
  500:
    description: Internal server error
    content:
      application/json:
        schema:
          type: object
          properties:
            status:
              type: string
              example: 'error'
            message:
              type: string
              example: 'An error has occurred!'

    """

    if request.method == 'DELETE':
        try:
            body = request.get_json()
            username = body['user_name']
            password = body['password']

            user = User.query.filter_by(username=username).first()

            if(user == None):
                return jsonify({
                    'status': 'error',
                    'message': 'Usuário não existente!'
                }), 404
            
            check_password = check_password_hash(user.password_hash, password)
            print(check_password)
            if(check_password):
                db.session.delete(user)
                db.session.commit()
                db.session.close()

                return jsonify({
                    'status': 'ok',
                    'message': 'Usuário deletado com sucesso!'
                }), 200
            
            else:
                return jsonify({
                    'status': 'error',
                    'message': 'Senha incorreta!'
                }), 200
            
        except Exception as error:
            print(error)
            return jsonify({
                    'status': 'error',
                    'message': 'An error has occurred!'
                }), 500
        
        
@user_route.route('/api/v1/change_user', methods=["PUT"])
def change_user():
    if(request.method == 'PUT'):
        try:
            body = request.get_json()
            user_id = body['id']
            name = body['name']
            username = body['username']
            email = body['email']
            password = body['password']
            re_password = body['re_password']

            user = User.query.filter_by(id=user_id).first()
            name_in_use = User.query.filter_by(username=username).first()

            if user == None:
                return jsonify({
                    'status': 'error',
                    'message': 'Usuário não encontrado!'
                }), 404
            
            if name_in_use != None and name_in_use.id != user.id:
                return jsonify({
                    'status': 'Conflict',
                    'message': 'Nome de usuário já esta em uso!'
                }), 409
            
            if password != re_password:
                return jsonify({
                    'status': 'error',
                    'message': 'Atenção, Senhas não coencidem!'
                })
            
            password_hash = generate_password_hash(password)
            
            user.name = name
            user.username = username
            user.email = email
            user.password_hash = password_hash

            db.session.commit()
            db.session.close()

            return jsonify({
                'status': 'ok',
                'message': 'Alteração feita com sucesso!'
            }), 200
        
        except Exception as error:
            print(error)
            return jsonify({
                    'status': 'error',
                    'message': 'An error has occurred!'
                }), 500
