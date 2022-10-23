from typing import Dict

from battleship.models.board import Board
from battleship.models.ship import Ship

def create_game(payload: Dict):
    ships = []
    for ship_data in payload.get('ships'):
        if not is_valid_ship_positioning(payload.get('x'), payload.get('y'), payload.get('size')):
            return 'Careful! Your ships are falling off the sea!', 400
        Board.add_ship(**ship_data)


def is_valid_ship_positioning(x: int, y: int, size: int) -> bool:
    if x + size > 9 or y + size > 9:
        return False
    return True
