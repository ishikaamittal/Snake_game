import turtle
import time

from scoreboard import Scoreboard
from snake import Snake
from food import Food

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # collision of food and snake
    if snake.head_of_snake.distance(food) < 16:
        food.refresh()
        snake.extend_snake()
        score.increase_score()

    # collision of snake with walls
    if snake.head_of_snake.xcor() > 290 or snake.head_of_snake.xcor() < -290 or snake.head_of_snake.ycor() > 290 or \
            snake.head_of_snake.ycor() < -290:
        score.reset_score()
        snake.reset_snake()

    # collision of snake head with any of its segment por tail
    for segment in snake.snake_segments[1:]:
        if snake.head_of_snake.distance(segment) < 10:
            score.reset_score()
            snake.reset_snake()

screen.exitonclick()
