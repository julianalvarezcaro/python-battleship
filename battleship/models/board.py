from .ship import Ship

class Board:
    ships = []
    sunk_ships = 0
    board_matrix = [[0 for i in range(10)] for i in range(10)]

    @classmethod
    def add_ship(cls, x, y, size, direction):
        cls.ships.append(Ship(len(cls.ships) + 1, x, y, size))
        for i in range(size):
            if cls.board_matrix[y][x + i] != 0:
                return # OVERLAP ERROR
            if direction == 'H':
                cls.board_matrix[y][x + i] = len(cls.ships) + 1
            else:
                cls.board_matrix[y + i][x] = len(cls.ships) + 1

    @classmethod
    def shot_fired(cls, x, y):
        ret = "HIT"
        if cls.board_matrix[y][x] > 0:
            cls.ships[cls.board_matrix[y][x]].take_hit()
            if cls.ships[cls.board_matrix[y][x]].health == 0:
                cls.sunk_ships += 1
                ret = "SINK"
            cls.board_matrix[y][x] = -1
        elif cls.board_matrix[y][x] == 0:
            ret = "WATER"
        return ret

    @classmethod
    def game_ended(cls) -> bool:
        if len(cls.ships) == cls.sunk_ships:
            return True
        return False

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
