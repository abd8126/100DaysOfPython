def turn_right():           #function defined
    turn_left()
    turn_left()
    turn_left()             #they are because to face the goal
while not at_goal():    
    if right_is_clear():    # loop for the movement to the goal direction
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        