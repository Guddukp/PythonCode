import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title('copy....past')
alabel=ttk.Label(root,text='Enter fileName')
alabel.grid(column=0,row=0)
def clickMe():
    try:
        file_name=name.get()
        file_name1=name1.get()
        with open(file_name) as file:
            f=file.read()

        f2=open(file_name1,'w')
        action.configure(f2.write(f))
        alabel.configure(foreground='green')
        f2.close()
    except:
        with open(file_name1) as file:
            f=file.read()
        action.configure(text=f)

action=ttk.Button(root,text='clickMe',command=clickMe)
action.grid(column=1,row=1)

name= tk.StringVar()
name1= tk.StringVar()
textbox=ttk.Entry(root,width=12,textvariable=name)
textbox.grid(column=0,row=1)
textbox1=ttk.Entry(root,width=12,textvariable=name1)
textbox1.grid(column=0,row=2)
root.mainloop()
