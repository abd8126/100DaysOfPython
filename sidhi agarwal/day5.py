import random
alpha="abcdefghijklmnopqrstuvwxyz"
number="0123456789"
character="~!@#$%^&*"
pas=""
pas=pas+''.join((random.choices(alpha,k=4)))
pas=pas+''.join((random.choices(character,k=4)))
pas=pas+''.join((random.choices(number,k=4)))
print("the password with 12 characters is:"+pas)
