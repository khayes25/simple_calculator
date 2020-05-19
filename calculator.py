from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#e.insert(0, "")

button_1 = Button(root, text="1")

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)

myButton = Button(root, text="Enter Your Stock Quote", pady=50, command=myClick, fg="blue", bg="#000000")

root.mainloop()