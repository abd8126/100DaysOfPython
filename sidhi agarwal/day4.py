import random
while True:
    choice=["rock","paper","scissor"]
    u_choice=input("choose among rock ,paper and scissor")
    if u_choice=="rock":
        choice.remove("rock")
        c_choice=random.choice(choice)
        if c_choice=="paper":
            print("computer chose:"+c_choice+"  computer wins")
        elif c_choice=="scissor":
            print("computer chose:"+c_choice+"  you win")
    elif u_choice=="paper":
        choice.remove("paper")
        c_choice=random.choice(choice)
        if c_choice=="rock":
            print("computer chose:"+c_choice+"  you win")
        elif c_choice=="scissor":
            print("computer chose:"+c_choice+"  computer win")
    elif u_choice=="scissor":
        choice.remove("scissor")
        c_choice=random.choice(choice)
        if c_choice=="rock":
            print("computer chose:"+c_choice+"  computer wins")
        elif c_choice=="paper":
            print("computer chose:"+c_choice+"  you win")
    i=input("type yes if you want to play again and no if you don't want to play")
    if i=="no":
        break
