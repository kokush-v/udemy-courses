
from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.hideturtle()
        self.setpos(x, y)
        self.color('white')
        self.write(f"SCORE: 0", align='center', font=('Courier', 10, 'bold'))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align='center', font=('Courier', 20, 'bold'))
    def update_score(self, score):
        self.clear()
        self.write(f"SCORE: {score}", align='center', font=('Courier', 10, 'bold'))