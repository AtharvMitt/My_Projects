import turtle as t
import random as r

is_race_on = False
my_screen = t.Screen()
my_screen.setup(width=500, height=400)
user_bet = my_screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []
colours = ["red", "orange", "yellow", "green", "blue", "purple"]

for turtle_index in range(0, 6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colours[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print("YOU WIN!!")
                print("The winning turtle is: "+str(winning_colour))
                break
            else:
                print("You lose.")
                print("The winning turtle is: "+str(winning_colour))
                break
        rand_distance = r.randint(0, 10)
        turtle.forward(rand_distance)


my_screen.exitonclick()
