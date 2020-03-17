import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Python GUI')
root.resizable(100,100)
alabel=ttk.Label(root,text='A label !')
alabel.grid(column=0,row=0)
def clickMe():
    action.configure(text='** I have been clicked...')
    alabel.configure(foreground='red')

action=ttk.Button(root,text='Click Me',command=clickMe)
action.grid(column=1,row=0)
root.mainloop()
