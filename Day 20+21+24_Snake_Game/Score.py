import turtle


class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.Score_value = 0
        self.color("White")
        self.speed("fastest")
        with open("my_text.txt", "r") as file:
            self.highscore = int(file.read())
        self.penup()
        self.goto(x=0, y=260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        with open("my_text.txt") as text:
            data = text.read()
        self.clear()
        self.write("Score: " + str(self.Score_value) + "  High Score: " + str(data), align="center", font=("Courier", 24, "normal"))


    def increase_score(self):
        self.Score_value += 1
        self.update_score()

    def reset(self):
        High_Score = self.highscore
        if self.Score_value > int(High_Score):
            with open("my_text.txt", "w") as file:
                file.write(str(self.Score_value))
        self.Score_value = 0
