import turtle

MOVE = 10

class Turtle:
    def __init__(self):
        self.turtles = []
        self.create_turtle()

    def create_turtle(self):
        turtle_variable = turtle.Turtle()
        turtle_variable.shape("turtle")
        turtle_variable.penup()
        turtle_variable.setheading(90)
        turtle_variable.goto(x=0, y=-280)
        self.turtles.append(turtle_variable)

    def turtle_move(self):
        self.turtles[0].forward(MOVE)

    def turtle_ycor(self):
        return self.turtles[0].ycor()

    def turtle_recoop(self):
        self.turtles[0].goto(x=0, y=-280)
