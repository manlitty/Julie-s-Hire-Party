from tkinter import * # imports everything from Tk

root = Tk() # top level window

def callback():
    label.config(text='You clicked me!', fg='red', bg='yellow')
# Here I have added font colour and background
# colour on click


#Create Label
label = Label(root, text="Hello Python")
label.pack()

# Create button(now with the command function)
button = Button(root, text='Click Me!' , command=callback)
button['state'] = 'disabled'
button['state'] = 'normal' # back to normal
button.pack()

root.geometry("350x300")
root.mainloop()