# CALCULATOR TO SPLIT THE BILL

print("Welcome to the tip calculator. Let's split the bill fairly!")

total_bill = float(input("What was the total bill?\n"))
extra_tax = float(input("What percentage it will have to increase?"))/100
number_of_people = int(input("How many people should pay the bill?"))

splitted_bill = (total_bill + total_bill*extra_tax)/number_of_people

print(f"Each person should pay: $ {round(splitted_bill, 2)}")
