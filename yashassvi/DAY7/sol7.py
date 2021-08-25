l=[]
l1=[]
n=int(input("Enter the elements of the list\n"))
for i in range(n):
    e = input()
    l.append(e)
for i in l:
    if i in l:
        l1.append(i)
print("Old List:", l)
print("New List:", l1)