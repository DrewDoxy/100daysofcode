import os
from auction_art import logo

def clear():
    print("\n" * 10)

bids = {}

print(logo)


def find_highest_bidder(bidding_record):
    for bidder in bidding_record:
        highest_bid = 0
        winner = ""
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"{winner} has the highest bid and is the winner! They won with a bid of ${highest_bid}")

auction_live = True

while auction_live:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    choice = input("Are there any other bidders? Yes or no: ").lower()
    if choice == "yes":
        clear()
    else:
        auction_live = False
        find_highest_bidder(bids)






