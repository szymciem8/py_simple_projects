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

        self.x_hover = 0
        self.y_hover = 0

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
        for i in range(self.n_blocks_in_y):
            self.active[i] = [0] * self.n_blocks_in_y

        #Next 2D list which describes next board of active elements
        self.next_active = [0]*self.n_blocks_in_x
        for i in range(self.n_blocks_in_y):
            self.next_active[i] = [0] * self.n_blocks_in_y

        self.changed = [0]*self.n_blocks_in_x
        #Add 1 for hovering cursor/shape
        for i in range(self.n_blocks_in_x):
            self.changed[i] = [0] * self.n_blocks_in_y

        self.clear_board(self.next_active)
        self.clear_board(self.changed)

        self.objects = [[[1]], 
                        
                        [[0, 0, 0], 
                         [1, 1, 1], 
                         [0, 0, 0]], 

                        [[1, 0, 0],
                         [0, 1, 1], 
                         [1, 1, 0]], 
                         
                        [[0, 0, 1, 1],
                         [0, 0, 1, 1],
                         [1, 1, 0, 0],
                         [1, 1, 0, 0], ],

                        [[0, 0, 0, 1, 1, 0, 0, 0],
                         [0, 1, 1, 0, 0, 1, 1, 0], 
                         [0, 0, 0, 1, 1, 0, 0, 0],
                         [1, 0, 0, 0, 0, 0, 0, 1],
                         [0, 1, 0, 0, 0, 0, 1, 0],
                         [0, 0, 0, 1, 1, 0, 0, 0],
                         [1, 1, 1, 0, 0, 1, 1, 1],
                         [1, 1, 0, 0, 0, 0, 1, 1],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 1, 1, 0, 0, 0],
                         [0, 0, 1, 0, 0, 1, 0, 0],],
                        
                          
                        [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                         [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0], 
                         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1], 
                         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1], 
                         [0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0], 
                         [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0], 
                         [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], 
                         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
                         [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
                         [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0], \
                         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]]
                        ]


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

                #'changed' list improves performance!
                if self.changed[x][y] == 1:
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
        self.clear_board(self.changed)
        for x in range(self.n_blocks_in_x):
            for y in range(self.n_blocks_in_y):
                if self.active[x][y] == 0 and self.neighboors(x, y) == 3:
                    self.next_active[x][y] = 1
                    self.changed[x][y] = 1
                elif self.active[x][y] == 1 and self.neighboors(x, y) < 2:
                    self.next_active[x][y] = 0
                    self.changed[x][y] = 1
                elif self.active[x][y] == 1 and self.neighboors(x, y) > 3:
                    self.next_active[x][y] = 0
                    self.changed[x][y] = 1
                else: 
                    self.next_active[x][y] = self.active[x][y]
                    self.changed[x][y] = 0


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

    def add_cell(self, id, x, y):
        x = math.floor(x/self.block_size)
        y = math.floor(y/self.block_size)

        for i in range(len(self.objects[id])):
                for j in range(len(self.objects[id][i])):
                    if self.objects[id][i][j] == 1:
                        self.active[x+i][y+j] = 1
                        self.changed[x+i][y+j] = 1

        self.render()

    def hover(self, id, x, y):

        new_x = math.floor(x/self.block_size)
        new_y = math.floor(y/self.block_size)

        if self.active[new_x][new_y] == 0:
            new_x *= self.block_size
            new_y *= self.block_size
            if new_x != self.x_hover: 
                self.render_hover(id, self.x_hover, self.y_hover, pygame.Color(255, 255, 255))
                self.x_hover = new_x
                self.render()
            if new_y != self.y_hover: 
                self.render_hover(id, self.x_hover, self.y_hover, pygame.Color(255, 255, 255))
                self.y_hover = new_y
                self.render()

            #ID the choosen object         
            #TODO add object rotation     
            self.render_hover(id, new_x, new_y, pygame.Color(200, 200, 200))
        
    #function that draws object either in hover mode or clear mode
    def render_hover(self, id, new_x, new_y, color):

        for i in range(len(self.objects[id])):
            for j in range(len(self.objects[id][i])):
                if self.objects[id][i][j] == 1:
                    x = new_x + 1 + i*self.block_size
                    y = new_y + 1 + j*self.block_size
                    pygame.draw.rect(self.surface, 
                                    color, 
                                    (x, y, self.block_size-1, self.block_size-1))

    def clear_hover(self, id):
        self.render_hover(id, self.x_hover, self.y_hover, pygame.Color(255, 255, 255))

    def what_changed(self):
        recs_changed = []

        #Cells on the board - dead or alive
        for x in range(self.n_blocks_in_x):
            for y in range(self.n_blocks_in_y):
                if self.changed[x][y] == 1:
                    block_x = x * self.block_size + 1
                    block_y = y * self.block_size + 1
                    recs_changed.append([block_x, block_y, self.block_size-1, self.block_size-1])

        #Cursor + shapes to be added
        recs_changed.append([self.x_hover+1, self.y_hover+1, self.block_size-1, self.block_size-1])

        return recs_changed


    #Rotation of each object that is available in the list
    def rotate_object(self, id, direction):

        tab = deepcopy(self.objects[id])
        length = len(tab)

        if length > 1:
            self.clear_hover(id)
            if direction == "right":
                for i in range(length):
                    for j in range(length):
                        self.objects[id][j][length-1-i] = tab[i][j]

            elif direction == "left":
                for i in range(length):
                    for j in range(length):
                        self.objects[id][i][j] = tab[j][length-1-i]
