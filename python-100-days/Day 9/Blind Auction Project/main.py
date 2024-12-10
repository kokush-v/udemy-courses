# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

bid_dict = {}

def ask_for_bid():
    name = input("What is your name?\n")
    bid = int(input("Write your bid\n"))
    bid_dict[name] = bid

def find_max_bid(compare_dict):
    max_bid_owner = max(compare_dict)
    print(f"The biggest bid have {max_bid_owner} it is ${compare_dict[max_bid_owner]}")


while True:
    ask_for_bid()

    stop = input("Do you wanna add another bid? y/n\n" ).lower()
    if stop == "n":
        find_max_bid(bid_dict)
        break