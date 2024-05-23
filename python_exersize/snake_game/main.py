from turtle import Turtle, Screen
from snake import Snake
import time

from food import Food
from scoreboad import Scoreboad

'''here we setupt he screen'''
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)



snake = Snake()
food = Food()
scoreboad = Scoreboad()



screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on :

    screen.update()
    time.sleep(0.1)

    snake.move()

    #detect collision
    if snake.all_tim[0].distance(food) < 15:
        print("yam yam")
        food.refresh()
        snake.extend()
        snake.extend()
        snake.extend()
        snake.extend()
        scoreboad.increase_score()

    #detect collision with wall
    if snake.all_tim[0].xcor() > 270 or snake.all_tim[0].xcor() < -270 or snake.all_tim[0].ycor() > 270 or snake.all_tim[0].ycor() < -270:
        game_is_on =False
        scoreboad.game_over()

    #detect collision with tail
    for tim in snake.all_tim[1:]:
        if snake.all_tim[0].distance(tim) < 10:
            game_is_on = False
            scoreboad.game_over()






        
        



screen.exitonclick()