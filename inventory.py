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
                if(self.items[x].selected == True and self.items[x].isEquipped == True):
                    pygame.draw.rect(win, (255, 0, 0), pygame.Rect(self.xPos+(66*(self.items[x].slot-1)), self.yPos, 64, 64),4)
                    pygame.draw.rect(win, (255, 255, 0), pygame.Rect(self.xPos+(66*(self.items[x].slot-1)), self.yPos, 64, 64),2)
                elif(self.items[x].selected == True):
                    pygame.draw.rect(win, (255, 0, 0), pygame.Rect(self.xPos+(66*(self.items[x].slot-1)), self.yPos, 64, 64),2)
                elif(self.items[x].isEquipped == True):
                    pygame.draw.rect(win, (255, 255, 0), pygame.Rect(self.xPos+(66*(self.items[x].slot-1)), self.yPos, 64, 64),2)
                

        else:
            self.clear_selection()

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
    
    def clear_selection(self):
        for x in range(len(self.items)):
            if(self.items[x].selected == True):
                self.items[x].selected = False

    def selected_slot(self):
        for x in range(len(self.items)):
            if(self.items[x].selected == True):
                return x+1
        return 0

    def select(self, entered_slot): 
        if(entered_slot > self.capacity or entered_slot > len(self.items) or self.items[entered_slot-1].selected == True):
            self.clear_selection()
        elif(self.selected_slot() > 0):
            self.clear_selection()
            self.items[entered_slot-1].selected = True
        else:
            self.items[entered_slot-1].selected = True

    def equip(self): 
        eq_slot = self.selected_slot()
        if(not eq_slot):
            return
        else:
            self.items[eq_slot-1].isEquipped = not self.items[eq_slot-1].isEquipped            
