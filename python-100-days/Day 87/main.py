import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import Scoreboard
from blocks import Blocks


def move_paddle(x, y):
    new_x = x - 800/2
    paddle.setpos(new_x, -260)


screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle(x=-20, y=-260)
ball = Ball()
scoreboard = Scoreboard()
blocks = Blocks()

screen.listen()
screen.getcanvas().bind('<Motion>', lambda event: move_paddle(event.x, event.y))

game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if not ball.ycor() < 285:
        ball.bounce_y()

    if not -385 < ball.xcor() < 385:
        ball.bounce_x()

    if ball.distance(paddle) < 70 and ball.ycor() < -240:
        print(ball.distance(paddle), ball.ycor())
        ball.bounce_y()

    blocks.check_colision(ball, scoreboard.add_point)

screen.exitonclick()
