import pandas as pd
import time

f = open("a.txt", "r")

data = pd.read_csv('a.txt', sep=" ", header=None)

f.close()

sim_time = int(data[0][0])
n_intersections = int(data[1][0])
n_street = int(data[2][0])
n_cars = int(data[3][0])
f_points = int(data[4][0])

#print(data)

mapa = {}
temp = 0
for i in range(n_street):
    mapa[data[2][i+1]] = (int(data[0][i+1]), int(data[1][i+1])), int(data[3][i+1])
    if data[0][i+1] > temp:
        temp = data[0][i+1]

intersections = []
for i in range(temp+1):
    intersections.append(0)
print(intersections)

car = []
for i in range(n_cars):
    car.append(None)
    car[i] = []
    for j in range(data[0][i+n_street+1]):
        car[i].append(data[j+1][i+n_street+1])


print(mapa)
print(car)

car_step = 0
check_l = True
for i in range(sim_time):
    if car_step < len(car[1]):
        car_intersection = mapa[car[0][car_step]][0][1]
        if check_l:
            l = mapa[car[1][car_step]][1]
            check_l = False

        #l_temp = l
        print(l)

        if l == 1: 
            car_step += 1
            check_l = True
        elif l > 1:
            l -= 1

        #print(car_intersection)

    time.sleep(1)