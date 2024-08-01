from app.db_config import db
from app.models.tables.category import Category
from flask import jsonify, request, Blueprint
from app.models.schemas.category_schema import CategorySchema
from werkzeug.security import generate_password_hash, check_password_hash


category_route = Blueprint('category_route', __name__)

@category_route.route('/api/v1/create_category', methods=["POST"])
def create_category():
    if request.method == 'POST':
        try:
            body = request.get_json()
            name = body['name'].upper()
            has_name = Category.query.filter_by(name=name).first()
            
            if has_name == None:
                category = Category(name=name)
                db.session.add(category)
                db.session.commit()
                db.session.close()

                return jsonify({
                    'status': 'ok',
                    'message': 'Categoria criada com sucesso!'
                }), 201
            
            return jsonify({
                'status': 'error',
                'message': 'A Categoria já existe!'
            }), 409
        
        except:
            return jsonify({
                    'status': 'error',
                    'message': 'An error has occurred!'
                }), 500
        

@category_route.route('/api/v1/get_all_category', methods=["GET"])
def get_all_category():
    if request.method == 'GET':
        try:
            category = Category.query.all()
            category_schema = CategorySchema(many=True)
            payload = category_schema.dump(category)

            if not category:
                return jsonify({
                    'status': 'error',
                    'message': 'Categorias não cadastradas!'
                }), 404
            
            return jsonify({
                'category': payload
            }), 200
        
        except:
            return jsonify({
                    'status': 'error',
                    'message': 'An error has occurred!'
                }), 500