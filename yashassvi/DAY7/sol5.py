l=[]
l1=[]
n=int(input("Enter the elements of the list\n"))
for i in range(n):
    e = input()
    l.append(e)
print("Old List:" , l)
for i in l:
    if i not in l1:
        l1.append(i)
print("New List:" , l1)

