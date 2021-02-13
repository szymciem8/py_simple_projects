import pygame
import math
import random 
from copy import deepcopy

#TODO Create known elements
#Still Lifes
#Oscillators
#Spaceships

class Net:
    
    def __init__(self, surface, n_blocks):
        self.surface = surface

        self.width = self.surface.get_width()
        self.height = self.surface.get_height()

        self.block_size = self.width/n_blocks
        self.n_blocks_in_x = n_blocks
        self.n_blocks_in_y = math.floor(self.height/self.block_size)

        #Creation of a net
        for i in range(self.n_blocks_in_x):
            pygame.draw.line(surface,
                                pygame.Color(150,150,150),
                                [i*self.block_size, 0],
                                [i*self.block_size, self.height])

        for i in range(self.n_blocks_in_y):
            pygame.draw.line(surface,
                                pygame.Color(150,150,150),
                                [0, i*self.block_size],
                                [self.width, i*self.block_size])

        #2D list where the firs index is 'x' and second is 'y'
        #List describes which part of the board is an active or alive element
        self.active = [0]*self.n_blocks_in_x
        for i in range(self.n_blocks_in_x):
            self.active[i] = [0] * self.n_blocks_in_y

        #Next 2D list which describes next board of active elements
        self.next_active = [0]*self.n_blocks_in_x
        for i in range(self.n_blocks_in_x):
            self.next_active[i] = [0] * self.n_blocks_in_y

        self.clear_board(self.next_active)


    #Create activa elements in random places
    def set_random_dots(self, number):
        for i in range(number):
            x = random.randint(0, self.n_blocks_in_x-1) 
            y = random.randint(0, self.n_blocks_in_y-1) 
            self.active[x][y] = 1

    #Render the board
    def render(self):
        for x in range(self.n_blocks_in_x):
            for y in range(self.n_blocks_in_y):
                block_x = x * self.block_size
                block_y = y * self.block_size

                #Alive cell - black color
                if self.active[x][y] == 1:
                    color = pygame.Color(0,0,0)
                #Dead cell - white color
                elif self.active[x][y] == 0:
                    color = pygame.Color(255,255,255)

                #Create actual cell
                pygame.draw.rect(self.surface, 
                                color, 
                                (block_x+1, block_y+1, self.block_size-1, self.block_size-1))

    #Description of rules of the game based od the Conway's rules
    def logic(self):
        for x in range(self.n_blocks_in_x):
            for y in range(self.n_blocks_in_y):
                if self.active[x][y] == 0 and self.neighboors(x, y) == 3:
                    self.next_active[x][y] = 1
                elif self.active[x][y] == 1 and self.neighboors(x, y) < 2:
                    self.next_active[x][y] = 0
                elif self.active[x][y] == 1 and self.neighboors(x, y) > 3:
                    self.next_active[x][y] = 0
                else: 
                    self.next_active[x][y] = self.active[x][y]


        self.active = deepcopy(self.next_active)
        self.clear_board(self.next_active)
        self.render()

    #Does not need to be used! But can be for setting each cell to 0
    def clear_board(self, tab):
        for x in range(self.n_blocks_in_x):
            for y in range(self.n_blocks_in_y):
                tab[x][y] = 0

    #Counts number of neighboors around given cell described by x an y
    def neighboors(self, x, y):
        number = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                #Skip choosen cell and handle the edges
                if 0 <= x+i < self.n_blocks_in_x and 0 <= y+j < self.n_blocks_in_y:
                    if i == 0 and j == 0:
                        pass
                    elif self.active[x+i][y+j] == 1:
                        number += 1
        return number

    def add_cell(self, x, y):
        x = math.floor(x/self.block_size)
        y = math.floor(y/self.block_size)
        print(x, y)
        self.active[x][y] = not self.active[x][y]
        self.render()

    def hover(self, element):
        #TODO
        return 0
