from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.goto(0, 0)
        self.x_move = 8
        self.y_move = 8
        self.move_speed = 0.03

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    def reset_ball(self):
        self.goto(0, 0)
        self.move_speed = 0.03
        self.x_move *= -1

    def wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.move_speed -= 0.001
        self.x_move *= -1


