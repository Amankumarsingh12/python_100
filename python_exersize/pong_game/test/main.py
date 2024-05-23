from turtle import Turtle, Screen

from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong")

tim = Paddle()




screen.listen()
screen.onkey(tim.go_up, "Up")

screen.exitonclick()