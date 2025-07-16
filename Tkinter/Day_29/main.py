import tkinter as tk
WHITE = '#FFFFFF'
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    user_web = web_input.get()     #input from web_input
    user_email = email_input.get()     #input from email_input
    user_password = password_input.get()     #input from password_input

    # save to data.txt when user clicks add (with open, write, f-string)
    with open('data.txt', 'a') as data:
        data.write(f'\n{user_web} | {user_email} | {user_password}')

    # clear input fields
    web_input.delete(0, 1000)
    password_input.delete(0, 1000)

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title('Password Generator')
window.config(padx=20, pady=20, bg='white')

canvas = tk.Canvas(width=200, height=200, bg='white', highlightthickness=0)
img = tk.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

#Website
web = tk.Label(text='Website', fg='black', bg=WHITE)
web.grid(column=0, row=1)
web_input = tk.Entry(bg=WHITE, highlightthickness=0, fg='black')
web_input.focus()
web_input.grid(column=1, row=1, columnspan=2, sticky='nsew', pady=2)

#Email/User
email = tk.Label(text='Email/Username', fg='black', bg=WHITE)
email.grid(column=0, row=2)
email_input = tk.Entry(bg=WHITE, highlightthickness=0, fg='black')
email_input.insert(0, 'christopher@python.com')
email_input.grid(column=1, row=2, columnspan=2, sticky='nsew', pady=2)

#Password
password = tk.Label(text='Password', fg='black', bg=WHITE)
password.grid(column=0, row=3)
password_input = tk.Entry(bg=WHITE, fg='black', highlightthickness=0)
password_input.grid(column=1, row=3, columnspan=1, sticky='nsew', pady=2)

#Generate Password
gen_pass = tk.Button(text='Generate Password', highlightbackground=WHITE)
gen_pass.grid(column=2, row=3, columnspan=1, pady=2, padx=2)

#Add
add = tk.Button(text='Add', highlightbackground=WHITE, command=save_password)
add.grid(column=1, row=4, columnspan=2, sticky='nsew', pady=2)






window.mainloop()