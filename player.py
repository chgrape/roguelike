import pygame
from entity import Entity

class Player(Entity):
    def __init__(self, x, y, name): 
        Entity.__init__(self, x, y)
        self.name = name
        self.mana = 100
        self.sprite = pygame.image.load("Sprites/player.png")
        self.body = self.sprite.get_rect()

    def get_pos(self):
        return Entity.get_pos(self)
    
    def set_pos(self, pos):
        Entity.set_pos(self, pos)

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_velocity(self):
        return Entity.get_velocity(self)

    def set_velocity(self, velocity):
        Entity.set_velocity(self, velocity)

    def get_health(self):
        return Entity.get_health(self)

    def set_health(self, health):
        Entity.set_health(self, health)

    def get_mana(self):
        return self.mana

    def set_mana(self, mana):
        if mana < 0:
            self.mana = 0
        else:
            self.mana = mana

    def move(self): # and sprint
        pass

    def draw(self, win): # ?
        win.blit(self.sprite, self.body)
    

    