
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.setpos(350, 230)
        self.write(self.score, align="center", font=('Arial', 40, "normal"))

    def add_point(self):
        self.score += 1
        self.update_score()
