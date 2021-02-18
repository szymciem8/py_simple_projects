import pygame
import random
import math

def narysuj_plansze(plansza):
    #Plansza 
    for i in range(ilosc_kratek):
        pygame.draw.line(plansza, pygame.Color(0, 0, 0), [i*wielkosc_kratki, 0], [i*wielkosc_kratki, wielkosc_okna])
        pygame.draw.line(plansza, pygame.Color(0, 0, 0), [0, i*wielkosc_kratki], [wielkosc_okna, i*wielkosc_kratki])

def render_planszy(plansza, snake, wielkosc_kratki, x_jablka, y_jablka):
    plansza.fill(pygame.Color(255, 255, 255))
    narysuj_plansze(plansza)

    for i in range(len(snake)):
        x = snake[i][0]
        y = snake[i][1]
        pygame.draw.rect(plansza, pygame.Color(255, 100, 100), (x, y, wielkosc_kratki, wielkosc_kratki))

    pygame.draw.rect(plansza, pygame.Color(50, 200, 50), (x_jablka, y_jablka, wielkosc_kratki, wielkosc_kratki))

def ruch_weza(snake, kierunek):
    for i in range(len(snake)-1, 1, -1):
        snake[i] = snake[i-1]

    if snake[0][0] == x_jablka and snake[0][1] == y_jablka:
        snake.append([x_jablka, y_jablka-wielkosc_kratki])
        print("zlapany")

    if kierunek == "prawo":
        snake[0][0] += wielkosc_kratki
    elif kierunek == "lewo":
        snake[0][0] -= wielkosc_kratki
    elif kierunek == "gora":
        snake[0][1] -= wielkosc_kratki
    elif kierunek == "dol":
        snake[0][1] += wielkosc_kratki

    render_planszy(plansza, snake, wielkosc_kratki, x_jablka, y_jablka)

ilosc_kratek = 30
wielkosc_okna = 800
wielkosc_kratki = wielkosc_okna/ilosc_kratek

pygame.init()
plansza = pygame.display.set_mode((wielkosc_okna, wielkosc_okna))
plansza.fill(pygame.Color(255, 255, 255))

narysuj_plansze(plansza)

#Snake
snake = [[0, 0]]
kierunek = "prawo"

#Jablko
x_jablka = random.randint(0, ilosc_kratek-1) * wielkosc_kratki
y_jablka = random.randint(0, ilosc_kratek-1) * wielkosc_kratki
pygame.draw.rect(plansza, pygame.Color(50, 200, 50), (x_jablka, y_jablka, wielkosc_kratki, wielkosc_kratki))


fpsClock = pygame.time.Clock()
fps = 3

running = True
while running:

    ruch_weza(snake, kierunek)
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                kierunek="prawo"
            elif event.key == pygame.K_a:
                kierunek="lewo"
            elif event.key == pygame.K_w:
                kierunek="gora"
            elif event.key == pygame.K_s:
                kierunek="dol"

    fpsClock.tick(fps)
    pygame.display.update()
                