### 1. Write a Python function that takes a list and returns a new list with prime number elements .

def checkPrime(x):
    c=0
    for i in range(2,x//2):
        if x%i==0:
            c=1
    if c==0:
        return 1
    else:
        return 0
def isprime(p):
    ans=[]
    for i in p:
        r = checkPrime(i)
        if r == 1 and i!= 2:
            ans.append(i)
    print(ans)


l = list(map(int,input().split()))
isprime(l)


### 2. Write a Python function to check whether a number is perfect or not.

def factor(x):           
    f=[]
    for i in range(1, x):
       if x % i == 0:
           f.append(i)
    return f

n = int(input("Enter the number"))
l = factor(n)

if(n==sum(l)):
    print("Perfect Number")
else:
    print("Not a Perfect Number")



### 3. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.

l = list(map(int,input().split('-')))
l=sorted(l)
for i in range(0,len(l)-1):
    print(l[i],end='-')
print(l[len(l)-1])
        


### 4. Write a Python function to check whether the given integer is a multiple of both 5 and 7

n = int(input("Enter the number"))

if(n%5==0 and n%7==0):
    print(n," is Multipul of 5 and 7")
else:
    print(n," is not Multipul of 5 and 7")
    