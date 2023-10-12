from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
print("Welcome to the secret auction program!")

auction_dict = {}

def secret_auction_program(name, bid):
    auction_dict[name] = bid


end_of_auction = False
while not end_of_auction:
    name = input("What is your name?: ")
    bid = input("What is your bid?: $")
    secret_auction_program(name, bid)
    result = input("Are there any other bidders? Type 'yes' or 'no'.")
    if result == "no":
        end_of_auction = True
    clear()

max = 0
for bidder in auction_dict:
    if int(auction_dict[bidder]) > int(max):
        max = auction_dict[bidder]
        winner = bidder
print(f"The winner is {winner} with a bid of ${max}")
