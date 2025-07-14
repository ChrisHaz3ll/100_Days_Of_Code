import tkinter as tk

window = tk.Tk() #like turtle Screen
window.title('Miles to Kilometer Converter')
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# TODO: Miles to KM Converter:
# Entry, labels, button... 2x3 grid

#Miles Input
miles_input = tk.Entry(width=10)
miles_input.grid(column=1, row=0)

#Miles Label
miles_label = tk.Label(text='Miles')
miles_label.grid(column=2, row=0)

#Is Equal to Label:
equal_to = tk.Label(text = 'is equal to')
equal_to.grid(column=0, row=1)

#KM Conversion Label:
km_conversion = tk.Label(text = 0)
km_conversion.grid(column=1, row=1)

#KM Label:
km_label = tk.Label(text='Km')
km_label.grid(column=2, row=1)

#Conversion function
def conversion():
    km_conversion['text'] = (int(miles_input.get()) * 1.6)

#Calculate Button:
calculate = tk.Button(text='Calculate', command=conversion)
calculate.grid(column=1, row=2)



window.mainloop() #keep window open, always at end of program