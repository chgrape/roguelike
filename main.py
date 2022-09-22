import pygame
from player import Player
from inventory import Inventory

win_width = 1000
win_height = 1000

win = pygame.display.set_mode((win_height, win_width))
pygame.display.set_caption("Game")

def redrawWindow(win, player, inventory):
    win.fill((0,255,0))
    player.draw(win)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    player = Player(100,100,"jivko")
    inventory = Inventory(5, win_height, win_width)
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
                        inventory.toggle(win)
                        print(inventory.isOpen)
                
        redrawWindow(win, player, inventory)

main()