import flask
import http

from battleship.controllers.placement import create_game

app = flask.Flask(__name__)

@app.route('/battleship', methods=['POST'])
def create_battleship_game():
    # Creates the game. Payload contains the ships.
    return create_game(flask.request.get_json())

@app.route('/battleship', methods=['PUT'])
def shot():
    #  Specifies a shot against the game. The payload contains the coordinates for the shot.
    ret = Board.shot()
    if Board.game_ended():
        ret += '\n GAME ENDED'
    return flask.jsonify({ret}), http.HTTPStatus.OK


@app.route('/battleship', methods=['DELETE'])
def delete_battleship_game():
    # Deletes the current game.
    return flask.jsonify({}), http.HTTPStatus.NOT_IMPLEMENTED
