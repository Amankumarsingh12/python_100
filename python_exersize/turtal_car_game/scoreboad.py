from turtle import Turtle

class Scoreboad(Turtle):
    def __init__(self) :
        self.level = 1
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.update_scoreboad()
    
    def update_scoreboad(self):
        self.clear()
        self.write(f"level: {self.level}", align="left", font=("Courier", 24, "normal"))

    def increase_level(self):
        self.level += 1
        self.update_scoreboad()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"game over bache", align="center", font=("Courier", 24, "normal"))

