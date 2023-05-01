# Sunshine Camp Assessment


from tkinter import *

root=Tk()
root.minsize(height=500,width=750) # size of the program

def window_1():
    label1=Label(root,text='Welcome to Sunshine Adventure Camp', font=('Century Gothic',25))
    label1.pack()
    button1=Button(root,text='Proceed',font=('Catamaran',15), bd='5', command=window_2)
    button1.pack(side=BOTTOM)
    def window_2():
        label1.destroy()
        button1.destroy()
        label2= Label(root,text='Night', font=('Century Gothic',15))

window_1()
root.mainloop()
