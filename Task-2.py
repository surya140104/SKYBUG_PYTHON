import tkinter
import string
import random
from tkinter import *

root = Tk()

length_var = tkinter.StringVar()


def submit():
    l1 = []
    l2 = []
    l3 = []
    whole = []
    password = []
    length = length_var.get()
    l1 = string.ascii_letters
    l2 = string.digits
    l3 = string.punctuation
    whole = l1+l2+l3

    n = int(length)
    for i in range(0, n):
        char = random.choice(whole)
        password.append(char)

    result = "".join(password)

    res.config(text=result)


root.geometry("380x330")
root.title("Random Password Generator")
root.config(background="#222329")

name = Label(root,
             text="Random Password Generator",
             font=("Ubuntu", 20),
             justify=CENTER,
             background="#222329",
             foreground="white")
name.grid(row=0, column=0, padx=10, pady=10)

text = Label(root,
             text="Enter the length",
             font=("Ubuntu", 20),
             justify=CENTER,
             background="#222329",
             foreground="white")
text.grid(row=1, column=0, padx=10, pady=10)

en = Entry(root,
           textvariable=length_var,
           font=("Ubuntu", 20),
           justify=CENTER)
en.grid(row=3, column=0, padx=10, pady=5)

sub = Button(root,
             text="Submit",
             border=5,
             font=("Ubuntu", 15),
             command=submit,
             background="black",
             foreground="white",
             activeforeground="white",
             activebackground="black")
sub.grid(row=4, column=0,padx=10,pady=10)

res_name = Label(root,
                 text="Generated Password",
                 font=("Ubuntu", 20),
                 background="#222329",
                 foreground="white",
                 padx=10,
                 pady=10)
res_name.grid(row=6, column=0)

res = Label(root,
            justify=CENTER,
            text="                                      ",
            font=("Ubuntu", 20),
            background="black",
            foreground="white",
            activebackground="black",
            activeforeground="white")
res.grid(row=7, column=0)


root.mainloop()
