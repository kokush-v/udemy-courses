FONT = ("Courier", 24, "normal")

from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.hideturtle()
        self.setpos(x, y)
        self.color('black')
        self.score = 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align='center', font=FONT)

    def update_score(self):
        self.clear()
        self.write(f"LEVEL: {self.score}", align='center', font=('Courier', 10, 'bold'))

    def increase_score(self):
        self.score += 1
        self.update_score()