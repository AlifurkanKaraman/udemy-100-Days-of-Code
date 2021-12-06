from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 20:
        food.refresh()
        if score_board.score > 4 and score_board.score % 5 == 0:
            food.add_big_food()
            snake.double_extend()
        else:
            snake.extend()
        score_board.increase_score()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -280:
        score_board.reset()
        snake.reset()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score_board.reset()
            snake.reset()

screen.exitonclick()