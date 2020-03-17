import tkinter as tk
from tkinter import ttk
from sys import argv ,exit

if argv[1:]:
    file_name=argv[1]
    file_name2=argv[2]
    with open(file_name) as file:
        f=file.read()
else:
    print('Please enter the fileName at start program')
    exit(0)
root = tk.Tk()
root.title('copy...')
alabel=ttk.Label(root,text='copy {} to {}'.format(file_name,file_name2))
alabel.grid(column=0,row=0)

##copy  function..
def Copy():
    try:
        f2=open(file_name2,'w')
        action.configure(f2.write(f))
        alabel.configure(foreground='red')
        f2.close()
    except TypeError:
        print(' Ok !')
        exit(0)

action=ttk.Button(root,text='Click to copy',command=Copy)
action.grid(column=1,row=0)
root.mainloop()
