def turnright():
    turn_left()
    turn_left()
    turn_left()
while  not at_goal():
        if front_is_clear():
            move()
        elif right_is_clear():
            turnright()
            move()
        else:
            turn_left()
             

        
    
        