import math
def paint(height, width, cover):
    area = height*width
    cans = area/cover
    print(math.ceil(cans))
h = int(input("Height of wall: "))
w = int(input("Width of wall: "))
coverage = 5
paint(height=h, width=w, cover=coverage)
