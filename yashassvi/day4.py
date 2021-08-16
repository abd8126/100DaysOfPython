import random
g=['rock','paper','scissors']#making a sequence for the system to chose from
print("It seems a Rock-Paper-Scissors Day. Let's start.")#telling the user about the game
p1=input("Choose your hand-rock, paper or scissors: ")#taking input from the user
g.remove(p1)#removing the user's choice from the available choices
p2=random.choice(g)#storing the system's choice in a variable
print("The computer chose: " + p2)#letting the user know what choice the system made
if((p1 == "rock" and p2 == "scissors") or (p1 == "paper" and p2 == "rock") or (p1 == "scissors" and p2 == "paper")):
    print("You won!")
else:
    print("The computer won. Better luck next time")