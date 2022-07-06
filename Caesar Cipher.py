# CAESAR CIPHER!

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def encode():
    message = input("Type your message:\n").lower()
    shift_number = int(input("Type the shift number:\n"))
    new_message = ''
    
    for letter in message:
        if alphabet.find(letter) + shift_number <= 25:
            new_message += alphabet[alphabet.find(letter) + shift_number]
        else:
            new_message += alphabet[(alphabet.find(letter) + shift_number) - 25 - 1]
    
    print(f'Encrypted message: {new_message}')
    
def decode():
    message = input("Type your message:\n").lower
    shift_number = int(input("Type the shift number:\n"))
    new_message = ''
    
    for letter in message:
        if alphabet.find(letter) - shift_number >= 0:
            new_message += alphabet[alphabet.find(letter) - shift_number]
        else:
            new_message += alphabet[(alphabet.find(letter) - shift_number) + 25 + 1]
            
    print(f'Decrypted message: {new_message}')
    
    
print("WELCOME TO CAESAR CIPHER! HERE YOUR MESSAGE WILL BE SAFE.")

is_data_valid = False

while is_data_valid == False:
    
    action = input("Type 'encode' to encrypt e 'decode' to decrypt:\n").lower()

    if action == 'encode':
        is_data_valid = True
        encode()
    elif action =='decode':
        is_data_valid = True
        decode()
    else:
        print("Please type 'encode' or 'decode'\n")
