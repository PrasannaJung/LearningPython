from tkinter import *

window = Tk()

window.title("Simple Calculator")
e = Entry(window, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


window.mainloop()