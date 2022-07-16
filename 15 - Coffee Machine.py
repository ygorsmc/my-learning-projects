# COFFEE MACHINE (COIN OPERATED)

menu = {"espresso": {"ingredients": {"water": 50, "coffee": 18, "milk": 0}, "price": 1.50}, "latte": {"ingredients": {"water": 200, "coffee": 24, "milk": 150}, "price": 2.50}, "cappuccino": {"ingredients": {"water": 250, "coffee": 24, "milk": 100}, "price": 3.00}}

def show_resources():
    print(f"Water: {water_storaged}ml\nMilk: {milk_storaged}ml\nCoffe: {coffee_storaged}g\nMoney: $ {money_storaged}")

def add_coin():
    
    while True:
        coin = input("Plase insert a coin. (5/10/25/50/100)\n")
        if coin.isdigit():
            coin = int(coin)/100
            break
        else:
            print("Please, insert a value coin.")
    return coin

def add_water():
    
    while True:
        amount_of_water = input("Plase insert some water.")
        if amount_of_water.isdigit():
            amount_of_water = int(amount_of_water)
            break
        else:
            print("Please, insert another value.")
    return amount_of_water

def add_milk():
    
    while True:
        amount_of_milk = input("Plase insert some milk.")
        if amount_of_milk.isdigit():
            amount_of_milk = int(amount_of_milk)
            break
        else:
            print("Please, insert another value.")
    return amount_of_milk

def add_coffe():
    
    while True:
        amount_of_coffee = input("Plase insert some coffee.")
        if amount_of_coffee.isdigit():
            amount_of_coffee = int(amount_of_coffee)
            break
        else:
            print("Please, insert another value.")
    return amount_of_coffee


machine_is_on = True

water_storaged  = 300
coffee_storaged = 100
milk_storaged  = 200
money_storaged  = 0

while machine_is_on:
        
    show_resources()
    
    while True: 
        choice = input("What you would like? (espresso/latte/cappuccino)\n").lower()
              
        if choice == "espresso" or choice == "latte" or choice == "cappuccino":
            break
        else:
            print("Please, verify your entry data.")

    def make_coffee(price = menu[choice]["price"], used_water = menu[choice]["ingredients"]["water"], used_coffee = menu[choice]["ingredients"]["coffee"], used_milk = menu[choice]["ingredients"]["milk"]):
    
        resources_is_ok = {"water": False, "coffee": False, "money": False, "milk": False}
        current_money = money_storaged
        current_water = water_storaged
        current_coffee = coffee_storaged
        current_milk = milk_storaged
        
        print(f"The {choice}'s price is $ {menu[choice]['price']}")
        refund_customer = False

        while list(resources_is_ok.values()).count(True) < len(resources_is_ok) and refund_customer == False: # Checking if all the resources will satisfy the operation
            
            if current_water < used_water:
                current_water += add_water()
                print(f"Current water: {current_water}ml")
            else:
                resources_is_ok["water"] = True
                print("Amount of water is ok.")
                
            if current_coffee < used_coffee:
                current_coffee += add_coffee()
                print(f"Current coffee: {current_coffee}g")
            else:
                resources_is_ok["coffee"] = True
                print("Amount of coffee is ok.")
                
            if current_milk < used_milk and used_milk != 0:
                current_milk += add_milk()
                print(f"Current milk: {current_milk}ml")
            else:
                resources_is_ok["milk"] = True
                if used_milk != 0:
                    print("Amount of milk is ok.")
                
            if current_money < price:
                current_money += add_coin()
                print(f"Current money: $ {current_money}")
                while current_money < price:
                    continue_adding_money = input("Add another coin? ('yes' or 'no')").lower()
                    if continue_adding_money == 'yes':
                        break
                    elif continue_adding_money == 'no':
                        print("You will be refund.")
                        refund_customer = True
                        break
                    else: 
                        print("Please, type only 'yes' or 'no'.")

            else:
                resources_is_ok["money"] = True
                print("Amount of coin is ok.")

        return current_money - price, current_water - used_water, current_coffee - used_coffee, current_milk - used_milk, refund_customer # to update the resources - money(0), water(1), coffe(2), milk (3), decision to refund(4)


    consumed_resources = make_coffee()
    money_storaged = 0
    water_storaged = consumed_resources[1]
    coffee_storaged = consumed_resources[2]
    milk_storaged = consumed_resources[3]

    if consumed_resources[4] == True:
        print("Come back again!")
    else:
        print("The coffe is ready!")
        print(f"Here is your change ${consumed_resources[0]}")
        print("Enjoy it and come back again!")
