import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import Scoreboard

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle(x=370, y=0)
left_paddle = Paddle(x=-370, y=0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.move_up, 'w')
screen.onkey(right_paddle.move_down, 's')
screen.onkey(left_paddle.move_up, 'Up')
screen.onkey(left_paddle.move_down, 'Down')


game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if not -285 < ball.ycor() < 285:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 340:
        ball.bounce_x()

    if ball.distance(left_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    if -420 > ball.xcor():
        ball.reset_pos()
        scoreboard.r_point()

    if 420 < ball.xcor():
        ball.reset_pos()
        scoreboard.l_point()


screen.exitonclick()
