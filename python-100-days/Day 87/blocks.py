from turtle import Turtle
from ball import Ball


class Block(Turtle):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.shape("square")
        self.color('red')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.setpos(x, y)
        self.block_width = (self.shapesize()[0] * 20)
        self.block_heigh = (self.shapesize()[1] * 20)

    def is_touched(self, ball: Ball):
        block_left = self.xcor() - self.block_width / 2
        block_right = self.xcor() + self.block_width / 2
        block_top = self.ycor() + self.block_heigh / 2
        block_bottom = self.ycor() - self.block_heigh / 2

        ball_x = ball.xcor()
        ball_y = ball.ycor()
        ball_radius = 10

        if (block_left - ball_radius <= ball_x <= block_right + ball_radius) and (block_bottom - ball_radius <= ball_y <= block_top + ball_radius):
            if ball_y > block_top or ball_y < block_bottom:
                ball.bounce_y()
                self.hideturtle()
                return True
            elif ball_x > block_right or ball_x < block_left:
                ball.bounce_x()
                self.hideturtle()
                return True
        return False


class Blocks():
    def __init__(self):
        self.blocks: list[Block] = []
        for row in range(5):
            for col in range(10):
                block = Block()
                x = -250 + col * ((block.shapesize()[1] * 20) + 20)
                y = 200 - row * ((block.shapesize()[0] * 20) + 20)
                block.setpos(x, y)
                self.blocks.append(block)

    def check_colision(self, ball: Ball, add_score):
        for block in self.blocks:
            if block.is_touched(ball):
                add_score()
                self.blocks.remove(block)
