import turtle
import pandas

screen = turtle.Screen()
screen.title("Ak.sing")

#path img
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#read data
data = pandas.read_csv("50_states.csv")

#convert it to list
all_state = data["state"].to_list()
#print(all_state)

guessed_list = []

while len(guessed_list) < 50 :
    #promt answer
    answer_state = screen.textinput(title=f"{len(guessed_list)}/50 state core.", 
                                    prompt="state name").title()

    
    if answer_state == "Exit":

        missing_state = []
        for state in all_state:
            if state not in guessed_list:
                missing_state.append(state)
        print(missing_state)

        break
        screen.exitonclick()
        turtle.done()

    if answer_state in all_state :
        #new entry
        guessed_list.append(answer_state)

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_cor = data[data["state"] == answer_state]
        t.goto(int(state_cor['x']), int(state_cor['y']))
        t.write(state_cor['state'].values[0]) 




