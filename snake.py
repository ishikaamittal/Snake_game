from turtle import Turtle

snake_positions = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
up = 90
down = 270
right = 0
left = 180

class Snake:

    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head_of_snake = self.snake_segments[0]

    def create_snake(self):
        for p in snake_positions:
            self.add_snake_segment(p)

    def add_snake_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.snake_segments.append(new_segment)

    def reset_snake(self):
        for seg in self.snake_segments:
            seg.goto(1000, 1000)
        self.snake_segments.clear()
        self.create_snake()
        self.head_of_snake = self.snake_segments[0]

    def extend_snake(self):
        self.add_snake_segment(self.snake_segments[-1].position())


    def move(self):
        for s in range(len(self.snake_segments)-1, 0, -1):
            new_x = self.snake_segments[s - 1].xcor()
            new_y = self.snake_segments[s -1].ycor()
            self.snake_segments[s].goto(new_x, new_y)
        self.head_of_snake.forward(move_distance)

    def up(self):
        if self.head_of_snake.heading() != down:
            self.head_of_snake.setheading(up)

    def down(self):
        if self.head_of_snake.heading() != up:
            self.head_of_snake.setheading(down)

    def right(self):
        if self.head_of_snake.heading() != left:
            self.head_of_snake.setheading(right)

    def left(self):
        if self.head_of_snake.heading() != right:
            self.head_of_snake.setheading(left)