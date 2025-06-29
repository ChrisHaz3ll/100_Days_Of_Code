import turtle as t
import random


t.colormode(255)

turtle = t.Turtle()
turtle.speed('fastest')

def random_colour():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour

# Spirograph
# new_heading = 5
# for _ in range(72):
#     turtle.color(random_colour())
#     turtle.circle(100)
#     turtle.setheading(new_heading)
#     new_heading += 5

# TODO: Project Challenge
#dot
#pen up, forward x spaces
#pen down, dot
#restart line above
def start_new_line():
    turtle.penup()
    turtle.backward(250)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)

for _ in range(10):
    for _ in range(10):
        turtle.dot(10, random_colour())
        turtle.penup()
        turtle.fd(25)
    start_new_line()




screen = t.Screen()
screen.exitonclick()
