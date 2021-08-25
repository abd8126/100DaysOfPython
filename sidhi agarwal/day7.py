l=[]
n=int(input("enter the number of elements in the list"))
for i in range(n):
    l.append(int(input()))
l.sort()
print(l[-1]) # 1.maximum
print(l[0]) # 2.minimum
#3.
l1=['abc','xyz','aba','1221']
c=0
for i in l1:
    if len(i)>1 and i[0]==i[-1]:
        c+=1
print(c)
#4.
list1=[(2,5),(1,2),(4,4),(2,3),(2,1)]
length=len(list1)
for i in range (0,length):
    for j in range(0, length-i-1):  
                if (list1[j][-1] > list1[j + 1][-1]):  
                    t = list1[j]  
                    list1[j]= list1[j + 1]  
                    list1[j + 1]= t 
print(list1)

#5.
l2=[]
for i in l:
    if i in l2:
        pass
    else:
        l2.append(i)
print(l2)
#6.
l3=[]
if len(l3)==0:
    print("empty")
#7.copy a list
l4=l.copy()
print(l4)
#8.
list=[]
length_of_list=int(input("enter the length of list of words"))
for i in range(length_of_list):
    word=input()
    list.append(word)
n=int(input("enter the length"))
for i in list:
    if len(i)>n:
        print(i)


