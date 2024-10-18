import turtle
import pandas
import time

my_screen = turtle.Screen()
my_screen.setup(width=750, height=1000)
my_screen.bgpic("India Political_2.Gif")

State_Name = turtle.Turtle()
State_Name.penup()
State_Name.speed("fastest")
State_Name.hideturtle()

data = pandas.read_csv("State_Names")
data_states = data["state"].to_list()
i = 0
Mistakes = 3
guessed_states = []
while i < len(data_states) and Mistakes > 0:
    user_guess = my_screen.textinput(title="Make your Guess", prompt="Guess the next State of India! ").title()
    if user_guess == "Exit":
        missing_states = [state for state in data_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if user_guess in data_states:
        Working_Data = data[data.state == user_guess]
        guessed_states.append(user_guess)
        State_Name.goto(x=int(Working_Data["x"]), y=int(Working_Data["y"]))
        State_Name.write(user_guess, align="center", font=("Courier", 8, "bold"))
        i += 1
    else:
        Mistakes -= 1
        Game_Over = turtle.Turtle()
        Game_Over.penup()
        Game_Over.speed("fastest")
        Game_Over.hideturtle()
        Game_Over.goto(x=0, y=0)
        if Mistakes >= 1:
            Game_Over.write("Wrong Guess! Continue after message disappears!! \n You have " + str(Mistakes) + " Mistakes remaining", align="center", font=("Courier", 18, "bold"))
            time.sleep(5)
            Game_Over.clear()
            continue
        else:
            break
State_Name.goto(x=0, y=0)
if Mistakes == 0:
    missing_states = [state for state in data_states if state not in guessed_states]
    new_data = pandas.DataFrame(missing_states)
    new_data.to_csv("states_to_learn.csv")
    State_Name.write("YOU LOSE!!!", align="center", font=("Courier", 24, "bold"))
elif i == 33:
    missing_states = [state for state in data_states if state not in guessed_states]
    new_data = pandas.DataFrame(missing_states)
    new_data.to_csv("states_to_learn.csv")
    State_Name.write("CONGRATS! You named every state!!", align="center", font=("Courier", 24, "bold"))
else:
    State_Name.write("Dont Worry Try again Later!!", align="center", font=("Courier", 24, "bold"))
my_screen.exitonclick()
