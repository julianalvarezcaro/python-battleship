class Ship:
    def __init__(self, ship_id: int, x: int, y: int, size: int):
        self.ship_id = ship_id
        self.x = x
        self.y = y
        self.health = size
        self.size = size
        self.direction = str

    def take_hit(self):
        self.health -= 1
