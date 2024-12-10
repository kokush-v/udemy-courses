from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.setpos(0, -250)
        self.color("white")
        self.shape('circle')
        self.penup()
        self.x_speed = 10
        self.y_speed = 10
        self.move_speed = 0.05

    def move(self):
        new_x = self.xcor() + self.x_speed
        new_y = self.ycor() + self.y_speed
        self.goto(new_x, new_y)

    def bounce_y(self):

        self.y_speed *= -1

    def bounce_x(self):

        self.x_speed *= -1

    def reset_pos(self):
        self.home()
        self.move_speed = 0.1
        self.bounce_x()
