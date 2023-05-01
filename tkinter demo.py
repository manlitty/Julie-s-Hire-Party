import tkinter as tk        # import tkinter module as tk to the program
from tkinter import ttk
root = tk.Tk()              # instance of the tk.TK class that creates the application window



#place a label on the root window
#message = tk.Label(root, text="Hello World")            #Label creates a widget placed on the root window
#message.pack()

root.title("CSC2 2023 Tkinter")

root.geometry("600x400+50+50")
root.resizable(True, False) #set the window to be non-resizable (x,y) (horizontally, vertically)
root.attributes("-alpha",0.5) #set the windoe transparency

root.mainloop()             #main window called root. Can also use main




"""The mainloop keeps the window visible on the screen,
If you don't call the mainloop method, the window will display
and disappear immediately. It keeps the window displaying and running
will you close it.
Place the call to the mainloop method as the last statement in a Tkinter program, after creating the widgets."""