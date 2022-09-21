from entity import Entity

class Player(Entity):
    def __init__(self, x, y, name): 
        Entity.__init__(self, x, y)
        self.name = name

    def get_pos(self):
        return Entity.get_pos(self)
    
    def set_pos(self, pos):
        Entity.set_pos(self, pos)

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name