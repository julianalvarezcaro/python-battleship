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
