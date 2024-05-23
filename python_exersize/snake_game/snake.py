from turtle import Turtle, Screen

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE  = 20


UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self) :
        self.all_tim = []
        self.creat_snake()

    def creat_snake(self):
        for pos in START_POSITION:
            self.add_snake(pos)


    def add_snake(self, pos):
            tim = Turtle("square")
            tim.color("white")
            tim.penup()
            tim.goto(pos)
            self.all_tim.append(tim)

    def extend(self):
        #add a new segment to the snake
        self.add_snake(self.all_tim[-1].position())


    def move(self):
        for tim_num in range(len(self.all_tim) - 1, 0, -1):
            new_x = self.all_tim[tim_num - 1].xcor()
            new_y = self.all_tim[tim_num - 1].ycor()

            self.all_tim[tim_num].goto(new_x, new_y)

        self.all_tim[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.all_tim[0].heading() != DOWN:
            self.all_tim[0].setheading(UP)

    def down(self):
        if self.all_tim[0].heading() != UP:
            self.all_tim[0].setheading(DOWN)

    def left(self):
        if self.all_tim[0].heading() != RIGHT:
            self.all_tim[0].setheading(LEFT)

    def right(self):
        if self.all_tim[0].heading() != LEFT:
            self.all_tim[0].setheading(RIGHT)


