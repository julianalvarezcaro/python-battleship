import json

from flask import jsonify
from http import HTTPStatus
from os import path
from typing import Dict

from battleship.models.board import Board
from battleship.models.ship import Ship

def create_game(payload: Dict):
    if not is_valid_payload(payload):
        return jsonify({'message': 'Please make sure to send a valid payload'}), HTTPStatus.BAD_REQUEST

    board = Board()
    for ship_data in payload.get('ships'):
        if not is_valid_ship_positioning(ship_data['x'], ship_data['y'], ship_data['size'], ship_data['direction']):
            return jsonify({'message': 'Careful! Your ships are falling off the sea!'}), HTTPStatus.BAD_REQUEST

        ret = board.add_ship(**ship_data)
        if ret == HTTPStatus.BAD_REQUEST:
            return jsonify({'message': 'Two or more of the ship are overlapping!'}), HTTPStatus.BAD_REQUEST
    with open(path.dirname(__file__) + '/../config/current_game.json', 'w+') as json_file:
        json.dump(board, fp=json_file, default=lambda o: o.__dict__)
    return jsonify({'message': 'Game started! Good luck!'}), HTTPStatus.OK


def is_valid_ship_positioning(x: int, y: int, size: int, direction: str) -> bool:
    if (direction == 'H' and x + size > 9) or (direction == 'V' and y + size > 9):
        print(f'Bad data is:\nx: {x}\ny: {y}\nsize: {size}')
        return False
    return True

def is_valid_payload(payload: Dict) -> bool:
    if not payload.get('ships'):
        return False
    for ship_data in payload.get('ships'):
        if None in [ship_data.get('x'), ship_data.get('y'), ship_data.get('size'), ship_data.get('direction')]:
            return False
    return True
