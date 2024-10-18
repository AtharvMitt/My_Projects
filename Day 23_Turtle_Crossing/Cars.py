import turtle
import random

COLOURS = ["red", "green", "yellow", "blue", "purple", "orange"]
Cars_List = []
rando_start = [0, 0.02, 0.04, 0.06, 0.08, 0.1]


class Cars:
    def __init__(self):
        self.MOVE = 0.2
        self.create_car()

    def create_car(self):
        car_variable = turtle.Turtle()
        car_variable.shape("square")
        car_variable.penup()
        car_variable.setheading(180)
        car_variable.color(random.choice(COLOURS))
        car_variable.shapesize(stretch_len=2, stretch_wid=1)
        car_variable.goto(x=random.randint(-260, 260), y=random.randint(-260, 260))
        Cars_List.append(car_variable)

    def car_move(self):
        for i in range(0, len(Cars_List)):
            Cars_List[i].forward(self.MOVE)

    def car_xcor(self, i):
        return Cars_List[i].xcor()

    def car_ycor(self, i):
        return Cars_List[i].ycor()

    def car_respawn(self, i):
        Cars_List[i].goto(x=290, y=random.randint(-260, 260))

    def access_list(self):
        return Cars_List
