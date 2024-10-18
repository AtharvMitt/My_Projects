import turtle as t
import random as r

Tim = t.Turtle()
Tim.speed("fastest")
t.colormode(255)
for i in range(72):
    Tim.left(5)
    Tim.color(r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))
    Tim.circle(100)

my_screen = t.Screen()
my_screen.exitonclick()
