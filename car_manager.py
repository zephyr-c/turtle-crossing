from turtle import Turtle
import random

MOVE_DISTANCE = 5
MOVE_INCREMENT = 2
COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']

class CarManager():

    def __init__(self):
        self.cars_on_screen = []
        self.generate_car()
        self.car_speed = MOVE_DISTANCE

    def generate_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle()
            car.color(random.choice(COLORS))
            car.penup()
            car.shape('square')
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.setpos(300, random.randint(-250, 250))
            self.cars_on_screen.append(car)

    def move_cars(self, player):
        for car in self.cars_on_screen:
            if car.xcor() < -320:
                car.clear()
                self.cars_on_screen.remove(car)
            else:
                car.backward(self.car_speed)
                if car.distance(player) < 20:
                    player.alive = False

    def go_faster(self):
        self.car_speed += MOVE_INCREMENT


class Car(Turtle):
    def __init__(self):
        super().__init__()


# TODO: 4. Create cars that are 20px high by 40px wide and randomly generated along the y axis between -300 and 300
