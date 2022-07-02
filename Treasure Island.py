# TREASURE ISLAND

# In this game the player must to find the treasure. And for that we need to follow the correct paths, if not, it's game over!

# 1 - Welcome to the jun... island!

print("Welcome to the game, a game to put your life on the line!!!")

gaming = True

# 2 - Direction 

direction = "right"

if gaming == True:
    
    if input("Left or right?\n").lower() != direction:
        print("GAME OVER")
        gaming = False
    else:
        print("Let's continue...")
        
# 3 - Wait for a boat or swim

boat_or_swim = "boat"

if gaming == True:
    
    if input("Will you wait for a 'boat' or will you 'swim?'\n").lower() != boat_or_swim:
        print("GAME OVER")
        gaming = False
    else:
        print("Now let's walking a litte...")
        
# 4 - Walk in daytime or nighttime

walking = 'daytime'

if gaming == True:

    if input("Will you walt during 'daytime' or during 'nighttime'\n").lower() != walking:
        print("GAME OVER")
        gaming = False
    else:
        print("We are getting close.")
        
# 5 - Which door to choose

door = 'yellow'

if gaming == True:

    if input("Will you choose which door between 'yellow', 'blue' or 'red'\n").lower() != door:
        print("GAME OVER")
        gaming = False
    else:
        print("Almost there.")
        
# 6 - Which chest to open

chest = 'middle'

if gaming == True:

    if input("Which chest will you open ('middle', 'left' or 'right')?\n").lower() != chest:
        print("GAME OVER")
        gaming = False
     
    else:
        print("You found the treasure!")
