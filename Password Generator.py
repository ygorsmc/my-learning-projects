# Welcome to the Ygor's Password Generator!

import random

list_of_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
list_of_letters = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z']
list_of_symbols = ['!','@','#','$','%','&','*','-','+']

trying = True

while trying:
    
    # Passwords settings

    # How many numbers

    quantity_of_letters = int(input("How many letters?"))

    # How many numbers

    quantity_of_numbers = int(input("How many numbers?"))

    # How many symbols

    quantity_of_symbols = int(input("How many symbols?"))

    # Setting the character's
    password = []


    for l in range(quantity_of_letters):
        random.shuffle(list_of_letters)
        password.append(list_of_letters[0])

    for n in range(quantity_of_numbers):
        random.shuffle(list_of_numbers)
        password.append(list_of_numbers[0])

    for s in range(quantity_of_symbols):
        random.shuffle(list_of_symbols)
        password.append(list_of_symbols[0])

    random.shuffle(password)

    final_password = ''.join(password)

    print(f"Here is you password: {final_password}")

    if input("Will you try again? (type yes or no)").lower() == 'yes':
        trying = True
    else:
        trying = False
