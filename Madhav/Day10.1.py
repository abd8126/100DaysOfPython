def prime(lst):
    lst2=list()
    for i in lst:
        q=True
        if i==1 or i==0:
            q=False
        else:
            for j in range(2,i//2+1):
                if i%j==0:
                    q=False
        if q:
            lst2.append(i)
    return lst2
print("---TO FIND THE PRIME NUMBERS IN GIVEN LIST---")
n=list(map(int,input("ENTER THE ELEMENTS OF LIST SPACE SEPARATED:").split()))
v=prime(n)
print(f"ELEMENTS THAT ARE PRIME IN THE GIVEN LIST IS: {v}")