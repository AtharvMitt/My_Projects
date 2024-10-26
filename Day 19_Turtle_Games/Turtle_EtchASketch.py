import turtle as t
import random as r

Tim = t.Turtle()
Tim.pensize(5)


def move_forwards():
    Tim.forward(10)


def move_backwards():
    Tim.back(10)


def turn_right():
    Tim.right(10)


def turn_left():
    Tim.left(10)


def clear():
    Tim.penup()
    Tim.home()
    Tim.pendown()
    Tim.clear()

def PenUpe():
    Tim.penup()

def PenDowne():
    Tim.pendown()

my_screen = t.Screen()
my_screen.listen()
my_screen.onkey(fun=move_forwards, key="w")
my_screen.onkey(fun=move_backwards, key="s")
my_screen.onkey(fun=turn_right, key="d")
my_screen.onkey(fun=turn_left, key="a")
my_screen.onkey(fun=clear, key="c")
my_screen.onkey(fun=PenUpe , key="r")
my_screen.onkey(fun=PenDowne, key="e")
my_screen.exitonclick()
