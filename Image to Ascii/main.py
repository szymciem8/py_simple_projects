import cv2
import math

ascii_table = [36, 64, 66, 37, 56, 38, 87, 77, 35, 42, 111, 97, 104, 107, 98, 100, 112, 113, 119, 109, 90, 79, 48, 81, 76, 67, 74, 85, 89, 88, 122, 99, 118, 117, 110, 120, 114, 106, 102, 116, 47, 92, 124, 40, 41, 49, 123, 125, 91, 93, 63, 45, 95, 43, 
126, 60, 62, 105, 33, 108, 73, 59, 58, 44, 34, 94, 96, 39, 46, 32]

print(ascii_table[::-1])

print(len(ascii_table))
img = cv2.imread('sasin.png', flags=0) 
cv2.imshow("original", img)
img = cv2.resize(img, (100, 50))

print(img)

thres = 255/len(ascii_table)
print(thres)

for x in range(len(img)):
    for y in range(len(img[x])):
        character = chr(ascii_table[math.floor(img[x][y] / thres) - 1])
        print(character, end="")

    print("")

cv2.waitKey()