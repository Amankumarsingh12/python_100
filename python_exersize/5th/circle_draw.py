import turtle 
import random

tim = turtle.Turtle()
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    rand = (r, g, b)
    
    return rand

tim.speed("fastest")

for _ in range(30):
    current_heading = tim.heading()
    tim.setheading(current_heading + 10)
    tim.color(random_color())
    tim.circle(100)

turtle.Screen().exitonclick()
