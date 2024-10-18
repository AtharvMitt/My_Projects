import turtle
from Bats import Bats
from MidLine import Middle
from Score import Score
from Ball import Ball
import time

is_on = True
pause = True


def end_game():
    global is_on
    is_on = False


def unpause_game():
    global pause
    pause = False


my_screen = turtle.Screen()
my_screen.bgcolor("Black")
my_screen.setup(width=1000, height=600)
my_screen.title("Pong")
my_screen.listen()
my_screen.tracer(0)

Bat_Object = Bats()
Middle_Object = Middle()
Score_Object = Score()


my_screen.onkey(fun=Bat_Object.bat_move_up_left, key="w")
my_screen.onkey(fun=Bat_Object.bat_move_down_left, key="s")
my_screen.onkey(fun=Bat_Object.bat_move_up_right, key="Up")
my_screen.onkey(fun=Bat_Object.bat_move_down_right, key="Down")
my_screen.onkey(fun=end_game, key="space")

ball_object = Ball()

while is_on:
    my_screen.update()
    while pause:
        my_screen.onkey(fun=unpause_game, key="g")
        my_screen.onkey(fun=end_game, key="space")
        my_screen.update()
    if ball_object.Ball_List[0].distance(Bat_Object.Bats_List[0]) < 70 and ball_object.ball_xcor() < -440 or ball_object.Ball_List[0].distance(Bat_Object.Bats_List[1]) < 70 and ball_object.ball_xcor() > 440:
        ball_object.rebound_perpendicular()
        ball_object.MOVE += 0.5
    if ball_object.ball_ycor() > 280 or ball_object.ball_ycor() < -280:
        ball_object.rebound_horizontal()
    if ball_object.ball_xcor() < -500:
        ball_object.ball_recoop()
        Score_Object.score_list[1] += 1
        Score_Object.score_update()
        pause = True
    elif ball_object.ball_xcor() > 500:
        ball_object.ball_recoop()
        Score_Object.score_list[0] += 1
        Score_Object.score_update()
        pause = True
    ball_object.ball_move()


my_screen.exitonclick()
