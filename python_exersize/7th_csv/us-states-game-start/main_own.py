import turtle

screen = turtle.Screen()
screen.title("A.k sing is king")

#path of imag
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



while True:
    answer_state = screen.textinput(title="guess", prompt="state name")

    #print(answer_state)

    from chekking import check

    answer = check()
    my_x_y_list = answer.check_ans(answer_state)
    print(my_x_y_list)

    my_turtle = turtle.Turtle()

    x= my_x_y_list[0]
    y= my_x_y_list[1]

    my_turtle.penup()  # Lift the pen to avoid drawing
    my_turtle.hideturtle()
    my_turtle.goto(x, y)

    # Write text at the specified position
    my_turtle.write(answer_state, align="center", font=("Arial", 8, "normal"))



screen.exitonclick()

