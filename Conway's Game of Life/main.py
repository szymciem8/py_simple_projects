import net
import pygame
import time

screen_size = 800

fpsClock = pygame.time.Clock()
fps = 60

pygame.init()
pygame.display.set_caption("Conway's Game Of Life")
screen = pygame.display.set_mode((screen_size, screen_size))  
screen.fill(pygame.Color(255,255,255))
pygame.display.update()

board = net.Net(screen, 100)
board.set_random_dots(5000)

last_x = 0
last_y = 0

pygame.display.update()
board.logic()

#Main Loop
running = True
life = False
while running:  
    #board.game_logic()
    x, y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            life = not life
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not life:
                board.add_cell(x, y)
    
    if life:
        rects = board.what_changed()
        pygame.display.update(rects)
        board.logic()
        fpsClock.tick(fps)
    elif not life:
        if last_x != x or last_y != x:
            board.hover(x, y)
            last_x = x
            last_y = y
            pygame.display.update()