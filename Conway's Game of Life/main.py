import net
import pygame
import time

screen_size = 800

fpsClock = pygame.time.Clock()
fps = 30

pygame.init()
pygame.display.set_caption("Conway's Game Of Life")
screen = pygame.display.set_mode((screen_size, screen_size))  
screen.fill(pygame.Color(255,255,255))
pygame.display.update()

board = net.Net(screen, 100)
#board.set_random_dots(1500)

#Main Loop
running = True
life = False
while running:  
    #board.game_logic()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            life = not life
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not life:
                x, y = pygame.mouse.get_pos()
                board.add_cell(x, y)
    
    if life:
        board.logic()

    pygame.display.update()
    fpsClock.tick(fps)