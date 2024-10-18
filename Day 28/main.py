import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check = ""
Timer = None
# ---------------------------- TIMER RESET ------------------------------- # 


def timer_reset():
    global Timer
    global reps
    window.after_cancel(str(Timer))
    Timer_Label.config(text="Timer")
    Check_Mark_Label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_work_timer():
    global check
    global reps
    reps += 1
    if reps % 2 == 1:
        Timer_Label.config(text="WORK")
        count_down(WORK_MIN*60)
    elif reps % 8 == 0:
        Timer_Label.config(text="BREAK", fg=RED)
        check += "✔"
        Check_Mark_Label.config(text=check)
        count_down(LONG_BREAK_MIN*60)
    else:
        Timer_Label.config(text="BREAK", fg=PINK)
        check += "✔"
        Check_Mark_Label.config(text=check)
        count_down(SHORT_BREAK_MIN*60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count_sec):
    global Timer
    minutes = math.floor(count_sec / 60)
    seconds = int(count_sec % 60)
    if seconds < 10:
        seconds = "0" + str(seconds)
    canvas.itemconfig(timer_text, text=str(minutes) + ":" + str(seconds))
    if count_sec > 0:
        Timer = window.after(1000, count_down, count_sec - 1)
    else:
        start_work_timer()

# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

Start_Button = tkinter.Button(text="Start", bg=YELLOW, highlightthickness=0, command=start_work_timer)
Start_Button.grid(column=0, row=2)

Reset_Button = tkinter.Button(text="Reset", bg=YELLOW, highlightthickness=0, command=timer_reset)
Reset_Button.grid(column=2, row=2)

Check_Mark_Label = tkinter.Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
Check_Mark_Label.grid(column=1, row=3)

Timer_Label = tkinter.Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, highlightthickness=0, fg=GREEN)
Timer_Label.grid(column=1, row=0)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()
