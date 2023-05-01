from tkinter import * # imports everything from Tk

my_window= Tk()

label_1=Label (my_window,width="20",height="3", bg="white")

button_1=Button(my_window,text="red",width="6")
button_2=Button(my_window,text="green",width="6")
button_3=Button(my_window,text="blue",width="6")

label_1.grid(row=0,column=1)

button_1.grid(row=1,column=0)
button_2.grid(row=1,column=1)
button_3.grid(row=1,column=2)

def label_red ():
    label_1["bg"]="red"

def label_green ():
    label_1["bg"]="green"

def label_blue():
    label_1["bg"]="blue"

label_1=Label (my_window,width="20",height="3",bg="white")
button_1=Button(my_window,text="red",width=6,command=label_red)
button_2=Button(my_window,text="green",width=6,command=label_green)
button_3=Button(my_window,text="blue",width=6,command=label_blue)

label_1.grid(row=0, column=1)
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

my_window.mainloop()