l=[]
l1=[]
n=int(input("Enter the elements of the list\n"))
for i in range(n):
    e =input()
    l.append(e)
n=int(input("Enter the required length: "))
for i in l:
    if len(i) > n:
        l1.append(i)
print(l1)
