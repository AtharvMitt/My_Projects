import turtle as t
import random as r

Tim = t.Turtle()
Tim.hideturtle()
Tim.speed("fastest")
t.colormode(255)
Tim.penup()
Tim.setx(-200)
Tim.sety(-250)
for i in range(50, 501, 50):
    for j in range(10):
        Tim.color(r.randint(0, 255), r.randint(0, 255), r.randint(0, 255),)
        Tim.dot(20)
        Tim.forward(50)
    Tim.setx(-200)
    Tim.sety(-250 + i)

my_screen = t.Screen()
my_screen.exitonclick()
