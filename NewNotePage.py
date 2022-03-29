import tkinter as tk
from tkinter import font

root = tk.Tk()
root.title("Test")


def HomePage():
    root.destroy()
    import HomePage


# tk.Button(root, text="New Note", command=newNotePage).pack()
tk.Label(root, text="yay").pack()
tk.Button(root, text="New Note", command=HomePage).pack()

root.mainloop()
