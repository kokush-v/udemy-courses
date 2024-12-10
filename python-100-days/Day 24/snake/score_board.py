
from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.hideturtle()
        self.setpos(x, y)
        self.score = 0
        with open('score.txt') as file:
            self.best_score = int(file.read())
        self.color('white')
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"SCORE: {self.score} BEST SCORE: {self.best_score}", align='center', font=('Courier', 10, 'bold'))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_best_score(self):
        if self.best_score < self.score:
            self.best_score = self.score
            with open('score.txt', mode='w') as file:
                file.write(str(self.best_score))
        self.score = 0
        self.update_score()