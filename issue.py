import tkinter as tk
from tkinter import *



    
class issue_page:
    def __init__(self,root):
        self.root=Frame(root,width=1360,height=768).pack()

        self.b=PhotoImage(file = "lib.png")
        self.label=Label(self.root,image=self.b).place(x=0,y=0)

        self.c=PhotoImage(file = "issue3.png")
        self.B=Button(self.root,image=self.c).place(x=200,y=300)

        self.d=PhotoImage(file = "return1.png")
        self.B1=Button(self.root,image=self.d).place(x=600,y=300)

        self.e=PhotoImage(file = "issue1.png")
        self.B2=Button(self.root,image=self.e,command=self.click).place(x=980,y=300)

        
        self.w=PhotoImage(file = "home1.png")
        self.label=Button(self.root,image=self.w,text='DAWN LIBRARY',command=self.click).place(x=0,y=0)
    def click(self):
        import Home_page
        
root=Frame(height=768,width=1360).pack()
d=issue_page(root)
