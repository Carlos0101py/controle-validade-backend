from app.db_config import db
from app.models.tables.product import Product
from flask import jsonify, request, Blueprint
from app.models.schemas.product_schema import ProductSchema
from werkzeug.security import generate_password_hash, check_password_hash
from app.functions.func import datatime_to_days


product_route = Blueprint('product_route', __name__)

@product_route.route('/api/v1/create_product', methods=["POST"])
def create_product():

    """
    Create a new product.
    ---
    tags:
      - Products
    description: >
      This endpoint allows you to create a new product. 
      **Note**: A user and a category must be created beforehand to test this endpoint.
    parameters:
      - name: body
        in: body
        required: true
        description: JSON body with product details
        schema:
          type: object
          required:
            - name
            - description
            - manufacture_at
            - expiry_at
            - product_code
            - batch
            - stockQuantity
            - supplier
            - status
            - user_id
            - category_id
          properties:
            name:
              type: string
              description: The name of product
            description:
              type: string
              description: The description of product
            manufacture_at:
              type: string
              format: date-time
              description: The date of manufacture of the product
            batch:
              type: string
              description: The batch of product
            stockQuantity:
              type: number
              format: double
              description: The stock Quantity of product
            supplier:
              type: string
              description: The supplier of product
            status:
              type: string
              description: The status of product
            user_id:
              type: string
              format: uuid
              description: The product-related user id
            category_id:
              type: string
              format: uuid
              description: The product-related category id
    responses:
      201:
        description: Product successfully created
      500:
        description: Internal server error
    """

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
            status = body['status']
            user_id = body['user_id']
            category_id = body['category_id']
            
            product = Product(name=name, description=description, manufacture_at=manufacture_at,expiry_at=expiry_at,
                            product_code=product_code, batch=batch, stockQuantity=stockQuantity,
                            supplier=supplier, category_id=category_id, user_id=user_id, status=status)
            
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
        

@product_route.route('/api/v1/delete_product', methods=["DELETE"])
def delete_product():
    
    """
    Delete a product.
---
tags:
  - Products
description: >
  This endpoint allows you to delete a product by its UUID.
  You must provide a valid `product_id` in the request body.
parameters:
  - name: body
    in: body
    required: true
    description: JSON body with product ID for deletion
    schema:
      type: object
      required:
        - product_id
      properties:
        product_id:
          type: string
          format: uuid
          description: The UUID of the product to delete
responses:
  200:
    description: Product successfully deleted
    content:
      application/json:
        schema:
          type: object
          properties:
            status:
              type: string
              example: ok
              description: Operation status
            message:
              type: string
              example: Produto deletado com sucesso!
              description: Success message
  404:
    description: Product not found
    content:
      application/json:
        schema:
          type: object
          properties:
            status:
              type: string
              example: error
              description: Operation status
            message:
              type: string
              example: Produto não foi encontrado
              description: Error message
  500:
    description: Internal server error
    content:
      application/json:
        schema:
          type: object
          properties:
            status:
              type: string
              example: error
              description: Operation status
            message:
              type: string
              example: An error has occurred!
              description: Error message

    """

    if request.method == 'DELETE':
        try:
            body = request.get_json()
            product_id = body['product_id']

            product = Product.query.filter_by(id=product_id).first()

            if (product == None):
                return jsonify({
                    'status': 'error',
                    'message': 'Produto não foi encontrado'
                }), 404
            
            if(product):
                db.session.delete(product)
                db.session.commit()
                db.session.close()

                return jsonify({
                    'status': 'ok',
                    'message': 'Produto deletado com sucesso!'
                }), 200

        except Exception as error:
            print(error)
            return jsonify({
                    'status': 'error',
                    'message': 'An error has occurred!'
                }), 500


@product_route.route('/api/v1/get_all_product', methods=["GET"])
def get_all_product():
    
    """
   Get all products.
---
tags:
  - Products
responses:
  200:
    description: List of products successfully retrieved
    content:
      application/json:
        schema:
          type: object
          properties:
            product:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: string
                    format: uuid
                    description: The UUID of the product
                  name:
                    type: string
                    description: The name of the product
                  description:
                    type: string
                    description: The description of the product
                  product_code:
                    type: string
                    description: The product code
                  batch:
                    type: string
                    description: The batch of the product
                  manufacture_at:
                    type: string
                    format: date-time
                    description: The manufacture date of the product
                  expiry_at:
                    type: integer
                    description: The expiry time of the product in days
                  stockQuantity:
                    type: number
                    format: double
                    description: The stock quantity of the product
                  supplier:
                    type: string
                    description: The supplier of the product
                  created_at:
                    type: string
                    format: date-time
                    description: The creation timestamp of the product
                  updated_at:
                    type: string
                    format: date-time
                    description: The last update timestamp of the product
                  category:
                    type: object
                    properties:
                      id:
                        type: string
                        format: uuid
                        description: The UUID of the category
                      name:
                        type: string
                        description: The name of the category
                  status_product:
                    type: object
                    properties:
                      id:
                        type: string
                        format: uuid
                        description: The UUID of the status
                      name:
                        type: string
                        description: The name of the status
                  user:
                    type: object
                    properties:
                      id:
                        type: string
                        format: uuid
                        description: The UUID of the user
                      name:
                        type: string
                        description: The name of the user
                      username:
                        type: string
                        description: The username of the user
                      email:
                        type: string
                        format: email
                        description: The email of the user
                      created_at:
                        type: string
                        format: date-time
                        description: The creation timestamp of the user
                      updated_at:
                        type: string
                        format: date-time
                        description: The last update timestamp of the user
  404:
    description: No products found
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
            product = Product.query.all()
            product_schema = ProductSchema(many=True)
            payload = product_schema.dump(product)

            if not product:
                return jsonify({
                    'status': 'error',
                    'message': 'Produtos não cadastrados!'
                }), 404
            
            for item in payload:
                item['expiry_at'] = datatime_to_days(item['expiry_at'])
            
            return jsonify({
                'product': payload
            }), 200

        except Exception as error:
            print(error)
            return jsonify({
                    'status': 'error',
                    'message': 'An error has occurred!'
                }), 500