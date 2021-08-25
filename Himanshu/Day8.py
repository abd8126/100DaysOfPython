H = eval(input("Enter the height of wall"))
B = eval(input("Enter the width of wall"))

n = (H*B)/5
print(round(n)," can" if(round(n) == 1) else " cans")