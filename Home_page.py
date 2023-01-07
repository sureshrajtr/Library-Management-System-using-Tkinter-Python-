from tkinter import *
import tkinter as tk


class home_page:
    def __init__(self,root):
        self.root =Frame(root,height=768,width=1360).pack()
        
        self.b=PhotoImage(file = "lib.png")
        self.label=Label(self.root,image=self.b,text='DAWN LIBRARY').place(x=0,y=0)
        self.c=PhotoImage(file = "BOOK3.png")
        self.b1=Button(self.root,image=self.c,command=self.click).place(x=80,y=243)
        self.s=PhotoImage(file = "stu1.png")
        self.b2=Button(self.root,command=self.click2,image=self.s).place(x=400,y=243)
        self.i=PhotoImage(file = "teacher.png")
        self.b3=Button(self.root,text='click me',image=self.i).place(x=750,y=243)
        self.r=PhotoImage(file = "issue3.png")      
        self.b4=Button(self.root,text='click me',image=self.r).place(x=1100,y=243)
    def click(self):
        import book
        return
    def click2(self):
        import student
        return
root=Frame(height=768,width=1360).pack()
d=home_page(root)


