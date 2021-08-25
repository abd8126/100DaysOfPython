import math
h=float(input("Enter the height of the wall in metres: "))
w=float(input("Enter the width of wall in metres: ")) #taking dimensions
c= math.ceil((h*w)/5) #no of cans required
print("Area of the wall = ", round(h*w,2))
print("Number of cans required= ", c)