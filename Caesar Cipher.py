# CAESAR CIPHER!

characters = 'abcdefghijklmnopqrstuvwxyz .,:!?0123456789'

def caesar():
    
    print("WELCOME TO CAESAR CIPHER! HERE YOUR MESSAGE WILL BE SAFE.")
    
     # What action to do
    is_action_valid = False
    while is_action_valid == False:
    
        action = input("Type 'encode' to encrypt e 'decode' to decrypt:\n").lower()
        
        if action == 'encode' or action =='decode':
            is_action_valid = True
        else:
            print("Please type 'encode' or 'decode'\n")
    
    # Message to work
    message = input("Type your message:\n").lower()
    
    # Shift number
    is_number = False
    while is_number == False:
    
        shift_number = input("Type the shift number:\n")
        
        if shift_number.isdigit():
            shift_number = int(shift_number)
                  
            if shift_number % len(characters) == 0:
                print("With this number your message will not change. Please choose another number.")
            else:
                is_number = True
        else:
            print("Plase type only numbers.")
            
    new_message = ''
    
    if action == 'encode':
        for letter in message:
            new_message += characters[(characters.find(letter) + shift_number)%len(characters)]
        print(f'Encrypted message: {new_message}')

    else:
        for letter in message:
                new_message += characters[(characters.find(letter) - shift_number)%len(characters)]
        print(f'Encrypted message: {new_message}')
