import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

root = tk.Tk()
root.title('Combobox...')
root.resizable(100,100)
alabel=ttk.Label(root,text='Enter the name')
alabel.grid(column=0,row=0)
alabel1=ttk.Label(root,text='Choose the number')
alabel1.grid(column=0,row=2)
def clickMe():
    action.configure(text='Hello {} {}'.format(name.get(),number.get()))
    alabel.configure(foreground='red')

action=ttk.Button(root,text='Click Me',command=clickMe, state='disabled' )
action.grid(column=1,row=0)

name= tk.StringVar()
textbox=ttk.Entry(root,textvariable=name)
textbox.grid(column=0,row=1)

number= tk.StringVar()
numberbox= ttk.Combobox(root,width=12,textvariable=number)
numberbox['value']=(1,2,3,4,5,12,34,100)
numberbox.current(0)

chvar= tk.IntVar()
check=ttk.Checkbutton(root,text='Enable',variable=chvar)

check.grid(column=1,row=1)

chvar1= tk.IntVar()
check1=ttk.Checkbutton(root,text='disabled',variable=chvar1)

check1.grid(column=1,row=2)

color1='Blue'
color2='Gold'
color3='Red'

def radcall():
    radsel=radvar.get()
    if radsel==1:
        root.configure(background=color1)
    elif radsel==2:
        root.configure(background=color2)
    elif radsel==3:
        root.configure(background=color3)

radvar= tk.IntVar()

rad1= tk.Radiobutton(root,text=color1,value=1,variable=radvar,command=radcall)
rad1.grid(column=0,row=3)
rad1= tk.Radiobutton(root,text=color2,value=2,variable=radvar,command=radcall)
rad1.grid(column=1,row=3)
rad1= tk.Radiobutton(root,text=color3,value=3,variable=radvar,command=radcall)
rad1.grid(column=2,row=3)

#scrolledtext...
scrollw=30
scrollh=5
scr= scrolledtext.ScrolledText(root,width=scrollw, height=scrollh, wrap=tk.WORD)
scr.grid(column=0)

##Usin for loop in Radiobutton..

colors=['Red','Blue','Green']
radvar1=tk.IntVar()
def radcalls():
    radsel=radvar1.get()
    if radsel==0:
        root.configure(background=colors[0])
    elif radsel==1:
        root.configure(background=colors[1])
    elif radsel==2:
        root.configure(background=colors[2])

for r in range(3):
     
    corerad=tk.Radiobutton(root,text=colors[r],variable=radvar1,value=r,command=radcalls)
    corerad.grid(column=r,row=5)
root.mainloop()
