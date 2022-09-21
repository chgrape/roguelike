
class Entity:
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self.pos = (self._x, self._y)

    def get_pos(self):
        return pos

    def set_pos(self, pos):
        self.pos = pos
        self._x = pos[0]
        self._y = pos[1]

    