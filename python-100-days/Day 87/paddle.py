from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.setpos(x, y)
        self.shape("square")
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len=7)
        self.penup()
