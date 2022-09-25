import pygame
from player import Player
from inventory import Inventory
from item import Weapon

win_width = 1000
win_height = 1000

win = pygame.display.set_mode((win_height, win_width))
pygame.display.set_caption("Game")

def redrawWindow(win, player, inventory):
    win.fill((0,255,0))
    player.draw(win)
    inventory.draw(win)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    player = Player(100,100,"jivko")
    inventory = Inventory(5, win_height, win_width)
    weapon1 = Weapon("Sword", "Sprites/sword1.png", False, 2)
    weapon2 = Weapon("Sword2", "Sprites/bow1.png", False, 2)
    inventory.add_item(weapon1)
    inventory.add_item(weapon2)
    run = True

    while run:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        player.set_y(player.get_y() + player.get_velocity())
                        player.set_pos((player.get_x(), player.get_y()))
                    if event.key == pygame.K_UP:
                        player.set_y(player.get_y() - player.get_velocity())
                        player.set_pos((player.get_x(), player.get_y()))
                    if event.key == pygame.K_RIGHT:
                        player.set_x(player.get_x() + player.get_velocity())
                        player.set_pos((player.get_x(), player.get_y()))
                    if event.key == pygame.K_LEFT:
                        player.set_x(player.get_x() - player.get_velocity())
                        player.set_pos((player.get_x(), player.get_y()))
                    if event.key == pygame.K_SPACE:
                        inventory.isOpen = not inventory.isOpen
                    if event.key == pygame.K_q:
                        if(inventory.isOpen):
                            inventory.remove_item(1)
                    if event.key == pygame.K_1:
                        inventory.select(1)
                    if event.key == pygame.K_2:
                        inventory.select(2)
                    if event.key == pygame.K_3:
                        inventory.select(3)
                    if event.key == pygame.K_4:
                        inventory.select(4)
                    if event.key == pygame.K_5:
                        inventory.select(5)
        redrawWindow(win, player, inventory)

main()