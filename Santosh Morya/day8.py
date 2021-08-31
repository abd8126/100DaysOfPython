h = eval(input("Enter the height of wall:"))
w = eval(input("enter the width of wall: "))

cans_require = round((h*w)/5)
if cans_require <= 1:
    print("number of can required is: ",cans_require)
else:
    print("number of cans required are: ",cans_require)