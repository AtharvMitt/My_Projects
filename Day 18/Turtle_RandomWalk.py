import turtle as t
import random

Tim = t.Turtle()
t.colormode(255)
Tim.speed("fastest")
Tim.pensize(15)
Directions=[0, 90, 180, 270]
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
for i in range(150):
    Tim.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    Tim.forward(30)
    Tim.setheading(random.choice(Directions))










































screen = t.Screen()
screen.exitonclick()
