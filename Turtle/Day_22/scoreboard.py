from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()

    def score_tally(self, x_pos):
        self.color('white')
        self.goto(x_pos, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.score}", align='center', font=('Courier', 24, 'normal'))

    def game_over(self):
        self.color('white')
        self.goto(0,0)
        self.write(f"GAME OVER", align='center', font=('Courier', 36, 'bold'))

    def update_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()