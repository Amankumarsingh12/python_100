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

move = [90, -90 ]

direction = [0, 90, 180, 270]


'''
for _ in range(10):
    tim.color(random.choice(colors))
    tim.width(10)
    tim.forward(30)
    tim.left(random.choice(move))
'''

tim.speed("fastest")

for _ in range(90):
    tim.color(random_color())
    tim.width(10)
    tim.forward(30)
    tim.setheading(random.choice(direction))
