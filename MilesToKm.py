from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

def miles_to_km():
    m = float(miles_input.get())
    km = round(m * 1.609)
    result.config(text=f"{km}")



#Entry
miles_input = Entry(width=6)
miles_input.insert(END, string="0")
miles_input.grid(column=1, row=0)

#4 labels
text1 = Label(text="Miles")
text1.grid(column=2, row=0)

text2 = Label(text="is equal to")
text2.grid(column=0, row=1)

result = Label(text="0")
result.grid(column=1, row=1)

text3 = Label(text="Km")
text3.grid(column=2, row=1)

#button
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)


window.mainloop()