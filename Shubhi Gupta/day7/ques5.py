u_list = []
n = int(input("Enter number of elements : "))              # give no. of element
for i in range(0, n):
    x = int(input())
 
    u_list.append(x)                                         # adding number to the list
     
print(u_list)
f_list = []                                                   #empty list
for num in u_list:
    if num not in f_list:
        f_list.append(num)
print(f_list)
