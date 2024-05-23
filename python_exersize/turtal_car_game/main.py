import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboad import Scoreboad

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboad = Scoreboad()

screen.listen()
screen.onkey(player.go_up, "Up")


game_is_on = True
while game_is_on :
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()

    #detect with collision
    for car in car_manager.all_car:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboad.game_over()

    #detect succesfull crossing
    if player.is_at_finish_line():
        player.go_to_start()
        scoreboad.increase_level()

screen.exitonclick()