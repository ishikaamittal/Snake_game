from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.color("yellow")
        self.refresh()

    def refresh(self):
        food_axis_x = random.randint(-275, 275)
        food_axis_y = random.randint(-275, 275)
        self.goto(food_axis_x, food_axis_y)
