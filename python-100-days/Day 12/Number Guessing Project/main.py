import random

random_number = random.randint(1, 100)
game_continue = True

def game():
    attempts = 5
    difficulty = input("Select difficulty hard (1) or easy (2).\n")
    if difficulty == '2':
        attempts = 10

    print(f"Im thinking about number between 1 and 100.\nYou have {attempts} attempts")
    for i in range(1, attempts + 1):
        guess = int(input("Make a guess: "))

        if guess == random_number:
            print("Yes, you win")
            return
        elif guess < random_number:
            print("Too low")
        else:
            print("Too high")
        print(f"{attempts - i} attempts left.")

    print(f"You lose! The number was {random_number}")

while game_continue:
    game()
    is_stop = input("Another round? y/n")
    if is_stop == 'n':
        game_continue = False

