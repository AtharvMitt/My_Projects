import turtle
from Turtle import Turtle
from Cars import Cars
from Level import Score

is_on = True

my_screen = turtle.Screen()
my_screen.setup(width=600, height=600)
my_screen.title("Turtle Crossing")
my_screen.listen()
my_screen.tracer(0)

Turtle_Object = Turtle()
Level_Object = Score()
for i in range(24):
    Car_Object = Cars()
Car_Object = Cars()
my_screen.onkey(fun=Turtle_Object.turtle_move, key="w")

while is_on:
    Cars_List = Car_Object.access_list()
    my_screen.update()
    for i in range(len(Cars_List)):
        if Car_Object.car_xcor(i) < -300:
            Car_Object.car_respawn(i)
    Car_Object.car_move()
    for i in range(len(Cars_List)):
        if Turtle_Object.turtles[0].distance(Cars_List[i]) < 30 and Turtle_Object.turtle_ycor() < (Car_Object.car_ycor(i) + 10) and Turtle_Object.turtle_ycor() > (Car_Object.car_ycor(i) - 10):
            Level_Object.game_over()
            is_on = False
    if Turtle_Object.turtle_ycor() > 290:
        Turtle_Object.turtle_recoop()
        Level_Object.increase_score()
        Car_Object.MOVE += 0.1

my_screen.exitonclick()
