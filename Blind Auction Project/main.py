# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
#--------------------FUNCTION------------------------
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f'O vencedor dessa porra é {winner} com a porra de um lance de ${highest_bid}')
#----------------------------------------------------
bids = {}
continue_bidding = True
while continue_bidding:
    name = input("Your Name: ")
    price = int(input("Your Bid: $"))
    bids[name] = price
    ask_continue = input("Wanna continue? y/n: ").lower()
    if ask_continue == 'n':
        continue_bidding = False
        find_highest_bidder(bids)
    elif ask_continue == 'y':
        print('\n' * 20)


# TODO-4: Compare bids in dictionary


