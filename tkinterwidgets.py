import tkinter as tk
from tkinter import *
from tkinter import messagebox

root = tk.Tk()
root.geometry("200x200")

# # upload = Image(file="calculator.py/calculator_icon.png")
# # image = Image.PhotoImage(upload)

# # label = Label(image=image)
# # label.pack()

# # label2 = Label(text="This is image^^^")
# # label2.pack()

# def msg():
#     messagebox.showinfo("Alert", "Virus found")
# button = Button(root, text="Check for Virus", command=msg)
# button.pack()



def topwin():
    top = Toplevel()
    top.title("New Window")
    top.geometry("200x200")
    label = Label(top, text="This is a new window")
    label.pack()
    new_button = Button(top, text="Open another window", command=topwin)
    new_button.pack()
    new_button.pack()
    top.mainloop()
button = Button(root, text="Open new window", command=topwin)
button.pack()



root.mainloop()
