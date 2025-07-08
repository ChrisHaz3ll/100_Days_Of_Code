from turtle import Turtle
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.goto(-200, 250)

    def level_number(self):
        self.color('black')
        self.update_level()

    def update_level(self):
        self.write(f"Level: {self.level}", align='center', font=FONT)

    def new_level(self):
        self.level += 1
        self.clear()
        self.update_level()

    def game_over(self):
        self.color('black')
        self.goto(0, 0)
        self.write(f"GAME OVER", align='center', font=FONT)