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
car_manager.generate_car()

screen.listen()
screen.onkey(key="Up", fun=player.move)

# game_on = player.alive
loop_count = 0
while player.alive:
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars(player)

    loop_count += 1
    if loop_count == 6:
        car_manager.generate_car()
        loop_count = 0

print("Game Over")




screen.exitonclick()

# Add listen and onkey method to move turtle north
# TODO: 5. Detect when turtle player collides with a car and trigger game over
# TODO: 6. Detect when turtle has reached the top edge of the screen(FINISH_LINE_Y), return turtle to starting position
# TODO: 7. Increase speed of cars each time turtle crosses the finish line