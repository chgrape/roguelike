import pygame

class Inventory:
    def __init__(self, capacity, width, height):
        self.capacity = capacity
        self.items = []
        self.isOpen = False
        self.xPos = width/3
        self.yPos = height/4
        self.selected = 0
        self.color = (10, 10, 10)

    def toggle(self, win):
        self.isOpen = not self.isOpen
        if (self.isOpen):
            for x in range(self.capacity):
                pygame.draw.rect(win, self.color, pygame.Rect(15, 15, self.xPos+(15*x), self.yPos))

    def add_item(self, item):
        self.items.append(item)
        # Display function

    def remove_item(self, item_id):
        self.items.pop(item_id)
        # Display function

    def toggle_equip(self, Player, space_id):
        self.items[space_id].isEquipped = not self.items[space_id].isEquipped
        if (not self.items[space_id].isEquipped):
            # highlights item and changes player stats
            pass
        else:
            # removes highlight and reverts stat changes
            pass
        pass
