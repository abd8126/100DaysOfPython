l=[]
n=int(input("Enter the elements of the list\n"))
for i in range(n):
    e = input()
    l.append(e)
if ((int not in l) or (str not in l) or (bool not in l) or (n == 0) or (not l)):
    print("Empty list")
else:
    print("Non empty list")