import pygame

class Item:
    def __init__(self, name, sprite, isEquipped):
        self.name = name
        self.sprite = pygame.image.load(sprite)
        self.isEquipped = isEquipped
        self.slot = 0

class Weapon(Item):
    def __init__(self, name, sprite, isEquipped, atk):
        Item.__init__(self, name, sprite, isEquipped)
        self.atk = atk

    
