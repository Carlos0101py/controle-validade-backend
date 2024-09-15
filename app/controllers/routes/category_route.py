from app.db_config import db
from app.models.tables.category import Category
from flask import jsonify, request, Blueprint
from app.models.schemas.category_schema import CategorySchema
from werkzeug.security import generate_password_hash, check_password_hash


category_route = Blueprint('category_route', __name__)

@category_route.route('/api/v1/create_category', methods=["POST"])
def create_category():

    """
    Create a new category.
---
tags:
  - Categories
summary: Create a new category with a specified name
description: >
  This endpoint allows you to create a new category. 
  You need to provide the `name` of the category in the request body. 
  The category name will be converted to uppercase before being stored.
parameters:
  - name: body
    in: body
    required: true
    description: JSON body with category name to create a new category
    schema:
      type: object
      required:
        - name
      properties:
        name:
          type: string
          description: The name of the category to be created
responses:
  201:
    description: Category successfully created
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
              example: Categoria criada com sucesso!
              description: Success message
  409:
    description: Category already exists
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
              example: A Categoria já existe!
              description: Error message indicating that the category already exists
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

    """
    Get all categories.
---
tags:
  - Categories
summary: Retrieve a list of all categories
description: >
  This endpoint allows you to retrieve a list of all categories.
  It returns an array of categories. If no categories are found, it will return an error.
responses:
  200:
    description: List of categories successfully retrieved
    content:
      application/json:
        schema:
          type: object
          properties:
            category:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: string
                    format: uuid
                    description: The unique identifier of the category
                  name:
                    type: string
                    description: The name of the category
          example:
            category:
              - id: "a1f8ba36-c9bd-41b1-8a2e-52786dcc07cc"
                name: "Sucos e Bebidas"
              - id: "b2f9ba36-c9bd-41b1-8a2e-52786dcc07cc"
                name: "Snacks"
  404:
    description: No categories found
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
              example: Categorias não cadastradas!
              description: Error message indicating that no categories are found
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
        

@category_route.route('/api/v1/delete_category', methods=["DELETE"])
def delete_category():

    """
    Delete a category.
---
tags:
  - Categories
summary: Delete a category by its name
description: >
  This endpoint allows you to delete a category by providing its name.
  The category name should be provided in the request body.
parameters:
  - name: body
    in: body
    required: true
    description: JSON body with the category name to delete
    schema:
      type: object
      required:
        - name
      properties:
        name:
          type: string
          description: The name of the category to be deleted
responses:
  200:
    description: Category successfully deleted
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
              example: Categoria deletada com sucesso!
              description: Success message
  400:
    description: Bad request if the name parameter is missing
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
              example: Categoria é um parâmetro requerido!
              description: Error message indicating that the category name is required
  404:
    description: Category not found
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
              example: Categoria não cadastrada!
              description: Error message indicating that the category does not exist
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
            name = body['name']

            if not name:
                return jsonify({
                    'status': 'error',
                    'message': 'Categoria é um parametro requerido!'
                }), 400
            
            category = Category.query.filter_by(name=name).first()

            if category == None:
                return jsonify({
                    'status': 'error',
                    'message': 'Categoria não cadastrada!'
                }), 404
            
            db.session.delete(category)
            db.session.commit()
            db.session.close()

            return jsonify({
                'status': 'ok',
                'message': 'Categoria deletada com sucesso!'
            }), 200
        
        except:
            return jsonify({
                    'status': 'error',
                    'message': 'An error has occurred!'
                }), 500