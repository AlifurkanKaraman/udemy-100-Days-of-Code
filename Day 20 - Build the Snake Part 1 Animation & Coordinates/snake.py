from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.whole_snake = []
        self.create_snake()
        self.head = self.whole_snake[0]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            snake = Turtle(shape='square')
            snake.color('white')
            snake.penup()
            snake.goto(position)
            self.whole_snake.append(snake)

    def move(self):
        for snake_index in range(len(self.whole_snake) - 1, 0, -1):
            new_x = self.whole_snake[snake_index - 1].xcor()
            new_y = self.whole_snake[snake_index - 1].ycor()
            self.whole_snake[snake_index].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)