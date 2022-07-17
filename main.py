from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_is_on = True

while machine_is_on:

    add_money = MoneyMachine()
    coffee = CoffeeMaker()
    menu = Menu()

    while True:


        user_choice = input(f"What will you choose? {menu.get_items()}\n").lower()

        if user_choice == 'latte' or user_choice == 'espresso' or user_choice == 'cappuccino':

            choice = menu.find_drink(user_choice)

            if coffee.is_resource_sufficient(choice):
                print(f"The cost for this coffee is: ${choice.cost}")
                print("Please, insert the necessary coins.")
                if add_money.make_payment(choice.cost):
                    coffee.make_coffee(choice)
                else:
                    print("Please, come back with the necessary coins. The coffees of here are delicious!!!")

        elif user_choice == 'report':
            coffee.report()
            add_money.report()

        elif user_choice == 'off':
            print("Turning off the machine...")
            machine_is_on = False
            break

        else:
            print("Please, enter with one of the options.")





