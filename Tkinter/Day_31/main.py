import pandas as pd
import tkinter as tk
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pd.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pd.read_csv('./data/french_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')



# SELECT RANDOM FRENCH WORD:
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn) #random int choice from amount of rows
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=current_card['French'], fill='black')
    canvas.itemconfig(card_bg, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    global current_card
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')
    canvas.itemconfig(card_bg, image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    learn_data = pd.DataFrame(to_learn)
    learn_data.to_csv('data/words_to_learn.csv', index=False)

    next_card()

# WINDOW
window = tk.Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# CANVAS
canvas= tk.Canvas(width=800, height=526)
card_front_img = tk.PhotoImage(file='images/card_front.png')
card_back_img = tk.PhotoImage(file='images/card_back.png')
card_bg = canvas.create_image(400,263, image=card_front_img)
card_title = canvas.create_text(400, 150, text='', font=('Arial', 40, 'italic'), fill='black')
card_word = canvas.create_text(400, 263, text='', font=('Arial', 60, 'bold'), fill='black')
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = tk.PhotoImage(file='images/wrong.png')
cross_button = tk.Button(image=cross_image, highlightthickness=0, command=next_card)
cross_button.grid(row=1, column=0)

check_image = tk.PhotoImage(file='images/right.png')
check_button = tk.Button(image=check_image, highlightthickness=0, command=is_known)
check_button.grid(row=1, column=1)

next_card()







window.mainloop()