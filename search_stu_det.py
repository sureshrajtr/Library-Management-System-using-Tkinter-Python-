import tkinter as tk
from tkinter import *

import mysql.connector
import tkinter.messagebox
class stu_se:
    def __init__(self,root):
        self.root=Frame(root,width=1360,height=768)
        self.user=StringVar()
        self.b=PhotoImage(file = "search2.png")
        self.label=Label(root,image=self.b).place(x=0,y=0)
        self.label2=Label(root,text="SEARCH STUDENT DETAILS",font=("times",31),bg="black",fg="white").place(x=360,y=10)
        self.e1=Entry(root,width=30,textvar=self.user,bg="black",fg="white").place(x=774,y=250)
        self.b1=Button(root,width=10,bg="black",fg="white",text="search",command=self.click).place(x=830,y=288)

    def click(self):
        self.d=self.user.get()
        self.co=mysql.connector.connect(host='localhost',user='root',password='rsd123',database='Library')
        self.c=self.co.cursor()
        self.s="select * from stu_info1 where stu_id="+str(self.d)
        self.g=self.c.execute(self.s)
        self.q=self.c.fetchall()
        print(self.q)
        if self.q==[]:
            tk.messagebox.showinfo('sorry','Not Found in database')


        else:    
            r1=self.q[0][0]
            r2=self.q[0][1]
            r3=self.q[0][2]
            r4=self.q[0][3]
            r5=self.q[0][4]
            r6=self.q[0][5]

          
            self.root=Frame(root,width=460,height=668).pack()
            self.d=PhotoImage(file = "back2.png")
            self.l1=Label(self.root,image=self.d).place(x=0,y=0)
            self.label=Label(root,text="STUDENT'S INFORMATION",font=('Times',40),bg="light blue").place(x=350,y=20)

            self.label=Label(root,text="STU_ID       :"+str(r1),font=('Times',16),bg="light blue").place(x=500,y=150)
            self.label=Label(root,text="STU_NAME      :"+str(r2),font=('Times',16)).place(x=500,y=200)
            self.label=Label(root,text="Class        :"+str(r3),font=('Times',16)).place(x=500,y=250)
            self.label=Label(root,text="D_O_B         :"+str(r4),font=('Times',16)).place(x=500,y=300)
            self.label=Label(root,text="PHONE NO.     :"+str(r5),font=('Times',16)).place(x=500,y=350)
            self.label=Label(root,text="ACCM.YEAR    :"+str(r6),font=('Times',16)).place(x=500,y=400)
            self.b1=Button(root,width=10,bg="black",fg="white",text="Delete",command=self.click1).place(x=580,y=470)


            print("STU_ID     :",self.q[0][0])
            print("STU_NAME   :",self.q[0][1])
            print("Class      :",self.q[0][2])
            print("D_O_B      :",self.q[0][3])
            print("PHONE NO.  :",self.q[0][4])
            print("ACCM.YEAR  :",self.q[0][5])
    def click1(self):
        self.d=self.user.get()
        self.co=mysql.connector.connect(host='localhost',user='root',password='rsd123',database='Library')
        self.c=self.co.cursor()
        self.s="delete from stu_info1 where stu_id="+str(self.d)
        self.c.execute(self.s)
        self.co.commit()
        self.co.close()
        tk.messagebox.showinfo('successful','Deleted from database')
        
root=Frame(height=768,width=1360).pack()
d=stu_se(root)        
