import turtle
import random
import time
DIRECTION = [45, 135, 225, 315]
rando_time = 0.02


class Ball:
    def __init__(self):
        self.Ball_List = []
        self.MOVE = float(10)
        self.create_ball()

    def create_ball(self):
        ball_creator = turtle.Turtle()
        ball_creator.shape("circle")
        ball_creator.color("white")
        ball_creator.speed("fastest")
        ball_creator.penup()
        ball_creator.setheading(random.choice(DIRECTION))
        self.Ball_List.append(ball_creator)

    def ball_move(self):
        self.Ball_List[0].forward(self.MOVE)
        time.sleep(rando_time)

    def ball_xcor(self):
        return self.Ball_List[0].xcor()

    def ball_ycor(self):
        return self.Ball_List[0].ycor()

    def rebound_perpendicular(self):
        ball_direction = self.Ball_List[0].heading()
        if 0 <= ball_direction <= 90:
            self.Ball_List[0].setheading(180-ball_direction)
        elif 180 <= ball_direction <= 270:
            self.Ball_List[0].setheading(540-ball_direction)
        elif 90 <= ball_direction <= 180:
            self.Ball_List[0].setheading(180-ball_direction)
        elif 270 <= ball_direction <= 360:
            self.Ball_List[0].setheading(540-ball_direction)

    def rebound_horizontal(self):
        ball_direction = self.Ball_List[0].heading()
        if 0 <= ball_direction <= 90:
            self.Ball_List[0].setheading(360-ball_direction)
        elif 180 <= ball_direction <= 270:
            self.Ball_List[0].setheading(360-ball_direction)
        elif 90 <= ball_direction <= 180:
            self.Ball_List[0].setheading(360-ball_direction)
        elif 270 <= ball_direction <= 360:
            self.Ball_List[0].setheading(360-ball_direction)

    def ball_recoop(self):
        self.Ball_List[0].hideturtle()
        self.Ball_List[0].goto(0, 0)
        self.MOVE = 10
        self.Ball_List[0].setheading(random.choice(DIRECTION))
        self.Ball_List[0].showturtle()
