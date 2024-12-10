import random
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)
input("Press enter to start")

chosen_word = random.choice(word_list)
print(chosen_word)

lives = 6
placeholder = "_"
guessed_letters = [placeholder for _ in range(len(chosen_word))]

while "".join(guessed_letters) != chosen_word:

    print(f"The word is: {"".join(guessed_letters)}.")
    print(f"****************************<???>/{lives} LIVES LEFT****************************")
    print(stages[lives])

    if lives <= 0:
        break

    letter = input(f"Guess the letter.").strip().lower()

    if letter in chosen_word and letter != "":
        for index, elem in enumerate(chosen_word):
            if elem == letter:
                guessed_letters[index] = letter
        print("Correct")
    else:
        lives -= 1
        print("Wrong")

if lives <= 0:
    print("You lose")
else:
    print("You win the word was: " + chosen_word)
