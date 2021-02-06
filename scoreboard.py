from turtle import Turtle

ALIGNMENT = "left"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-280, 280)
        self.display_level()

    def display_level(self):
        self.clear()
        self.text = f"Level {self.level}"
        self.write(self.text, align=ALIGNMENT, font=FONT)

    def update_level(self):
        self.level += 1
        self.display_level()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)




# Create a scoreboard that keeps track of which level the user is on.
# Increase level each time turtle crosses finish line
# Display GAME OVER in centre of screen when turtle collides with car