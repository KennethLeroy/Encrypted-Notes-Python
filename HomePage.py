import tkinter as tk
from tkinter import END, font
import sqlite3
from SafeNotes import Note
import tkinter.messagebox


def add(title, content):
    note = Note(title, content, universalPassword)
    print(note.content)
    qinsert = "INSERT INTO Notes VALUES(?,?)"
    '''INSERT into Notes VALUES(8,"qwer",24);'''
    cursor = connection.cursor()
    cursor.execute(qinsert, (note.title, note.content))
    cursor.close()


def decrypt(index, password):
    # get the password and try decrypting the note with that
    cleartext = listOfnotes[index[0]].decode(password)
    print(cleartext)
    if cleartext:
        tk.messagebox.showinfo("Decoded Value", cleartext)


def homePage(root):
    global listOfnotes
    # get list of all notes from db
    # populate the list of notes from db
    # for each note make a button
    listOfnotes = []
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Notes;")
    rows = cursor.fetchall()
    cursor.close()
    print(f"all the rows are {rows}")
    for row in rows:
        note = Note(row[0], row[1], universalPassword)
        listOfnotes.append(note)
        print(row)
    # qinsert = '''INSERT into Notes VALUES('test','test');'''
    # cursor.execute(qinsert)

    # print(a)
    page = tk.Frame(root)
    page.grid()
    notesListBox = tk.Listbox(page, selectmode="SINGLE")
    notesListBox.grid(row=9)
    for note in listOfnotes:
        notesListBox.insert(END, note.title)
    tk.Label(page, text='This is page 1').grid(row=0)
    tk.Button(page, text='New Note', command=changepage).grid(row=1)
    tk.Label(page, text='Title').grid(row=2)

    clearTextBox = tk.Label(page, text='')
    clearTextBox.grid(row=3)
    passwordBox = tk.Entry()
    passwordBox.grid(row=4)
    tk.Button(page, text='Decrypt',
              command=lambda: decrypt(notesListBox.curselection(), passwordBox.get())).grid(row=5)


def newNotesPage(root):
    page = tk.Frame(root)
    page.grid()
    # tk.Label(page, text='This is page 2').grid(row=0)
    titleBox = tk.Entry()
    titleBox.grid(row=1)
    contentBox = tk.Entry()
    contentBox.grid(row=2)
    tk.Button(page, text='Save', command=lambda: add(
        titleBox.get(), contentBox.get())).grid(row=1)
    tk.Button(page, text='To page 1', command=changepage).grid(row=2)


def changepage():
    global pagenum, root, cursor
    for widget in root.winfo_children():
        widget.destroy()
    if pagenum == 1:
        newNotesPage(root)
        pagenum = 2
    else:
        homePage(root)
        pagenum = 1


listOfnotes = []
connection = sqlite3.connect("Notes.db")
cursor = connection.cursor()
universalPassword = "pass123"
createTable = "CREATE TABLE IF NOT EXISTS Notes (title text,content text);"
cursor.execute(createTable)
cursor.close()
pagenum = 1
root = tk.Tk()
homePage(root)
root.mainloop()

connection.commit()
connection.close()
