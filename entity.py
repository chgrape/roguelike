
class Entity:
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self.pos = (self._x, self._y)
        self.velocity = 3
        self.health = 100
        self.sprite = 0

    def get_x(self):
        return self._x
    
    def set_x(self, x):
        self._x = x

    def get_y(self):
        return self._y
    
    def set_y(self, y):
        self._y = y

    def get_pos(self):
        return self.pos

    def set_pos(self, pos):
        self.pos = pos
        self._x = pos[0]
        self._y = pos[1]

    def get_velocity(self):
        return self.velocity

    def set_velocity(self, velocity):
        if velocity < 1:
            self.velocity = 1
        else:  
            self.velocity = velocity

    def get_health(self):
        return self.health

    def set_health(self, health):
        if health < 0:
            self.health = 0
        else:
            self.health = health
    