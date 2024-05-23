from turtle import Turtle

class Paddle:
    def __init__(self):
        self.turtle = Turtle("square")
        self.turtle.shapesize(stretch_wid=5, stretch_len=1)
        self.turtle.color("white")
        self.turtle.penup()
        self.turtle.goto(350, 0)

    def go_up(self):
        self.turtle.goto(self.turtle.xcor(), self.turtle.ycor() + 20)
        print("hi")