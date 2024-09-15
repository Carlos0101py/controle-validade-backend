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

    """
    Create a new group.
---
tags:
  - Groups
summary: Create a new group with a specified name and creator
description: >
  This endpoint allows you to create a new group. 
  You need to provide both `name` and `creator` in the request body.
parameters:
  - name: body
    in: body
    required: true
    description: JSON body with group name and creator ID
    schema:
      type: object
      required:
        - name
        - creator
      properties:
        name:
          type: string
          description: The name of the group to be created
        creator:
          type: string
          format: uuid
          description: The UUID of the user creating the group
responses:
  201:
    description: Group successfully created
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
              example: Grupo criado com sucesso!
              description: Success message
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

    """
    Add a new member to a group.
---
tags:
  - Groups
summary: Add a new member to a group by user ID and group ID
description: >
  This endpoint allows you to add a new member to a group. 
  You need to provide both `user_id` and `group_id` in the request body.
parameters:
  - name: body
    in: body
    required: true
    description: JSON body with user ID and group ID to add a new member
    schema:
      type: object
      required:
        - user_id
        - group_id
      properties:
        user_id:
          type: string
          format: uuid
          description: The UUID of the user to add as a member
        group_id:
          type: string
          format: uuid
          description: The UUID of the group to which the user will be added
responses:
  201:
    description: Member successfully added to the group
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
              example: Novo membro adicionado com sucesso!
              description: Success message
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