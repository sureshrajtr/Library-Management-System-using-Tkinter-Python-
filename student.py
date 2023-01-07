import tkinter as tk
from tkinter import *

class stu_page:
    def __init__(self,root):
        self.root=Frame(root,width=1360,height=768)

        self.b=PhotoImage(file = "lib.png")
        self.label=Label(root,image=self.b).place(x=0,y=0)

        self.c=PhotoImage(file = "stu1.png")
        self.B1=Button(root,image=self.c).place(x=134,y=200)

        self.d=PhotoImage(file = "update1.png")
        self.B2=Button(root,image=self.d,command=self.click).place(x=534,y=200)

        self.e=PhotoImage(file = "search1.png")
        self.B3=Button(root,image=self.e,command=self.click3).place(x=850,y=200)

        

        self.g=PhotoImage(file = "home1.png")
        self.B5=Button(root,image=self.g,command=self.click2).place(x=0,y=0)

    def click(self):
        
        import lib_m1
        return
    def click2(self):
        import Home_page
        return
    def click3(self):
        import search_stu_det
        return
root=Frame(height=768,width=1360).pack()
d=stu_page(root)
