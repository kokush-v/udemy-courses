import random
from turtle import Turtle, Screen, colormode

colors = ['red', 'green', 'blue', "purple"]
angles = [90, 180, 270, 360]

bob = Turtle()
colormode(255)
bob.speed(100)
bob.shape("turtle")
bob.color("red")

def random_color():
    return  tuple([random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)])

def draw_shape(steps):
    bob.pencolor(random_color())
    bob.pensize(10)
    for _ in range(steps):
        bob.forward(50)
        bob.setheading(random.choice(angles))

def draw_circles(steps, radius):
    x = 360 / steps
    for _ in range(steps):
        bob.pencolor(random_color())
        bob.circle(radius)
        bob.left(x)


draw_circles(50, 200)

screen = Screen()
screen.exitonclick()