from turtle import Turtle, Screen
import random
screen = Screen()

screen.setup(width = 500, height = 400) #screen size
user_bet = screen.textinput(title = "Race Bet", prompt = "Who will win? red, blue, green, purple?")

colours = ['red', 'blue', 'green', 'purple']
y_positions = [-70, -40, -10, 20]
all_turtles = []

#set start position
for index in range(0, 4):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colours[index])
    new_turtle.penup()
    new_turtle.setpos(-200, y_positions[index])
    all_turtles.append(new_turtle) #adds that new turtle to a list of turtles

#race
if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles: #applies actions to each turtle in list
        if turtle.xcor() > 200:
            race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print (f"You've won! The winner was {winning_colour}")
            else:
                print(f"You've lost. The winner was {winning_colour}")
        turtle.forward(random.randint(1,10))






screen.exitonclick()
