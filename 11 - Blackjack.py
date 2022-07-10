import random

deck_values = [2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10,11]

player_hand = []
computer_hand = []

random.shuffle(deck_values)

for card in range(2): # Player's hand
    player_hand.append(deck_values.pop()) 
print(f"Your hand: {player_hand}")

for card in range(1): # Computer's hand
    computer_hand.append(deck_values.pop())     
print(f"Computer's hand: {computer_hand}")

player_result = sum(player_hand)
computer_result = sum(computer_hand)

is_picking = True
while is_picking:

    pick_a_card = input("Type 'yes' to pick a card or 'no' to pass.\n").lower()

    if pick_a_card == 'yes':
        player_hand.append(deck_values.pop())
        print(f"Your hand: {player_hand}")
        player_result = sum(player_hand)
        if player_result > 21:
            player_result = 'BUST!'
            print(player_result)
            print("YOU LOSE...")
            is_picking = False
    elif pick_a_card == 'no':
        count = 0
        for card in deck_values:
            if card <= 21 - sum(computer_hand):
                count += 1 
        if count/len(deck_values) >= 0.5:
            computer_hand.append(deck_values.pop())
            computer_result = sum(computer_hand)
            print("The computer has picked a card.")
            if computer_result > 21:
                computer_result = "BUST!"
                print(computer_result)
                print("YOU WIN!")
                is_picking = False
        else:
            print("The Computer has stopped.")
            #print(count/len(deck_values))
            is_picking = False
    else:
        print("Please, type only 'yes' or 'no'!")
    
print(f"Your hand: {player_hand}")
print(f"Computer's hand: {computer_hand}")

if player_result != "BUST!" and computer_result != "BUST!":

    if player_result <= 21 and player_result > computer_result:
        print("YOU WIN!")
    elif computer_result > 21:
        print("YOU WIN!")
    elif computer_result > player_result:
        print("YOU LOSE...")
    else:
        print("IT'S A DRAW!")
