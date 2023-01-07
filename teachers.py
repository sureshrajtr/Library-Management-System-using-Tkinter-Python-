import tkinter as tk
from tkinter import *

class stu:
    def __init__(self,root):
        self.root=Frame(root,width=1360,height=768)

        self.b=PhotoImage(file = "lib.png")
        self.label=Label(root,image=self.b).place(x=0,y=0)

        self.c=PhotoImage(file = "teacher.png")
        self.B1=Button(root,image=self.c).place(x=250,y=300)

        self.d=PhotoImage(file = "update2.png")
        self.B2=Button(root,image=self.d,command=self.lib_m3).place(x=600,y=300)

        self.e=PhotoImage(file = "search1.png")
        self.B3=Button(root,image=self.e,command=self.search_teachers).place(x=950,y=300)

        self.g=PhotoImage(file = "home1.png")
        self.B5=Button(root,image=self.g,command=self.Home_page).place(x=0,y=0)

    def lib_m3(self):
        
        import lib_m3
        return
    def Home_page(self):
        import Home_page
        return
    def search_teachers(self):
        import search_teachers
root=Frame(height=768,width=1360).pack()
d=stu(root)
