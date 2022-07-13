# NUMBER GUESSING GAME

print("I ma thinking of a number between 1 and 100.")

list_of_numbers = [i+1 for i in range(100)]

import random

random.shuffle(list_of_numbers)

secret_number = list_of_numbers[0]

count_of_attempts = 1

while True:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':\n").lower()
    
    if difficulty == 'easy':
        attempts = 10
        break
    elif difficulty =='hard':
        attempts = 5
        break
    else:
        print("Please. Type only 'easy' or 'hard'.")

if difficulty == 'easy':
    print("You have 10 attempts ramaining to guess the number.")
else:
    print("You have 5 attempts ramaining to guess the number.")

def make_a_guess():
    while True:

        guess = input("Make a guess:\n")

        if guess.isdigit():
            guess = int(guess)
            break
        else:
            print("Please. Type only numbers.")

    return guess
    

while count_of_attempts <= attempts:

    guess = make_a_guess()

    if secret_number == guess:
        print("YOU GUESSED RIGHT!!")
        break
    elif secret_number + 10 <= guess:
        print("You are too high.")   
    elif secret_number - 10 >= guess:
        print("You are too low.")
    elif secret_number < guess:
        print("You are a little above")
    elif secret_number > guess:
        print("You are a little below")

    print(f"You have {attempts - count_of_attempts} attempts ramaining to guess the number.")   
    count_of_attempts += 1
    
if count_of_attempts > attempts:
    print("YOU LOSE...")
    print(f"The number I was thinking is {secret_number}!")
