import turtle
LOCATION = [-450, 450]
MOVE = 40


class Bats:
    def __init__(self):
        self.Bats_List = []
        for location in LOCATION:
            self.create_bats(location=location)

    def create_bats(self, location):
        bat = turtle.Turtle()
        bat.shape("circle")
        bat.penup()
        bat.shapesize(1, 7)
        bat.left(90)
        bat.color("white")
        bat.goto(x=location, y=0)
        self.Bats_List.append(bat)

    def bat_move_up_left(self):
        self.Bats_List[0].forward(MOVE)

    def bat_move_down_left(self):
        self.Bats_List[0].back(MOVE)

    def bat_move_down_right(self):
        self.Bats_List[1].back(MOVE)

    def bat_move_up_right(self):
        self.Bats_List[1].forward(MOVE)
