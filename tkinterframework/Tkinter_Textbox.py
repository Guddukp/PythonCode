import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title('python tkinter')
alabel=ttk.Label(root,text='Enter a Name')
alabel.grid(column=0,row=0)
def clickMe():
    file_name=name.get()
    with open(file_name) as file:
        f=file.read()
    action.configure(text=f)
    alabel.configure(foreground='green')

action=ttk.Button(root,text='clickMe',command=clickMe)
action.grid(column=1,row=1)

name= tk.StringVar()

textbox=ttk.Entry(root,width=12,textvariable=name)
textbox.grid(column=0,row=1)
root.mainloop()
