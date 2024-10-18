import turtle
import random
from Snake import Snake

Snake_Object = Snake()


class Fruit(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        Fruit_Spawn_X = [-260, -240, -220, -200, -180, -160, -140, -120, -100, -80, -60, -40, -20, -0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260]
        Fruit_Spawn_Y = [-260, -240, -220, -200, -180, -160, -140, -120, -100, -80, -60, -40, -20, -0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260]
        for i in range(len(Snake_Object.snake)):
            xcor = Snake_Object.snake_xcor(i)
            Fruit_Spawn_X.remove(int(xcor))
        for i in range(len(Snake_Object.snake)):
            ycor = Snake_Object.snake_ycor(i)
            Fruit_Spawn_Y.remove(int(ycor))
        random_x = random.choice(Fruit_Spawn_X)
        random_y = random.choice(Fruit_Spawn_Y)
        self.goto(random_x, random_y)
