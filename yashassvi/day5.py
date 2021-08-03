import random
c_l=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
c_u=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
sym=['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']
y=[]
password=[]
c1=random.choice(c_l)
c_l.remove(c1)
c2=random.choice(c_u)
c_u.remove(c2)
c3=random.choice(c_l)
c_l.remove(c3)
c4=random.choice(c_u)
c_u.remove(c4)
com=c_l+c_u+sym
random.shuffle(com)
for i in range(0,8):
    y.append(com[i])
y_n=''.join([str(x) for x in y])
password.append(c1)
password.append(c2)
password.append(c3)
password.append(c4)
password.append(y_n)
f_pass=''.join([str(x) for x in password])
print("Your passord could be: " + f_pass)
