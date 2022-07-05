while not at_goal():
    if front_is_clear():
        move()
    elif right_is_clear(): # turn three times to the left to finally turn to right.
        turn_left()
        turn_left()
        turn_left()
    elif not right_is_clear() and front_is_clear():
        move()
    else:
        turn_left()
