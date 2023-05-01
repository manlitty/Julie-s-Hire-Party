from tkinter import *

root = Tk()     # top level window

# Create Label
label = Label(root, text="Hello Python")
label.pack()


# Create button(without command does not do anything)
button=Button(root, text="Click me")
button.pack()

root.geometry("350x200")
root.mainloop() # this is always at the end of the code

#knhom srolanh neak 