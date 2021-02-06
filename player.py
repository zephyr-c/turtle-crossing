from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.setpos(STARTING_POSITION)
        self.seth(90)
        self.alive = True

    def move(self):
        self.forward(MOVE_DISTANCE)
        if self.ycor() >= FINISH_LINE_Y:
            self.reset()
            self.__init__()




# Create a turtle player that starts at the bottom of the screen
# Create a move method to move the turtle north. Add screen listen to main file.