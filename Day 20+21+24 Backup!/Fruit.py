import turtle
import random


class Fruit(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
        self.Fruit_Spawn = [-260, -240, -220, -200, -180, -160, -140, -120, -100, -80, -60, -40, -20, -0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260]

    def refresh(self):
        random_x = random.randint(-260, 260)
        random_y = random.randint(-260, 260)
        self.goto(random_x, random_y)
