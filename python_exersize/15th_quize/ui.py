from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quize_brain: QuizBrain) :
        self.quiz = quize_brain

        ##creat screen ###
        self.windoew = Tk()
        self.windoew.title("Quizezler")
        self.windoew.config(padx=20, pady=20, bg=THEME_COLOR)
        ####

        ###lable ###
        self.score_lable = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_lable.grid(row=0, column=1)

        ############ this will create a img on windows ############### 
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 
            125,
            width=280, 
            text="aman", 
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
            )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        ##############################################

        ##button###
        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.check_ans_true)
        self.true_button.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.check_ans_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_que()

        self.windoew.mainloop()

    def get_next_que(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_lable.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, 
                                   text=f"You've completed the quiz\nYour final score was: {self.quiz.score}")

            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        

    def check_ans_true(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)
        

    def check_ans_false(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        
        self.windoew.after(1000, self.get_next_que)
        

        