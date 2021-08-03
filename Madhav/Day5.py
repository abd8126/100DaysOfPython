'''PROGRAM TO CREATE A STRONG PASSWORD'''
import string
import random as ran
print("WELCOME TO PASSWORD GENERATOR:")
m=int(input("ENTER THE NO. OF PASSWORD YOU WANT: "))
u_char=string.ascii_uppercase
l_char=string.ascii_lowercase
num=string.digits
s_char=string.punctuation
for i in range(1,m+1):
    test_pass=[]
    for j in range(3):
        l1=ran.choice(u_char)
        l2=ran.choice(l_char)
        l3=ran.choice(num)
        l4=ran.choice(s_char)
        test_pass.extend([l1,l2,l3,l4])
    ran.shuffle(test_pass)
    strong_pass="".join(test_pass)
    print(f"{i}. YOUR PASSWORD : {strong_pass}")