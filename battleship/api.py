import flask
import http

from battleship.controllers.delete_game import delete_game
from battleship.controllers.placement import create_game
from battleship.controllers.shots import shot_fired

app = flask.Flask(__name__)

@app.route('/battleship', methods=['POST'])
def create_battleship_game():
    # Creates the game. Payload contains the ships.
    return create_game(flask.request.get_json())

@app.route('/battleship', methods=['PUT'])
def shot():
    #  Specifies a shot against the game. The payload contains the coordinates for the shot.
    return shot_fired(flask.request.get_json())


@app.route('/battleship', methods=['DELETE'])
def delete_battleship_game():
    # Deletes the current game.
    return delete_game()
