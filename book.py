import tkinter as tk
from tkinter import *



    
class book_page:
    def __init__(self,root):
        self.root=Frame(root,width=1360,height=768).pack()

        self.b=PhotoImage(file = "lib.png")
        self.label=Label(self.root,image=self.b).place(x=0,y=0)

        self.c=PhotoImage(file = "book3.png")
        self.B=Button(self.root,image=self.c).place(x=250,y=300)

        self.d=PhotoImage(file = "update2.png")
        self.B1=Button(self.root,image=self.d).place(x=600,y=300)

        self.e=PhotoImage(file = "search1.png")
        self.B2=Button(self.root,image=self.e,command=self.click2).place(x=950,y=300)

        
        self.w=PhotoImage(file = "home1.png")
        self.label=Button(self.root,image=self.w,text='DAWN LIBRARY',command=self.click1).place(x=0,y=0)
    def click(self):
        import lib_m2
        return
    def click1(self):
        import Home_page
        return
    def click2(self):
        import book_search
        return

root=Frame(height=768,width=1360).pack()
d=book_page(root)

