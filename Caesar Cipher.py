# CAESAR CIPHER!

characters = 'abcdefghijklmnopqrstuvwxyz .,:!?0123456789'

def caesar():
    
    print("WELCOME TO CAESAR CIPHER! HERE YOUR MESSAGE WILL BE SAFE.")

    is_action_valid = False

    while is_action_valid == False:
    
        action = input("Type 'encode' to encrypt e 'decode' to decrypt:\n").lower()
        
        if action == 'encode' or action =='decode':
            is_action_valid = True
        else:
            print("Please type 'encode' or 'decode'\n")
                  
    message = input("Type your message:\n").lower()
    shift_number = int(input("Type the shift number:\n"))
    new_message = ''
    
    if action == 'encode':
        for letter in message:
            new_message += characters[(characters.find(letter) + shift_number)%len(characters)]
        print(f'Encrypted message: {new_message}')
    else:
        for letter in message:
                new_message += characters[(characters.find(letter) - shift_number)%len(characters)]
        print(f'Encrypted message: {new_message}')
