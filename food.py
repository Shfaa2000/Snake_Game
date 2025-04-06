import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.shapesize(0.5, 0.5)
        self.penup()
        self.appear()
    def appear(self):
        self.goto(random.randint(-380, 380), random.randint(-380, 380))
