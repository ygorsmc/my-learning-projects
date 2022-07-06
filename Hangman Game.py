# WELCOME TO HANGMAN GAME!
print("WELCOME TO HANGMAN GAME!")

import random

word_list = ['cat', 'mouse', 'sheep', 'strawberry', 'honey', 'rooster']
random.shuffle(word_list)

word_game = word_list[0]
len_word = len(word_game)
letter_guess = ''
word_spaces = []
error_count = 0

one_error = ' '
two_error = ' '
three_error = ' '
four_error = "  "
five_error = " "
six_error = "  "

alive = True
free = False

def print_scaffold (error_count, one_error, two_error, three_error, four_error, five_error, six_error):
    
    if error_count == 1:
        one_error = 'O'
    elif error_count == 2:
        one_error = 'O'
        two_error = '|'
    elif error_count == 3:
        one_error = 'O'
        two_error = '|'
        three_error = '/'
    elif error_count == 4:
        one_error = 'O'
        two_error = '|'
        three_error = '/'
        four_error = "\ "
    elif error_count == 5:
        one_error = 'O'
        two_error = '|'
        three_error = '/'
        four_error = "\ "
        five_error = "/"
    elif error_count == 6:
        one_error = 'O'
        two_error = '|'
        three_error = '/'
        four_error = "\ "
        five_error = "/"
        six_error = "\ "

    print(f'''
     +-----+
     |     |
     {one_error}     |
    {five_error}{two_error}{six_error}   |
    {three_error} {four_error}   |
           |
    =========
    ''')

print_scaffold(error_count, one_error, two_error, three_error, four_error, five_error, six_error)

for l in word_game:
    word_spaces.append('_')

print(" ".join(word_spaces))



while alive and not free:
    letter_guess = input("Which letter do you choose?\n").lower()

    is_right = False
    count_position = 0
    
    for l in word_game:
        if letter_guess == l:
            is_right = True
            word_spaces[count_position] = letter_guess

        count_position += 1
        
    if is_right == False:
        error_count += 1
        
    print_scaffold(error_count, one_error, two_error, three_error, four_error, five_error, six_error)
    print(" ".join(word_spaces))
    
    if word_spaces.count('_') == 0:
        free = True
        print('YOU WIN!!!')
        
        
    if error_count == 6:
        alive = False
        print("YOU LOSE...")
        print_scaffold(error_count, one_error, two_error, three_error, four_error, five_error, six_error)
