from re import S
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

    def draw(self, win):
        if (self.isOpen):
            for x in range(self.capacity):
                pygame.draw.rect(win, self.color, pygame.Rect(self.xPos+(66*x),self.yPos, 64, 64))
            for x in range(len(self.items)):
                win.blit(self.items[x].sprite, (self.xPos+(66*x),self.yPos))

    def order_slots(self):
        for x in range(len(self.items)):
            self.items[x].slot = x+1

    def add_item(self, item):
        if(len(self.items) +1 < self.capacity):
            self.items.append(item)
            self.order_slots()

    def remove_item(self, item_slot):
        for x in self.items:
            if(x.slot == item_slot):
                self.items.pop(x.slot-1)
                self.order_slots()
                return
        print("Item doesn't exist")

    
    def toggle_equip(self, Player, space_id):
        self.items[space_id].isEquipped = not self.items[space_id].isEquipped
        if (not self.items[space_id].isEquipped):
            # highlights item and changes player stats
            pass
        else:
            # removes highlight and reverts stat changes
            pass
        pass
