from turtle import Turtle
import random

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "black", "wheat", "gray"]

tim = Turtle()

def draw_shap(no_side):
    angle = 360 / no_side
    for _ in range(no_side):
        tim.forward(100)
        tim.right(angle)

for shape in range(3,11):
    tim.color(random.choice(colors))
    draw_shap(shape)