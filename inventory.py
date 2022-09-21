class Inventory:
    def __init__(self, capacity, xPos, yPos, width, height):
        self.capacity = capacity
        self.items = []
        self.isOpen = False
        self.xPos = width/3
        self.yPost = height/4
        self.selected = 0

    def toggle(self):
        self.isOpen = not self.isOpen
        if(isOpen):
            #Display function
            continue

    def add_item(self, item):
        self.items.append(item)
        #Display function

    def remove_item(self, item_id):
        self.items.pop(item_id)
        #Display function

    def toggle_equip(self, Player, space_id):
        self.items[space_id].isEquipped = not self.items[space_id].isEquipped
        if(not self.items[space_id].isEquipped):
            #highlights item and changes player stats
            continue
        else:
            #removes highlight and reverts stat changes
            continue
        continue
