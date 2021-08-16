'''***********SINGLE PLAYER ROCK PAPER SCISSOR GAME ***********'''
while True:
    import random as ran
    print("WELCOME TO ROCK PAPER SCISSOR GAME:")
    user=input("ENTER R or r FOR ROCK P or p FOR PAPER S or s FOR SCISSOR: ").lower()
    u=['r','p','s']
    u.remove(user)
    i=ran.choice(u)
    print(i)
    if i=='r':
        if user=='p':
            print("YOU WON...")
        else:
            print("YOU LOST...BETTER LUCK NEXT TIME")
    elif i=='p':
        if user=='s':
            print("YOU WON...")
        else:
            print("YOU LOST...BETTER LUCK NEXT TIME")
    elif i=='s':
        if user=='r':
            print("YOU WON...")
        else:
            print("YOU LOST...BETTER LUCK NEXT TIME")
    w=input("WANNA PLAY AGAIN?PRESS ENTER KEY ELSE N : ").lower()
    if w=='n':
        break