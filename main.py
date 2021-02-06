from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
car_manager.generate_car()

screen.listen()
screen.onkey(key="Up", fun=player.move_forward)
screen.onkey(key="Down", fun=player.move_backward)


while player.alive:
    time.sleep(0.1)
    screen.update()

    car_manager.generate_car()
    car_manager.move_cars(player)

    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.update_level()
        car_manager.go_faster()

scoreboard.game_over()




screen.exitonclick()

# Add listen and onkey method to move turtle north
# Detect when turtle player collides with a car and trigger game over
# Detect when turtle has reached the top edge of the screen(FINISH_LINE_Y), return turtle to starting position
# Increase speed of cars each time turtle crosses the finish line