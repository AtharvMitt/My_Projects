import turtle


class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.Score_value = 1
        self.color("Black")
        self.speed("fastest")
        self.penup()
        self.goto(x=-150, y=260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write("Level: " + str(self.Score_value), align="center", font=("Courier", 24, "normal"))

    def increase_score(self):
        self.Score_value += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))