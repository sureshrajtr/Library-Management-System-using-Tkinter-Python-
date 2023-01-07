import tkinter as tk
from tkinter import *
from tkinter import messagebox
import mysql.connector

class rsd():
    def __init__(self,master):
        self.master = master
        self.root =Frame(master,height=768,width=1360,bg='White').pack()
        self.user=StringVar()
        self.user2=StringVar()
        self.user3=StringVar()
        self.user4=StringVar()
        self.d=PhotoImage(file = "back2.png")
        self.l1=Label(self.root,image=self.d).place(x=0,y=0)
        self.c=PhotoImage(file = "lib1.png")
        self.l1=Label(self.root,image=self.c,text='DAWN LIBRARY').place(x=680,y=0)
        

        self.l2=Label(self.root,text='Student ID:',font=('Times',13),bg='Black',fg='white').place(x=780,y=150) 
        self.e1=tk.Entry(self.root,width=30,textvar=self.user).place(x=875,y=150)
        self.l4=Label(self.root,text='Student Name:',font=('Times',13),bg='Black',fg='white').place(x=760,y=200)
        self.e3=tk.Entry(self.root,width=30,textvar=self.user2).place(x=875,y=200)
        self.l3=Label(self.root,text='BOOK ID:',font=('Times',13),bg='Black',fg='white').place(x=790,y=250) 
        self.e2=tk.Entry(self.root,width=30,textvar=self.user3).place(x=875,y=250)
        
        self.l2=Label(self.root,text='BOOK NAME :',font=('Times',13),bg='Black',fg='white').place(x=755,y=300)
        self.e5=tk.Entry(self.root,width=30,textvar=self.user4).place(x=875,y=300)
        self.label=Button(self.root,height=2,width=12,text="submit",font=("times",11),bg="black",fg="white",command=self.click).place(x=900,y=350)
        self.label2=Button(self.root,height=1,width=7,text="search",font=("times",11),bg="black",fg="white",command=self.click7).place(x=980,y=200)
        self.label3=Button(self.root,height=1,width=7,text="search",font=("times",11),bg="black",fg="white",command=self.click6).place(x=980,y=260)

    def click7(self):   
        self.p=self.user.get()
        self.co=mysql.connector.connect(host='localhost',user='root',password='rsd123',database='Library')
        self.c=self.co.cursor()
        self.n2="select (Name) from stu_info1 where stu_id="+str(self.p)
        self.q=self.c.execute(self.n2)
        self.f1=self.c.fetchall()
        self.d1=self.f1
        self.co.close()
        
        print(self.d1)
        self.e3.insert(END,self.d1[0][0])
    def click6(self):
        self.p2=self.user3.get()
        self.co=mysql.connector.connect(host='localhost',user='root',password='rsd123',database='Library')
        self.c=self.co.cursor()
        self.n1="select (Book_name) from book_details where Book_id="+str(self.p2)
        self.c.execute(self.n1)
        self.f2=self.c.fetchall()
        self.d2=self.f1
        self.co.close()

        print(self.d2)
       # self.e5.insert(END,self.d2)



    def click(self):
        g1=self.user.get()
        g2=self.user2.get()
        g3=self.user3.get()
        g4=self.user4.get()
        
        if g1=='' or g2==''or g3==''or g4=='':
            tk.messagebox.showinfo('warning','please fill up all boxes')
    
        else:
            print(g1,g2,g3,g4)
            self.co=mysql.connector.connect(host='localhost',user='root',password='rsd123',database='Library')
            self.c=self.co.cursor()
            self.c.execute("CREATE TABLE IF NOT EXISTS issue_details(Stu_Id varchar(30),Stu_Name varchar(40),Book_Id varchar(10),Book_Name varchar(50),issued_date curdate)")
            self.s="insert into issue_details (Stu_Id,Stu_Name,Book_Id,Book_Name) VALUES ('{}','{}','{}','{}')".format(g1,g2,g3,g4)
            self.c.execute(self.s)
            self.co.commit()
            self.co.close()

            tk.messagebox.showinfo('successful','stored in database')
root=Tk()
d=rsd(root)
root.mainloop()
        
