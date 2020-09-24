#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 15:10:52 2020

@author: namitabhosle
"""
from tkinter import *
class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='First number')
        self.lbl2=Label(win, text='Second number')
        self.lbl3=Label(win, text='Result')
        self.t1=Entry(bd=3)
        self.t2=Entry(bd=3)
        self.t3=Entry(bd=3)
        self.btn1 = Button(win, text='Add')
        self.btn2 = Button(win, text='Subtract')
        self.lbl1.place(x=80, y=50)
        self.t1.place(x=200, y=50)
        self.lbl2.place(x=80, y=100)
        self.t2.place(x=200, y=100)
        self.b1=Button(win, text='Add', command=self.add)
        self.b2=Button(win, text='Subtract')
        self.b2.bind('<Button-1>', self.sub)
        self.b1.place(x=100, y=150)
        self.b2.place(x=200, y=150)
        self.lbl3.place(x=80, y=200)
        self.t3.place(x=200, y=200)
    def add(self):
        self.t3.delete(0, 'end')
        n1=int(self.t1.get())
        n2=int(self.t2.get())
        result=n1+n2
        self.t3.insert(END, str(result))
    def sub(self, event):
        self.t3.delete(0, 'end')
        n1=int(self.t1.get())
        n2=int(self.t2.get())
        result=n1-n2
        self.t3.insert(END, str(result))

window=Tk()
mywin=MyWindow(window)
window.title('my first python GUI')
window.geometry("500x300+10+10")
window.mainloop()