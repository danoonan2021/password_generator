import tkinter.messagebox
from tkinter import *
import server.server as server

m = Tk()

# Initializing variables
words_var = IntVar()
numbers_var = IntVar()
capitalized_var = IntVar()
symbols_var = IntVar()

m.title("Password Generator")

# Setting up the labels
Label(m, text='Words:').grid(row=0)
Label(m, text='Numbers:').grid(row=1)
Label(m, text='Capitalized:').grid(row=2)
Label(m, text='Special Characters:').grid(row=3)

# Setting up text fields
words_entry       = Entry(m, textvariable=words_var)
numbers_entry     = Entry(m, textvariable=numbers_var)
capitalized_entry = Entry(m, textvariable=capitalized_var)
symbols_entry     = Entry(m, textvariable=symbols_var)
words_entry.grid(row=0, column=1)
numbers_entry.grid(row=1, column=1)
capitalized_entry.grid(row=2, column=1)
symbols_entry.grid(row=3, column=1)

# Setting up input validation
def on_click():
    words = words_var.get()
    numbers = numbers_var.get()
    capitalized = capitalized_var.get()
    symbols = symbols_var.get()

    if not server.validate_pwgen(words, numbers, capitalized, symbols):
        tkinter.messagebox.showinfo("Error", "Invalid Input")
    else:
        pw = server.pwgen(words, numbers, capitalized, symbols)
        tkinter.messagebox.showinfo("Success", pw)

    words_var.set(0)
    numbers_var.set(0)
    capitalized_var.set(0)
    symbols_var.set(0)


# Setting up button
Button(m, text='Generate', command= on_click).grid(row=4, column=1)


# main driver
m.mainloop()


