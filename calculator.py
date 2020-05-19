from tkinter import *

root = Tk()
root.title("Simple Calculator") #Editing the title bar of the window

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10) #Set columnspan to 3 so entry field spans 3 buttons underneath

def button_add():
    return

# Define buttons and put them on the screen

button_1 = Button(root, text="1", padx=40, pady=20, command=button_add).grid(row=3, column=0)
button_2 = Button(root, text="2", padx=40, pady=20, command=button_add).grid(row=3, column=1)
button_3 = Button(root, text="3", padx=40, pady=20, command=button_add).grid(row=3, column=2)

button_4 = Button(root, text="4", padx=40, pady=20, command=button_add).grid(row=2, column=0)
button_5 = Button(root, text="5", padx=40, pady=20, command=button_add).grid(row=2, column=1)
button_6 = Button(root, text="6", padx=40, pady=20, command=button_add).grid(row=2, column=2)

button_7 = Button(root, text="7", padx=40, pady=20, command=button_add).grid(row=1, column=0)
button_8 = Button(root, text="8", padx=40, pady=20, command=button_add).grid(row=1, column=1)
button_9 = Button(root, text="9", padx=40, pady=20, command=button_add).grid(row=1, column=2)

button_0 = Button(root, text="0", padx=40, pady=20, command=button_add).grid(row=4, column=0)
button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_add).grid(row=4, column=1, columnspan=2) #Set columnspan to 2 so "Clear" will span 2 buttons
button_add = Button(root, text="+", padx=39, pady=20, command=button_add).grid(row=5, column=0)
button_equal = Button(root, text="=", padx=91, pady=20, command=button_add).grid(row=5, column=1, columnspan=2) #Set columnspan to 2 so "=" will span 2 buttons


def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)

myButton = Button(root, text="Enter Your Stock Quote", pady=50, command=myClick, fg="blue", bg="#000000")

root.mainloop()