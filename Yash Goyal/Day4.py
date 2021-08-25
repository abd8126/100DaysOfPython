while True:
    import random as ran
    print("Welcome to rock paper scissor game:")
    user = input(
        "Enter R or r for rock P or p for paper S or s FOR scissor:\n").lower()
    u = ['r', 'p', 's']
    u.remove(user)
    i = ran.choice(u)
    print(i)
    if i == 'r':
        if user == 'p':
            print("HURRAH..! YOU WON")
        else:
            print("YOU LOST...BETTER LUCK NEXT TIME")
    elif i == 'p':
        if user == 's':
            print("YOU WON...")
        else:
            print("YOU LOST...BETTER LUCK NEXT TIME")
    elif i == 's':
        if user == 'r':
            print("YOU WON...")
        else:
            print("YOU LOST...BETTER LUCK NEXT TIME")
    w = input("Do you want to play again..? Press Enter Key else N:\n ").lower()
    if w == 'n':
        break
