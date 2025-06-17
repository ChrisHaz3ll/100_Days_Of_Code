# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from art import logo
print(logo)

blind_auction = {}
another_bid = True

while another_bid:
    name = input("What is your name?: ")
    bid = input("What is your bid?: $")
    blind_auction[name] = int(bid)

    another_bidder = input("Are there any other bidders? Type 'yes', or 'no': ").lower()
    if another_bidder == "yes":
        print("\n" * 20)
    else:
        another_bid = False

    winning_bid = 0
    for key in blind_auction: #compare and assign winning bid
        if blind_auction[key] > winning_bid:
            winning_bid = blind_auction[key]

    for key in blind_auction: #find the winner
        if blind_auction[key] == winning_bid:
            winner = key
            print(f"The winning bid is {winner}, with a bid of: ${winning_bid}")


#find the maximum value:
# winner = max(blind_auction, key=blind_auction.get)
# print(winner)



