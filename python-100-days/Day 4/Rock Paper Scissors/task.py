import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

elem_list = [rock, paper, scissors]
person_choice = elem_list[int(input("What do you choose? 0 - rock / 1 - paper / 2 - scissors\n"))]
computer_choice = random.choice(elem_list)

print(f"You choose\n{person_choice}")
print(f"Computer choose\n{computer_choice}")

if (person_choice is scissors and computer_choice is paper) or (person_choice is paper and computer_choice is rock) or (person_choice is rock and computer_choice is scissors):
    print("You win")
elif person_choice == computer_choice:
    print("Draw")
else:
    print("You lose")


