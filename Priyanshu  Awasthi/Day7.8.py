str=input("enter strings : ")

a=str.split(" ")

b=[]

n=int(input("enter value of n "))

for i in a:

    if (len(i)> n) :

        b.append(i)

print("list of words : ",b)