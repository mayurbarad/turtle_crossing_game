import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)

screen.listen()
player = Player(screen)
car_manager = CarManager()
scoreboard = Scoreboard()

# screen.onkey(fun=player.go_up, key='Up')
screen.onkeypress(fun=player.start_moving,key='Up')
screen.onkeyrelease(fun=player.stop_moving, key='Up')


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.go_up()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 23:
            game_is_on = False
            scoreboard.game_over()

    # player reach finish line
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()