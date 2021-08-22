list = []
n = int(input("Enter number of elements : "))              # give no. of element
for i in range(0, n):
    x = int(input())
 
    list.append(x)                                          # adding number to the list
print("list given by user:-",list)                                 
# for cloning or copying list
list1=[]                                                     #empty list declared 
list1 = list[:]                                             #using slice operator to copy
print("Original list is:-",list)
print("Copied list is:-",list1)
