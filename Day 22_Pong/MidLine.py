import turtle


class Middle:
    def __init__(self):
        self.create_midline()

    def create_midline(self):
        midline = turtle.Turtle()
        midline.speed("fastest")
        midline.color("white")
        midline.pensize(10)
        midline.penup()
        midline.goto(x=0, y=300)
        midline.setheading(270)
        for i in range(30):
            midline.pendown()
            midline.forward(30)
            midline.penup()
            midline.forward(30)
