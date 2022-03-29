import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("HOMEPAGE")
root.geometry("600x450")

btn1 = Button(root, text="Button 1")
btn1.place(x=35, y=70)

btn2 = Button(root, text="Button 2")
btn2.place(x=35, y=130)

btn3 = Button(root, text="Button 3")
btn3.place(x=35, y=190)

btn4 = Button(root, text="Button 4")
btn4.place(x=35, y=250)

btn5 = Button(root, text="Button 5")
btn5.place(x=35, y=310)

lbl = Label(root, text="LABEL")
lbl.place(x=370, y=40)

txtArea = Entry(root)
txtArea.place(x=250, y=90, height=240, width=300)

key = Entry(root, text="Enter Key")
key.place(x=250, y=360, height=30, width=200)

submit_btn = Button(root, text="Submit")
submit_btn.place(x=500, y=360, height=30)


root.mainloop()
