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

        guess_function = input("Make a guess:\n")

        if guess_function.isdigit():
            guess_function = int(guess_function)
        else:
            print("Please. Type only numbers.")
    return guess_function
    
guess = make_a_guess()

while count_of_attempts < attempts:
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
         
    count_of_attempts += 1
    guess = make_a_guess()
    
if count_of_attempts == attempts:
    print("YOU LOSE...")
    
print(f"The number I was thinking is {secret_number}!")
