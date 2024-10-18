import turtle
locations = [(20, 0), (0, 0), (-20, 0)]
Move_Distance = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()

    def create_snake(self):
        for position in locations:
            self.add_segment(position)
            self.snake[0].shape("triangle")


    def add_segment(self, position):
        snake_body = turtle.Turtle(shape="square")
        snake_body.color("white")
        snake_body.penup()
        snake_body.goto(position)
        self.snake.append(snake_body)

    def reset(self):
        for seg in self.snake:
            seg.goto(2000,2000)
        self.snake.clear()
        self.create_snake()

    def extend(self):
        self.add_segment(self.snake[-1].position())

    def snake_move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[i - 1].xcor()
            new_y = self.snake[i - 1].ycor()
            self.snake[i].goto(new_x, new_y)
        self.snake[0].forward(Move_Distance)

    def turnup(self):
        if self.snake[0].heading() != DOWN:
            for i in self.snake:
                i.setheading(UP)

    def turndown(self):
        if self.snake[0].heading() != UP:
            for i in self.snake:
                i.setheading(DOWN)

    def turnright(self):
        if self.snake[0].heading() != LEFT:
            for i in self.snake:
                i.setheading(RIGHT)

    def turnleft(self):
        if self.snake[0].heading() != RIGHT:
            for i in self.snake:
                i.setheading(LEFT)

    def snake_xcor(self, i):
        return self.snake[i].xcor()

    def snake_ycor(self, i):
        return self.snake[i].ycor()