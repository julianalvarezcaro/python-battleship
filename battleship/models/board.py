import json
from typing import Dict, List
from os import path

from battleship.models.ship import Ship

class Board:
    def __init__(self, ships: List=None, sunk_ships: int=0, board_matrix: List=None):
        self.ships = ships if ships else []
        self.sunk_ships = sunk_ships
        self.board_matrix = board_matrix if board_matrix else [[0 for i in range(10)] for i in range(10)]


    def add_ship(self, x, y, size, direction) -> int:
        for i in range(size):
            if self.board_matrix[y][x + i] != 0:
                return 400
            if direction == 'H':
                self.board_matrix[y][x + i] = len(self.ships) + 1
            else:
                self.board_matrix[y + i][x] = len(self.ships) + 1
        self.ships.append(Ship(len(self.ships) + 1, x, y, size))
        return 200

    def shot_fired(self, x, y) -> str:
        ret = "HIT"
        if self.board_matrix[y][x] > 0:
            self.ships[self.board_matrix[y][x] - 1].take_hit()
            if self.ships[self.board_matrix[y][x] - 1].health == 0:
                self.sunk_ships += 1
                ret = "SINK"
            self.board_matrix[y][x] = -1
        elif self.board_matrix[y][x] == 0:
            ret = "WATER"
        return ret


    def game_ended(self) -> bool:
        if len(self.ships) == self.sunk_ships:
            return True
        return False


    def game_restart(self):
        self.ships = []
        self.board_matrix = [[0 for i in range(10)] for i in range(10)]


    @classmethod
    def from_json(cls):
        with open(path.dirname(__file__) + '/../config/current_game.json', 'r') as json_file:
            json_dict = json.load(json_file)
            json_dict['ships'] = [Ship(**ship_data) for ship_data in json_dict['ships']]
        return cls(**json_dict)


    # def __str__(self):
    #     # breakpoint()
    #     my_dict =  self.__dict__.copy()
    #     # my_dict['ships'] =  json.dumps([str(ship) for ship in self.__dict__['ships']])
    #     # my_dict['ships'] = json.dumps([str(ship) for ship in self.__dict__['ships']])
    #     # return json.dumps(my_dict)
    #     return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=4)
    #
    # def __repr__(self):
    #     return self.__str__()

    # board = [
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 2, 2, 2, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 3, 3]
    # ]
