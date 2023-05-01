from tkinter import *
#from PIL import ImageTk, Image

root=Tk()
root.minsize(height=500,width=750) # size of the program

#Tab 1 = Welcome Page
def tab1():
    # Page 2
    def tab2():
        label1.destroy()
        button1.destroy()
        label2= Label(root,text='Night', font=('Century Gothic',35))
        label2.pack()
        bg = PhotoImage(file="Downloads/2022-23DITP DITM-CSC2/IMAGES/CAMP_SUNSHINE_LOGO.png")


        def back():
            label2.destroy()
            button2.destroy()
            tab1()
        button2 = Button(root, text='Exit', font=('Century Gothic',15),command=back)
        button2.pack(side=BOTTOM)  
    label1=Label(root,text='Welcome to Sunshine Adventure Camp', font=('Century Gothic',25))
    label1.pack()
    button1=Button(root,text='Proceed',font=('Catamaran',15), bd='5', command=tab2)
    button1.pack(side=BOTTOM)
tab1()
root.mainloop()