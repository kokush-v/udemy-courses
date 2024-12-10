import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

continue_game = True

def get_req_str(player_cards_inp, computer_cards_inp):
    return f"Your cards is: {player_cards_inp} total is {sum(player_cards_inp)}\nComputer cards is {computer_cards_inp} total is {sum(computer_cards_inp)}."

def get_card(player):
    card = random.choice(cards)
    if card == 11 and sum(player) == 20:
        card = 1
    player.append(card)

def black_jack():
    player_cards = []
    computer_cards = []

    for _ in range(2):
        player_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))

    req_string = get_req_str(player_cards, [computer_cards[0]])
    print(req_string)
    get_more_cards = input("Get more cards? y/n ")

    if get_more_cards.lower() == 'y':
        get_card(player_cards)

    print(get_req_str(player_cards, computer_cards))

    if sum(player_cards) > 21:
        print("You lose!")
        return

    if sum(computer_cards) < 17:
        print("Computer has less than 17, it takes card")
        get_card(computer_cards)
        print(get_req_str(player_cards, computer_cards))

    if sum(computer_cards) > 21 or sum(computer_cards) < sum(player_cards):
        print("You win!")
    elif sum(computer_cards) > sum(player_cards):
        print("You lose!")
    elif sum(computer_cards) == sum(player_cards):
        print("Draw")


while continue_game:
    black_jack()
    new_game = input("Ready for next game? y/n ")
    if new_game.lower() == "n":
        continue_game = False
