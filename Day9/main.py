from replit import clear
from art import logo

print(logo)
bids = {}

def max_of_bid(bidders):
    highest_bid_amount = 0
    for bidder in bidders:
        bid_amount = bidders[bidder]
        if highest_bid_amount < bid_amount:
            highest_bid_amount = bid_amount
            winner = bidder
    
    print(f"The winner is {winner} with a bid of ${highest_bid_amount}")

is_finish = True
while is_finish:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid

    decision = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    #Chech if user wrote correct word
    while True:
        if decision == 'no' or decision == 'yes':
            break
        print("Invalid word. Please try again: ")
        decision = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if decision == 'no':
        is_finish = False
        max_of_bid(bids)
    elif decision == "yes":
        clear()
    