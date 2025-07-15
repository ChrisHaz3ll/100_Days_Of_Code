import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global timer, reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    timer_label['text'] = 'Timer'
    check_mark['text'] = ''
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_time = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break)
        timer_label['text'] = 'BREAK'
        timer_label['fg'] = RED
    elif reps % 2 == 0:
        countdown(short_break) #calls countdown function for button press
        timer_label['text'] = 'BREAK'
        timer_label['fg'] = PINK
        check_mark['text'] += '✓'
    else:
        countdown(work_time)
        timer_label['text'] = 'WORK'

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1) # last *args is what inputs into function
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title('POMODORO')
window.config(padx=100, pady=50, bg=YELLOW)
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = tk.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=img)

#Central Timer
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

#Timer Label
timer_label = tk.Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 48, 'bold'))
timer_label.grid(column=1, row=0)

#Start Button
start = tk.Button(text='Start', highlightbackground=YELLOW, command=start_timer)
start.grid(column=0, row=2)

#Reset Button
reset = tk.Button(text='Reset', highlightbackground=YELLOW, command=reset)
reset.grid(column=2, row=2)

#Check Mark
check_mark = tk.Label(text='', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 36, 'bold'))
check_mark.grid(column=1, row=3)



window.mainloop()