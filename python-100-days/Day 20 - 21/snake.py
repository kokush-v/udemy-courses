import random
from turtle import Turtle, Screen

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self, screen):
        self.segments = []
        self.score = 0

        self.screen = screen
        screen.listen()
        screen.onkey(key="a", fun=self.move_left)
        screen.onkey(key="d", fun=self.move_right)
        screen.onkey(key="w", fun=self.move_up)
        screen.onkey(key="s", fun=self.move_down)

        for x in range(3):
            new_turtle = Turtle('square')
            new_turtle.width(20)
            new_turtle.penup()
            new_turtle.color('white')
            if len(self.segments) > 0:
                new_turtle.setpos(x=self.segments[x - 1].xcor() - 20, y=self.segments[x - 1].ycor())
            self.segments.append(new_turtle)

        self.head = self.segments[0]

    def move(self):
        for index in range(len(self.segments) - 1, 0, -1):
            self.segments[index].goto(self.segments[index - 1].xcor(), self.segments[index - 1].ycor())
        self.head.forward(20)

        self.screen.update()

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def add_score(self):
        self.score += 1
        new_turtle = Turtle('square')
        new_turtle.width(20)
        new_turtle.penup()
        new_turtle.color('white')
        self.segments.append(new_turtle)

class Apple(Turtle):
    def __init__(self, snake):
        super().__init__()
        self.shape('turtle')
        self.snake = snake
        self.width(20)
        self.setpos(random.randint(-250, 250), random.randint(-250, 250))
        self.color('white')
        self.penup()

    def is_eaten(self):
        is_collided = abs(self.xcor() - self.snake.segments[0].xcor()) < 20 and abs(self.ycor() - self.snake.segments[0].ycor()) < 20
        if is_collided:
            self.snake.add_score()
            self.replace()
        return is_collided

    def replace(self):
        self.setpos(random.randint(-250, 250), random.randint(-250, 250))

