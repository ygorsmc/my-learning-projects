# HIGHER LOWER

import random

def make_a_list():
    list_of_entry = [("Cadbury", 200000), ("Uganda", 368000), ("Charlotte's Web", 165000), ("Tai Chi", 301000), ("The Prestige", 301000), ("2001 A Space Odyssey", 201000)]
    random.shuffle(list_of_entry)
    return list_of_entry

def play_the_game():
    
    list_of_comparisons = make_a_list()
    max_score = len(make_a_list())-1
    score = 0
    
    print("Welcome and enjoy the game!\n")
    
    is_gaming = True    
    while is_gaming:

        print(f"{list_of_comparisons[0][0]}\nhas\n{list_of_comparisons[0][1]}\naverage monthly searches\n")
        print("VS\n")
        print(f"{list_of_comparisons[1][0]}\n")

        while True:

            choice = input(f"{list_of_comparisons[1][0]} has 'higher' or 'lower' searches?\n").lower()

            if choice == "higher":
                if list_of_comparisons[1][1] >= list_of_comparisons[0][1]:
                    score += 1
                    print(f"You are right!")
                    print(f"Your score is: {score}\n")
                    break
                else:
                    print("YOU LOSE...")
                    print(f"Your final score is {score}")
                    is_gaming = False
                    break

            elif choice == "lower":
                if list_of_comparisons[1][1] <= list_of_comparisons[0][1]:
                    score += 1
                    print(f"You are right!")
                    print(f"Your score is: {score}")
                    break
                else:
                    print("YOU LOSE...")
                    print(f"Your final score is {score}\n")
                    is_gaming = False
                    break
            else:
                print("Please, type only 'higher' or 'lower'!")
            
        if score == max_score:
            print("YOU ARE AWESOME! THERE IS NOTHING YOU DO NOT KNOW!")
            break
        else:
            list_of_comparisons.pop(0)

play_the_game()

while True:
    
    ask_for_replay = input("Type 'yes' to raplay the game? or 'no' to stop.").lower()

    if ask_for_replay == "yes":
        print("It's fun right?")
        play_the_game()
    elif ask_for_replay == "no":
        print("Bye!")
        break
    else:
        print("Please, type only 'yes' or 'no'.")
