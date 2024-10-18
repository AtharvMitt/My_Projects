import turtle
import time
from Fruit import Fruit
from Snake import Snake
from Score import Score

is_on = True
pause = True


def Unpause():
    global pause
    pause = False


def End():
    global is_on
    is_on = False


snake = Snake()
Fruit = Fruit()
Score_tracker = Score()

my_screen = turtle.Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("Black")
my_screen.title("My Snake Game")
my_screen.listen()
my_screen.tracer(0)
my_screen.onkey(fun=snake.turnup, key="Up")
my_screen.onkey(fun=snake.turnright, key="Right")
my_screen.onkey(fun=snake.turnleft, key="Left")
my_screen.onkey(fun=snake.turndown, key="Down")
my_screen.onkey(fun=End, key="space")

while is_on:
    while pause:
        my_screen.onkey(fun=Unpause, key="g")
        my_screen.onkey(fun=End, key="space")
        my_screen.update()
    Snake_XCOR = []
    Snake_YCOR = []
    time.sleep(0.1)
    my_screen.update()
    snake.snake_move()
    for i in range(len(snake.snake)):
        xcor = snake.snake_xcor(i)
        Snake_XCOR.append(int(xcor))
    print("Xcor is: " + str(Snake_XCOR))
    for i in range(len(snake.snake)):
        ycor = snake.snake_ycor(i)
        Snake_YCOR.append(int(ycor))
    print("Ycor is: " + str(Snake_YCOR))
    if snake.snake[0].distance(Fruit) < 15:
        Fruit.refresh()
        Score_tracker.increase_score()
        snake.extend()
    if snake.snake[0].xcor() > 290 or snake.snake[0].xcor() < -290 or snake.snake[0].ycor() > 290 or snake.snake[0].ycor() < -290:
        Score_tracker.reset()
        snake.reset()
        pause = True
    for segment in snake.snake[1:len(snake.snake)-1]:
        if segment == snake.snake[0]:
            pass
        elif snake.snake[0].distance(segment) < 10:
            Score_tracker.reset()
            snake.reset()
            pause = True


my_screen.exitonclick()
