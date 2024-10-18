import pandas
import tkinter
import random

BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
try:
    to_learn = pandas.read_csv("words_to_learn.csv").to_dict(orient="records")
except FileNotFoundError:
    to_learn = pandas.read_csv("German_to_English.csv").to_dict(orient="records")

def Flip_Card():
    global current_card
    canvas.itemconfig(Card_Side, image=card_back_img)
    canvas.itemconfig(Title_Text, text="English", fill="white")
    canvas.itemconfig(Word_Text, text=current_card["ENGLISH"], fill="white")


def Next_Card_Known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index=False)
    Next_Card_Unknown()

def Next_Card_Unknown():
    global current_card, flip_timer
    my_screen.after_cancel(flip_timer)
    canvas.itemconfig(Card_Side, image=card_front_img)
    current_card = random.choice(to_learn)
    canvas.itemconfig(Word_Text, text=current_card["GERMAN"], fill="black")
    canvas.itemconfig(Title_Text, text="German", fill="black")
    flip_timer = my_screen.after(3000, Flip_Card)


my_screen = tkinter.Tk()
my_screen.title("Flashy")
my_screen.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = my_screen.after(3000, Flip_Card)

canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = tkinter.PhotoImage(file="card_front.png")
card_back_img = tkinter.PhotoImage(file="card_back.png")
Card_Side = canvas.create_image(400, 263, image=card_front_img)
Title_Text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "bold"))
Word_Text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

right_image = tkinter.PhotoImage(file="right.png")
wrong_img = tkinter.PhotoImage(file="wrong.png")
right_button = tkinter.Button(image=right_image, highlightthickness=0, command=Next_Card_Known)
wrong_button = tkinter.Button(image=wrong_img, highlightthickness=0, command=Next_Card_Unknown)
right_button.grid(column=1, row=1)
wrong_button.grid(column=0, row=1)

Next_Card_Unknown()

my_screen.mainloop()
