list = []
n = int(input("Enter number of elements : "))              # give no. of element
for i in range(0, n):
    x = input()
 
    list.append(x)                                         # adding number to the list
     
print(list)
count = 0  
  
for y in list:                                              # y is the item of list
    if len(y) > 1 and y[0] == y[-1]:  
      count += 1  
print(count) 