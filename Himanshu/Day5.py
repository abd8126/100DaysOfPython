import random
L = ['0','1','2','3','4','5','6','7','8','9']
C = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
C1 = [i.upper() for i in C]
S = ['~','!','@','#','$','%','^','&','*','?','/','_','(',')',':',',','+','-']

n=int(input("Enter the length of the password : "))
if n<4:
    print("The length must be greater than 4\n Please try again")
else:
    password = random.choice(C)+ random.choice(L) + random.choice(C1).upper()+ random.choice(S)
    for i in range(n-4):
        password=password + random.choice(L+C+C1+S)

    print("Your password is:  ",password)