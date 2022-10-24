import json


class Ship:
    def __init__(self, ship_id: int, x: int, y: int, size: int, health: int=0):
        self.ship_id = ship_id
        self.x = x
        self.y = y
        self.health = health if health else size
        self.size = size

    def take_hit(self):
        self.health -= 1


    # def __str__(self):
    #     return json.dumps(self.__dict__)
    #
    #
    # def __repr__(self):
    #     self.__str__()


boardx = {
    'ships': [
        {
            'x': 2,
            'y': 1,
            'size': 4,
            'direction': 'H'
         },
        {
            'x': 7,
            'y': 4,
            'size': 3,
            'direction': 'V'}
        , {'x': 3, 'y': 5, 'size': 2, 'direction': 'V'}, {'x': 6, 'y': 8, 'size': 1, 'direction': 'H'}
    ]
}
