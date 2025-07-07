from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0) #turns off animation


snake = Snake()
food = Food()
scoreboard = Scoreboard()

#set up key press inputs... function found in Snake Class
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

#Game Loop
game_is_on = True
while game_is_on:
    screen.update()  # updates
    time.sleep(0.12)
    snake.move()

    #update food & score
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()

    #wall collision
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        scoreboard.game_over()
        game_is_on = False

    #tail collision: if head collides with any segment/part
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False




screen.exitonclick()
# COMPLETED: create snake body
# COMPLETED: move & control snake: arrow keys
# COMPLETED: food collision
# COMPLETED: scoreboard
# COMPLETED: detect collision with wall/own tail










