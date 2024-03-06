from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.ALL_SQUARES = []
        self.create_snake()
        self.head = self.ALL_SQUARES[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_square(position)

    def add_square(self, position):
        square = Turtle(shape="square")
        square.color("white")
        square.penup()
        square.goto(position)
        self.ALL_SQUARES.append(square)

    def reset(self):
        for seg in self.ALL_SQUARES:
            seg.goto(1000, 1000)
        self.ALL_SQUARES.clear()
        self.create_snake()
        self.head = self.ALL_SQUARES[0]

    def extend(self):
        self.add_square((self.ALL_SQUARES[-1].position()))

    def move(self):
        for square_num in range(len(self.ALL_SQUARES) - 1, 0, -1):
            new_x = self.ALL_SQUARES[square_num - 1].xcor()
            new_y = self.ALL_SQUARES[square_num - 1].ycor()
            self.ALL_SQUARES[square_num].goto(x=new_x, y=new_y)
        self.ALL_SQUARES[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
