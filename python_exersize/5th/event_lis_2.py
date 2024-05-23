from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def forward():
    tim.forward(10)

def back():
    tim.backward(10)

def clock():
    tim.right(10)

def conter_clock():
    tim.left(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=back)
screen.onkey(key="a", fun=conter_clock)
screen.onkey(key="d", fun=clock)
screen.onkey(key="c", fun=clear)



screen.exitonclick()
