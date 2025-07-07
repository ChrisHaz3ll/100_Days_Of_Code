from turtle import Turtle

#constants
COORDINATES = [0, -20, -40]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in COORDINATES:
            self.add_part(position)

    def add_part(self, x_position, y_position=0):
        snake_part = Turtle(shape='square')
        snake_part.color('white')
        snake_part.penup()
        snake_part.setposition(y=y_position, x=x_position)
        self.snake_body.append(snake_part)

    def extend(self):
        #add new segment to snake
        self.add_part(x_position=self.snake_body[-1].position()[0],
                      y_position=self.snake_body[-1].position()[1]
                      )

    def move(self):
        for i in range(len(self.snake_body) -1, 0, -1):
            new_x = self.snake_body[i-1].xcor()
            new_y = self.snake_body[i-1].ycor()
            self.snake_body[i].goto(new_x, new_y)
        self.snake_body[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)