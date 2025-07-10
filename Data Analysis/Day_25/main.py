import turtle
import pandas as pd

img = 'blank_states_img.gif'

screen = turtle.Screen()
screen.title('US States Game')
screen.addshape(img)
turtle.shape(img)

score = 0

data = pd.read_csv('50_states.csv')

#check is answer in dataframe
all_states = data.state.to_list()
guessed_states = []
missed_states = []

while len(guessed_states) < 50:
    user_answer = screen.textinput(title=f'State Guesser. Score: {score}/50', prompt='Guess Another State').title()

    if user_answer == 'exit':
        # get states that weren't guessed and extract to csv... states_to_learn.csv
        for i in all_states:
            if i not in guessed_states:
                missed_states.append(i)
        data_to_learn = pd.DataFrame(missed_states)
        data_to_learn.to_csv('states_to_learn.csv')
        break

    if user_answer in all_states:
        guessed_states.append(user_answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == user_answer]
        t.goto(state_data.x.item(), state_data.y.item()) #extracts the single item
        t.write(user_answer)
        score += 1






screen.exitonclick()

