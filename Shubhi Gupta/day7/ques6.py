list = []
n = int(input("Enter number of elements : "))              # give no. of element
for i in range(0, n):
    x = int(input())
 
    list.append(x)                                         # adding number to the list
# to check wheather list is empty or not
if(n==0):
    print("Empty list")
else:
    print("Non-Empty list")

