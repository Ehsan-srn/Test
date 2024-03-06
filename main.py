from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# TODO 1-Create a snake body
# TODO 2-Move the snake
# TODO 3-Control the snake
# TODO 4-Detect collision with food
# TODO 5-Create a scoreboard
# TODO 6-Detect collision with wall
# TODO 7_Detect collision with tail


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score_board = ScoreBoard()


screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.left, key="Left")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

#   Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increase_score()

#   Detect collision with wall.
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        score_board.reset()
        snake.reset()

#   Detect collision with tail.
    for square in snake.ALL_SQUARES[1:]:
        if snake.head.distance(square) < 10:
            score_board.reset()
            snake.reset()


















screen.exitonclick()