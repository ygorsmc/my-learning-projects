# SECRET AUCTION

print("Welcome to the secret auction!")
name_and_bid = {}
bid_values = []

is_auctioning = True
while is_auctioning:
    
    is_bidding = True
    while is_bidding:
        action = input("Are there any offer?\n").lower()

        if action == 'yes':
            name = input("What is your name?\n")
            bid = int(input("What is you bid?\n"))

            name_and_bid.update({name: bid})
            bid_values.append(bid)

        elif action == 'no':
            is_bidding = False
        else:
            print("Please type 'yes' or 'no'.")

    count_of_higher_bid = bid_values.count(max(bid_values))
    
    if count_of_higher_bid == 1:

        for n in name_and_bid:
            if max(bid_values) == name_and_bid[n]:
                winner_name = n
                winner_value = name_and_bid[n]
                is_auctioning = False

    else:
        print("It is a draw. Please, continue the auction.")
        is_auctioning = True

print(f"The winner is: {winner_name} with a bid of $ {winner_value}")
