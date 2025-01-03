from turtle import Turtle

FONT = ('Courier',18,'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280,270)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.write_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align='center',font=FONT)
