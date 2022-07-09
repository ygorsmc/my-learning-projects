def addition(x, y):
    result = x + y
       
    while True:
        continue_calculating = input(f"Type 'yes' to continue calculating with {result} or 'no' to start a new calculation:")        
        if continue_calculating == 'yes':
            return result
            break
        elif continue_calculating == 'no':
            print(f"{x} + {y} = {result}")
            break
        else:
            print("Please, type a correct value.") 

def subtraction(x, y):
    result = x - y
    
    while True:
        continue_calculating = input(f"Type 'yes' to continue calculating with {result} or 'no' to start a new calculation:")
        if continue_calculating == 'yes':
            return result
            break
        elif continue_calculating == 'no':
            print(f"{x} - {y} = {result}")
            break
        else:
            print("Please, type a correct value.")
            
def multiplication(x, y):
    result = x * y
    while True:
        continue_calculating = input(f"Type 'yes' to continue calculating with {result} or 'no' to start a new calculation:")
        if continue_calculating == 'yes':
            return result
            break
        elif continue_calculating == 'no':
            print(f"{x} x {y} = {result}")
            break
        else:
            print("Please, type a correct value.")
            
def division(x, y):
    result = x / y
    while True:
        continue_calculating = input(f"Type 'yes' to continue calculating with {result} or 'no' to start a new calculation:")
        if continue_calculating == 'yes':
            return result
            break
        elif continue_calculating == 'no':
            print(f"{x} / {y} = {result}")
            break
        else:
            print("Please, type a correct value.")

            
first_number = ''
second_number = ''

is_calculating = True

while is_calculating:
        
    if first_number == '': # Checking if this is a continuation of operation

        while True:
            first_number = input("Type the first number:\n")

            if first_number.isdigit():
                first_number = int(first_number)
                break
            else:
                print("Plese, type only numbers")

    print('''
    Operators:
    +
    -
    *
    /
    ''')

    while True:

        operator = input("Choose the operator:\n")

        if operator == '*' or operator == '+' or operator == '-' or operator == '/':
            break
        else:
            print('''
            Please, type one of these options:
            Operators:
            +
            -
            *
            /''')        

    while True:

        second_number = input("Type the second number:\n")

        if second_number.isdigit():
            second_number = int(second_number)
            break
        else:
            print("Plese, type only numbers")
        
    if operator == '+':
        result = addition(first_number, second_number)
        if result == None:
            is_calculating = False
        else:
            first_number = result
            
    elif operator == '-':
        result = subtraction(first_number, second_number)
        if result == None:
            is_calculating = False
        else:
            first_number = result
            
    elif operator == '*':
        result = multiplication(first_number, second_number)
        if result == None:
            is_calculating = False
        else:
            first_number = result
    else:
        result = division(first_number, second_number)
        if result == None:
            is_calculating = False
        else:
            first_number = result
