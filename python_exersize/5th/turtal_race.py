from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="wchi turtal win race, color")
print(user_bet)

is_race_on = False


colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_axis = [-100, -50, 0, 50, 100, 150]

tim_all = []

for index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[index])
    tim.penup()
    tim.goto(x=-230, y=y_axis[index])
    tim_all.append(tim)

while not is_race_on :



    for turtal in tim_all :
        if turtal.xcor() > 230:
            print(turtal.color())
            is_race_on = True
            win_color = turtal.pencolor()
            if win_color == user_bet:
                print(f"you won {win_color}")
            else:
                print(f"you loss win->color {win_color}")
            break
            

        rand_dis = randint(0, 10)
        turtal.forward(rand_dis)
    
    


screen.exitonclick()