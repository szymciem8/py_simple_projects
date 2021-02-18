import pygame
import time
import math


def render(platform_x, ball_x, ball_y):
    screen.fill(pygame.Color(255,255,255))

    pygame.draw.rect(screen, pygame.Color(255, 0, 0), (platform_x, screen_size - 50, 100, 20))


    pygame.draw.circle(screen, pygame.Color(0, 0, 255), (ball_x, ball_y), int(ball_size/2))
    pygame.display.update()


#TODO Array of Blocks


screen_size = 800

fpsClock = pygame.time.Clock()
fps = 60

pygame.init()
screen = pygame.display.set_mode((screen_size, screen_size))  
screen.fill(pygame.Color(255,255,255))

#Platform 
platform_x = 0
platform_y = screen_size - 50

#Ball
ball_size = 50
ball_x = int(screen_size/2 - ball_size/2)
ball_y = 100
speed_x = 5
speed_y = 5


#Main Loop
running = True
while running:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    platform_x, y = pygame.mouse.get_pos()

    ball_x += speed_x
    ball_y += speed_y

    if ball_x + ball_size/2 > screen_size and speed_x > 0:
        speed_x = -5
    elif ball_x - ball_size/2 < 0 and speed_x < 0:
        speed_x = 5

    if ball_y + ball_size/2 > screen_size and speed_y > 0:
        speed_y = -5
    elif ball_y - ball_size/2 < 0 and speed_y < 0:
        speed_y = 5

    if ball_y + ball_size/2 > platform_y and platform_x < ball_x < platform_x + 100:
        speed_y = -5
     

    render(platform_x, ball_x, ball_y)
    fpsClock.tick(fps)