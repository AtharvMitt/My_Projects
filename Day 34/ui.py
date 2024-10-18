import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.Score_Counter = tkinter.Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.Score_Counter.grid(column=1, row=0)

        self.canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Question goes here!", fill=THEME_COLOR, font=("Ariel", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        Tick_Image = tkinter.PhotoImage(file="images/true.png")
        self.tick = tkinter.Button(image=Tick_Image, command=self.Check_Correct)
        self.tick.grid(column=0, row=2)

        Wrong_Image = tkinter.PhotoImage(file="images/false.png")
        self.cross = tkinter.Button(image=Wrong_Image, command=self.Check_False)
        self.cross.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.Score_Counter.config(text="Score: " + str(self.quiz.score))
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.Score_Counter.config(text="Score: " + str(self.quiz.score))
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.tick.config(state="disabled")
            self.cross.config(state="disabled")

    def Check_Correct(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def Check_False(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
