from turtle import Turtle, Screen
import prettytable
import random

color=[]
Tim = Turtle()
Tim.shape("turtle")
Tim.color("red")
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
for i in range(3, 11):
    Tim.color(random.choice(colours))
    for y in range(i):
        Tim.forward(100)
        Tim.right(360/i)
Tim.hideturtle()























screen = Screen()
screen .exitonclick()
