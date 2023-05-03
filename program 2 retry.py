# Sunshine Camp Assessment

from tkinter import *
import tkinter as tk


root=Tk()
root.title("Camp Sunshine")
root.iconbitmap("campsunshine.ico")
root.minsize(height=500,width=750) # size of the program
#Tab 1 - Welcome Page
def window_1():
    def window_2():#page 2
        label1.destroy()
        button1.destroy()
        label2= Label(root,text='Night', font=('Century Gothic',15))
        button2 = Button(root, text='Exit', font=('Century Gothic',15),command=back)
        label2.pack()
        button2.pack(side=BOTTOM)
        def back():
            label2.destroy()
            button2.destroy()
            window_1()  
    label1=Label(root,text='Welcome to Sunshine Adventure Camp', font=('Century Gothic',25))
    label1.pack()
    button1=Button(root,text='Proceed',font=('Catamaran',15), bd='5', command=window_2)
    button1.pack(side=BOTTOM)
    bg = PhotoImage(file= "C:\\Users\\super\\Downloads\\IMAGES\\campsunshine.png")
    label1 = Label( root, image = bg )

    #canvas
    canvas1 = Canvas( root, width = 750,
                 height = 500)
    canvas1.pack(fill = "both", expand = True)
    canvas1.create_image( 0, 0, image = bg, 
                     anchor = "nw")
window_1()
root.mainloop()
