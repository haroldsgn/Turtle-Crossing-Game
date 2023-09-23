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
screen.onkeypress(player.move_up, "Up")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    car_manager.generate_cars()
    car_manager.move()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if player.distance(car) < 22:
            scoreboard.game_over()
            game_is_on = False

    # Detect if the player pass the lvl
    if player.ycor() > 280:
        car_manager.next_level()
        player.restart_position()
        scoreboard.increment_lvl()


screen.exitonclick()




