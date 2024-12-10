from turtle import Screen, Turtle
from snake import Snake, Apple
from time import sleep
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake')
screen.tracer(0)


score = ScoreBoard(x=0, y=270)
snake = Snake(screen)
apple = Apple(snake=snake)

game_on = True

while game_on:
    sleep(0.5)
    snake.move()

    if -280 < snake.head.xcor() < 280 and -280 < snake.head.ycor() < 280:
        print(len(snake.segments))
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_on = False
    else:
        game_on = False
    
    if apple.is_eaten():
        score.update_score(score=snake.score)

score.game_over()

screen.exitonclick()