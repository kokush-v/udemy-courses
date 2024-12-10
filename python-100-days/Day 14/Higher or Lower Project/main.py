import random

from game_data import data

score = 0

def game():
    global score

    random_candidates = []

    for i in range(2):
        candidate = random.choice(data)
        while candidate in random_candidates:
            candidate = random.choice(data)
        random_candidates.append(candidate)

    def compare_candidates(choice):
        if choice == 2:
            random_candidates.reverse()

        return random_candidates[0]["follower_count"] > random_candidates[1]["follower_count"]

    choice = int(input(f"Who has more subscribers in instagram?\n"+ "or".join([f'\n{index + 1}) {value["name"]} the {value["description"]} from {value["country"]}\n' for index, value in enumerate(random_candidates)])))

    if compare_candidates(choice):
        print("Yes, its correct")
        score += 1
        game()
    else:
        print("No its wrong")
        print(f"Your score is {score}")


game()