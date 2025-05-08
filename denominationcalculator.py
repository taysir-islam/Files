import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
#window setup

root = tk.Tk()
root.title("Denomination Calculator")
root.geometry("400x400")


#main

label1 = Label(root, text="Hello! Welcome to the Denomination Calculator", font=("Arial", 12))
label1.place(relx=0.5, rely=0.1, anchor=CENTER)

def topwin():
    top = Toplevel()
    top.title("Denomination Calculator")
    top.geometry("400x400")

    label2 = Label(top, text="Enter the total amount", font=("Arial", 12))
    label2.place(relx=0.5, rely=0.1, anchor=CENTER)

    entry1 = Entry(top)
    entry1.place(relx=0.5, rely=0.2, anchor=CENTER)

    label3 = Label(top, text="Here are number of notes of each denomination", font=("Arial", 12))
    label3.place(relx=0.5, rely=0.3, anchor=CENTER)

    l1 = Label(top, text="2000")
    l1.place(relx=0.2, rely=0.4, anchor=CENTER)

    l2 = Label(top, text="500")
    l2.place(relx=0.2, rely=0.5, anchor=CENTER) 

    l3 = Label(top, text="200")
    l3.place(relx=0.2, rely=0.6, anchor=CENTER)

    e1 = Entry(top)
    e1.place(relx=0.5, rely=0.4, anchor=CENTER)

    e2 = Entry(top)
    e2.place(relx=0.5, rely=0.5, anchor=CENTER)

    e3 = Entry(top)
    e3.place(relx=0.5, rely=0.6, anchor=CENTER)


    def calculate():
        try:
            global amount
            amount = int(entry1.get())
            note2000 = amount // 2000
            amount%=2000
            note500 = amount // 500
            amount%=500
            note200 = amount // 200
            amount%=200

            e1.delete(0, END)
            e1.insert(END, str(note2000))

            e2.delete(0, END)
            e2.insert(END, str(note500))

            e3.delete(0, END)
            e3.insert(END, str(note200))
        
        except:
            messagebox.showerror("Error", "Please enter a valid amount")

    button2 = Button(top, text="Calculate", command=calculate)
    button2.place(relx=0.5, rely=0.7, anchor=CENTER)

    top.mainloop()

def msg():
    msgbox = messagebox.showinfo("Alert","Do you want to calculate denomination count?\nClick OK to proceed")
    if msgbox == "ok":
        topwin()

button1 =  Button(root, text="Click here to proceed", command=msg())
button1.place(relx=0.5, rely=0.5, anchor=CENTER)



root.mainloop()