h=int(input("Enter the height of wall in meter:- "))
w=int(input("Enter the width of wall in meter:- "))
area= h*w
y= area/5                    # 1 can cover 5sq meter
x= round(y)
# we want everytime can should be sufficent to colour
if(y>x):
    print(x+1)               
else:
    print(x)
