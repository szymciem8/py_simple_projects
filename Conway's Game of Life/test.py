

def neighboors(active, x, y, width, height):
    number = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            #Skip the choosen block
            if 0 <= x+i < width and 0 <= y+j < height:
                if i == 0 and j == 0:
                    pass
                elif active[x+i][y+j] == 1:
                    number += 1
                    print(str(x+i) + ", " + str(y+j) + ": " + str(active[x+i][y+j]))
                
    return number

tab = [ [1, 0, 0], 
        [1, 0, 0], 
        [1, 1, 1]]

x, y = 1, 1
width, height = 3, 3

print(neighboors(tab, 0, 1, width, height))