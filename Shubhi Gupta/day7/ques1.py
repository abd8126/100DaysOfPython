list = []
n = int(input("Enter number of elements : "))              # give no. of element
for i in range(0, n):
    x = int(input())
 
    list.append(x)                                         # adding number to the list
     
print(list)
print("Maximun number of list is:-",max(list))
