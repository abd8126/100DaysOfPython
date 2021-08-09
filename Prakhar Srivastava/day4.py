#ROCK PAPER SCISSSORS GAME 
a=input()
b=input()
ai=input()
bi=input()
if (ai=="Rock" and bi=="Scissor")or(ai=="Paper" and bi=="Rock")or(ai=="Scissor" and bi=="Paper"):
    print(a,"Win")
elif (bi=="Rock" and ai=="Scissor")or(bi=="Paper" and ai=="Rock")or(bi=="Scissor" and ai=="Paper"):
    print(b,"Win")
else:
    pass