x = int(input("Enter no of tuple group : "))
list=[]
for r in range (x):
    tup = tuple(map(int,input().split(" ")))
    list.append(tup)
print(list)
lst=len(list)
for i in range (0,lst):
    for j in range(0, lst-i-1):  
                if (list[j][-1] > list[j + 1][-1]):  
                    temp = list[j]  
                    list[j]= list[j + 1]  
                    list[j + 1]= temp 
print(list)