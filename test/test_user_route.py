from helpers import *


def test_create_user():
    payload = {
        'name': 'test_name',
        'username': 'test_username',
        'email': 'test_email',
        'password': 'test_password',
        're_password': 'test_password',
    }

    create_user_response = create_user(payload)
    status = create_user_response.status_code
    assert status == 201

    delete_user_payload = {
        'user_name': payload.get('username'),
        'password': payload.get('password')
    }

    delete_user_response = delete_user(delete_user_payload)
    assert delete_user_response.status_code == 200


def test_delete_users():
    payload = {
        'name': 'test_name',
        'username': 'test_username',
        'email': 'test_email',
        'password': 'test_password',
        're_password': 'test_password',
    }

    create_user_response = create_user(payload)
    status = create_user_response.status_code
    assert status == 201

    delete_user_payload = {
        'user_name': payload.get('username'),
        'password': payload.get('password')
    }

    delete_user_response = delete_user(delete_user_payload)
    assert delete_user_response.status_code == 200

    get_one_user_payload = {
        'username': payload.get('username')
    }

    get_one_user_response = get_one_user(get_one_user_payload)
    assert get_one_user_response.status_code == 404


def test_authenticate_user():
    payload = {
        'name': 'test_name',
        'username': 'test_username',
        'email': 'test_email',
        'password': 'test_password',
        're_password': 'test_password'
    }

    create_user_response = create_user(payload)
    status = create_user_response.status_code
    assert status == 201

    authenticate_payload = {
        'username': payload.get('username'),
        'password': payload.get('password')
    }

    authenticate_user_reponse = authenticate_user(authenticate_payload)
    status = authenticate_user_reponse.status_code
    assert status == 200

    delete_user_payload = {
        'user_name': payload.get('username'),
        'password': payload.get('password')    
    }

    delete_user_response = delete_user(delete_user_payload)
    assert delete_user_response.status_code == 200


def test_get_one_user():
    payload = {
        'name': 'test_name',
        'username': 'test_username',
        'email': 'test_email',
        'password': 'test_password',
        're_password': 'test_password'
    }

    create_user_response = create_user(payload)
    status = create_user_response.status_code
    assert status == 201

    get_one_user_payload = {
        'username': payload.get('username')
    }

    get_one_user_response = get_one_user(get_one_user_payload)
    status = get_one_user_response.status_code
    assert status == 200

    user_data = get_one_user_response.json()
    assert user_data.get('user').get('email') == payload.get('email')

    delete_user_payload = {
        'user_name': payload.get('username'),
        'password': payload.get('password')
    }

    delete_user_response = delete_user(delete_user_payload)
    assert delete_user_response.status_code == 200


def test_get_users():
    get_users_response = get_users()
    assert get_users_response.status_code == 200
    users_object = get_users_response.json()
    assert str(type(users_object)) == "<class 'dict'>"
