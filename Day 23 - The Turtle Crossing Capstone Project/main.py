import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()
    scoreboard.update_scoreboard()

    # Checks if turtle cross the finish line.
    # If true, then turtle goes to starting position and level is up.
    if player.ycor() >= 280:
        player.next_level()
        scoreboard.increase_score()
        car_manager.update_speed()

    # Checks if turtle collide with cars.
    # If true, then the game is over.
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
