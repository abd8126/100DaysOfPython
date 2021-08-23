import random 

pass_len = int(input("in who many digit , special character , alphabet password you want: "))
pass_data = "dcbewfveuicadcbqrgfque362187432874#%&^%$#@!&()"
password = "".join(random.sample(pass_data, pass_len))
print(password)