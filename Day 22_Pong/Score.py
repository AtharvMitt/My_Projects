import turtle
POSITION = [(-70, 250), (50, 250)]


class Score:
    def __init__(self):
        self.score_list = [0, 0]
        self.score = []
        for position_no in range(2):
            self.create_score(position_no)

    def create_score(self, position):
        score = turtle.Turtle()
        score.speed("fastest")
        score.penup()
        score.hideturtle()
        score.color("white")
        score.goto(POSITION[position])
        self.score.append(score)
        score.write(str(self.score_list[position]), font=("Courier", 35, "bold"))

    def score_update(self):
        for i in range(2):
            self.score[i].clear()
            self.score[i].write(str(self.score_list[i]), font=("Courier", 35, "bold"))
