import http
import json
from flask import jsonify
from os import path
from typing import Dict

from battleship.models.board import Board

def shot_fired(payload: Dict):
    if not is_valid_shot(payload):
        return jsonify({'result': 'Both x and y should be numbers between 0 and 9'}), http.HTTPStatus.BAD_REQUEST
    board = Board.from_json()
    ret = board.shot_fired(**payload)
    if board.game_ended():
        ret += '. GAME ENDED'
    with open(path.dirname(__file__) + '/../config/current_game.json', 'w+') as json_file:
        json.dump(board, fp=json_file, default=lambda o: o.__dict__)
    return jsonify({'result': ret}), http.HTTPStatus.OK


def is_valid_shot(payload: Dict):
    x = payload['x']
    y = payload['y']
    if x > 9 or x < 0 or y > 9 or y < 0:
        return False
    return True
