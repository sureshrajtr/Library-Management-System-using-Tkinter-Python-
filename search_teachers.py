import tkinter as tk
from tkinter import *

import mysql.connector
import tkinter.messagebox
class stu:
    def __init__(self,root):
        self.user=StringVar()
        self.root=Frame(root,width=1360,height=768)
        self.b=PhotoImage(file = "lib.png")
        self.label=Label(root,image=self.b).place(x=0,y=0)
        self.e1=Entry(root,width=30,textvar=self.user).place(x=134,y=200)
        self.b1=Button(root,width=10,bg="black",fg="white",text="search",command=self.click).place(x=280,y=198)

    def click(self):
        self.d=self.user.get()
        self.co=mysql.connector.connect(host='localhost',user='root',password='rsd123',database='Library')
        self.c=self.co.cursor()
        self.s="select * from teachers_info where Teacher_id="+str(self.d)
        self.g=self.c.execute(self.s)
        self.q=self.c.fetchall()
        print(self.q)
        if self.q==[]:
            tk.messagebox.showinfo('Sorry','Not Found In Database')
        else:

            r1=self.q[0][0]
            r2=self.q[0][1]
            r4=self.q[0][2]
            r5=self.q[0][3]
            r6=self.q[0][4]

          
            self.root=Frame(root,width=460,height=668).pack()
            self.d=PhotoImage(file = "back2.png")
            self.l1=Label(self.root,image=self.d).place(x=0,y=0)
            self.label=Label(root,text="STUDENT'S INFORMATION",font=('Times',40),bg="light blue").place(x=350,y=20)

        

            self.label=Label(root,text="TEACHER_ID       :"+str(r1),font=('Times',16),bg="light blue").place(x=500,y=150)
            self.label=Label(root,text="NAME      :"+str(r2),font=('Times',16)).place(x=500,y=200)
            self.label=Label(root,text="D_O_B         :"+str(r4),font=('Times',16)).place(x=500,y=250)
            self.label=Label(root,text="PHONE NO.     :"+str(r5),font=('Times',16)).place(x=500,y=300)
            self.label=Label(root,text="ACCM.YEAR    :"+str(r6),font=('Times',16)).place(x=500,y=350)
            self.b1=Button(root,width=10,bg="black",fg="white",text="Delete",command=self.click1).place(x=580,y=420)


            print("TEACHER_ID     :",self.q[0][0])
            print("NAME   :",self.q[0][1])
            print("D_O_B      :",self.q[0][2])
            print("PHONE NO.  :",self.q[0][3])
            print("ACCM.YEAR  :",self.q[0][4])
    def click1(self):
        self.d=self.user.get()
        self.co=mysql.connector.connect(host='localhost',user='root',password='rsd123',database='Library')
        self.c=self.co.cursor()
        self.s="delete from teachers_info where Teacher_id="+str(self.d)
        self.g=self.c.execute(self.s)
        self.q=self.c.close()
        tk.messagebox.showinfo('successful','Deleted from database')
        
root=Frame(height=768,width=1360).pack()
d=stu(root)        
