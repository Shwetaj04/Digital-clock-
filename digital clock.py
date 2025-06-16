from tkinter import *
from tkinter.ttk import *
from time import strftime

top=Tk()
top.title("Digital clock")
def none():
    text=strftime('  %H:%M:%S  %p  ')
    lb1.config(text=text)
    lb1.after(1000,none)

lb1=Label(top,font=('digital-7',50,'bold'),background='black',foreground='red')
lb1.pack(anchor='center')
none()
mainloop()
