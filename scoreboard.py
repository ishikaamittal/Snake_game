import this
from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as file:
            self.highscore = int(file.read())
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.score_display()

    def score_display(self):
        self.clear()
        self.write(f"Score: {self.score} , High Score: {self.highscore}", align=ALIGN, font=FONT)

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", mode="w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.score_display()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.score_display()
