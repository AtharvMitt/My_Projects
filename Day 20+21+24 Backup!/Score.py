import turtle


class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.Score_value = 0
        self.high_score = 0
        self.color("White")
        self.speed("fastest")
        self.penup()
        self.goto(x=0, y=260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write("Score: " + str(self.Score_value) + "  High Score: " + str(self.high_score), align="center", font=("Courier", 24, "normal"))

    def increase_score(self):
        self.Score_value += 1
        self.update_score()

    def reset(self):
        if self.Score_value > self.high_score:
            self.high_score = self.Score_value
        self.Score_value = 0
