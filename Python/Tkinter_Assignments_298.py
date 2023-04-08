Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> win = Tk()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    win = Tk()
NameError: name 'Tk' is not defined
>>> import tkinter
>>> win = Tk()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    win = Tk()
NameError: name 'Tk' is not defined
>>> from tkinter import *
>>> win = Tk()
>>> b1 = Button(win, text="one")
>>> b2 = Button(win, text="two")
>>> b1.grid(row=0, column=0)
>>> b2.grid(row=1, column=1)
>>> 1 = Label(win, text="This is a label")
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> 1.grid(row=1, column=2)
SyntaxError: invalid decimal literal
