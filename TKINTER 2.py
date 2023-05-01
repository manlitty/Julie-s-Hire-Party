from tkinter import *
from tkinter import ttk

root = Tk() # top level window



label = Label(root, text="Hello Python") #what you see
# on screen

# font colour, config is for properties
label.config(text="Hello Python", fg="red") 
label.config(bg="yellow") #background colour
label.config(font='Times 20') 

label.config(text='Python is a great program and we can do lots with it.')
label.config(wraplength='150')          #wrap text if long label
label.config(justify="right")           


label.pack()
root.geometry("300x250")

root.mainloop() #GUI is always looping -
# when you run your mouse over and you can click on
# #any buttons/labels