import http

from flask import jsonify
from os import path


def delete_game():
    with open(path.dirname(__file__) + '/../config/current_game.json', 'w'):
        pass # This is just to empty the JSON file
    return jsonify({'message': 'Game ended.'}), http.HTTPStatus.OK
