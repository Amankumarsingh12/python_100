color_list = [(224, 218, 211), (206, 212, 220), (194, 151, 125), (143, 84, 60), (142, 160, 180), (79, 96, 118)]

import turtle as t
import random
t.colormode(255)

tim = t.Turtle()

tim.speed("fastest")
tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for d_count in range(1, 51):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if d_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


t.Screen().exitonclick()