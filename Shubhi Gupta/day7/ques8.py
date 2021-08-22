list = []
n = int(input("Enter number of elements : "))              # give no. of element
for i in range(0, n):
    x = input()
 
    list.append(x)                                         # adding number to the list
     
print(list)
i=int(input("Enter the length for the word from above that u want word from list"))
for x in list:
    y=len(x) 
    if(i<=y):
        print(x)
    else:
        print("Non word's length is greater than ",i)
        break