import requests
from requests import Response


ENDPOINT = 'http://localhost:5000/api/v1'

def create_user(payload:dict) -> Response:
    return requests.post(ENDPOINT + '/create_user',
    json=payload)

def authenticate_user(payload:dict) -> Response:
    return requests.post(ENDPOINT + '/login',
    json=payload)

def get_one_user(payload:dict) -> Response:
    return requests.get(ENDPOINT + '/get_one_user',
    json=payload)

def get_users() -> Response:
    return requests.get(ENDPOINT + '/get_users')

def delete_user(payload:dict) -> Response:
    return requests.delete(ENDPOINT + '/delete_user',
    json=payload)