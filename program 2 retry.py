# Sunshine Camp Assessment

from tkinter import *

root=Tk()
root.minsize(height=500,width=750) # size of the program

def window_1():
    def window_2():
        label1.destroy()
        button1.destroy()
        label2= Label(root,text='Night', font=('Century Gothic',15))
        button2 = Button(root, text='Exit', font=('Century Gothic',15),command=back)
        label2.pack()
        button2.pack(side=BOTTOM)
        def back():
            label2.destroy()
            button2.destroy()  
    label1=Label(root,text='Welcome to Sunshine Adventure Camp', font=('Century Gothic',25))
    label1.pack()
    button1=Button(root,text='Proceed',font=('Catamaran',15), bd='5', command=window_2)
    button1.pack(side=BOTTOM)
    bg = PhotoImage(file= "C:\\Users\\super\\Downloads\\IMAGES\\campsunshine.png")
    label1 = Label( root, image = bg )
    label1.place(x = 0, y = 0)
    frame1 = Frame(root)
    frame1.pack(pady = 20 )

window_1()
root.mainloop()
