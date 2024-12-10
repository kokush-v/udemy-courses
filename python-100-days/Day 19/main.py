import random
from turtle import Turtle, Screen

screen = Screen()

screen.setup(width=500, height=400)
user_input = screen.textinput(title="Make a bet!", prompt="Who would win: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
turtle_position = -166

for x in range(6):
    bob = Turtle(shape='turtle')
    bob.penup()
    bob.color(colors[x])
    bob.goto(x=-220, y=-turtle_position)
    turtle_position += 66
    turtles.append(bob)

if user_input:
    race_on = True

while race_on:
    for t in turtles:
        if t.xcor() > 230:
            race_on = False
            if t.color() == user_input:
                print("You win")
            else:
                print("You lose")

        t.forward(random.randint(1, 10))





screen.exitonclick()