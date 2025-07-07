import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
# Scoreboard
# Player Paddle
# Puck/Ball

#screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('PONG')
screen.tracer(0)

#half way line
t = Turtle(shape='square')
t.goto(0, -300)
t.setheading(90)
t.color('white')
t.width(5)
for _ in range(20):
    t.fd(30)
    t.penup()
    t.fd(30)
    t.pendown()

#instantiate classes
r_paddle = Paddle(350, 0)
l_paddle = Paddle(start_x = -350, start_y = 0)

ball = Ball()

r_score = Scoreboard()
l_score = Scoreboard()
game_over = Scoreboard()

#key inputs
screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down,'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down,'s')

#game loop
game_is_on = True
while game_is_on:
    speed_increase = 0.1
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    l_score.score_tally(x_pos = -50)
    r_score.score_tally(x_pos= 50)

    #detect collision with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()

    #detech collision with paddle
    if (ball.distance(r_paddle) < 50 and
        ball.xcor() > 320 or
        ball.distance(l_paddle) < 50 and
        ball.xcor() < -320):
            ball.rebound()

    #right ball out of bounds
    if ball.xcor() > 380:
        ball.reset_position()
        l_score.update_score()

    #left ball out of bounds:
    if ball.xcor() < -380:
        ball.reset_position()
        r_score.update_score()

    #game over:
    if l_score.score == 10 or r_score.score == 10:
        game_over.game_over()
        game_is_on = False


screen.exitonclick()