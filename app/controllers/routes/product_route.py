from app.db_config import db
from app.models.tables.product import Product
from app.models.tables.situation_product import Situation_product
from app.models.tables.status_product import Status_product
from flask import jsonify, request, Blueprint
from app.models.schemas.product_schema import ProductSchema
from app.models.schemas.situation_schema import Situation_product
from app.models.schemas.status_schema import Status_product
from werkzeug.security import generate_password_hash, check_password_hash


product_route = Blueprint('product_route', __name__)

@product_route.route('/api/v1/create_product', methods=["POST"])
def create_product():
    if request.method == 'POST':
        try:
            body = request.get_json()
            name = body['name']
            description = body['description']
            manufacture_at = body['manufacture_at']
            expiry_at = body['expiry_at']
            product_code = body['product_code']
            batch = body['batch']
            stockQuantity = body['stockQuantity']
            supplier = body['supplier']
            situation = body['situation']
            status = body['status']
            user_id = body['user_id']
            category_id = body['category_id']
            
            product = Product(name=name, description=description, manufacture_at=manufacture_at,expiry_at=expiry_at,
                            product_code=product_code, batch=batch, stockQuantity=stockQuantity,
                            supplier=supplier, category_id=category_id, user_id=user_id, situation=situation, status=status)
            
            db.session.add(product)
            db.session.commit()
            db.session.close()

            return jsonify({
                'status': 'ok',
                'message': 'Produto criado com sucesso!'
            }), 201

        except Exception as error:
            print(error)
            return jsonify({
                    'status': 'error',
                    'message': 'An error has occurred!'
                }), 500