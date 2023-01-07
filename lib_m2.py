import tkinter as tk
from tkinter import *
from tkinter import messagebox
import mysql.connector


class book:
    def __init__(self,root):
        self.root =Frame(root,height=768,width=1360).pack()
        self.user=IntVar()
        self.user1=StringVar()
        self.user2=StringVar()
        self.user3=StringVar()
        self.user4=StringVar()
        self.user5=StringVar()   
    
        self.a=PhotoImage(file = "back2.png")    
        self.l1=label=Label(self.root,image=self.a,text='DAWN LIBRARY').place(x=0,y=0)
        self.b=PhotoImage(file = "lib1.png")    
        self.l1=label=Label(self.root,image=self.b,text='DAWN LIBRARY').place(x=540,y=0)
        self.l2=Label(self.root,text='Book ID:',font=('Times',13),bg='Black',fg='white').place(x=650,y=150)
        self.e1=Entry(self.root,width=30,textvar=self.user).place(x=730,y=150)
        self.l3=Label(self.root,text='Book Name :',font=('Times',13),bg='Black',fg='white').place(x=630,y=200)
        self.e2=Entry(self.root,width=30,textvar=self.user1).place(x=730,y=200)
        self.l4=Label(self.root,text='Author Name :',font=('Times',13),bg='Black',fg='white').place(x=620,y=250)
        self.e3=Entry(self.root,width=30,textvar=self.user2).place(x=730,y=250)
        self.l5=Label(self.root,text='Catagory :',font=('Times',13),bg='Black',fg='white').place(x=650,y=300)
        self.e4=Entry(self.root,width=30,textvar=self.user3).place(x=730,y=300)
        self.l6=Label(self.root,text='Publication :',font=('Times',13),bg='Black',fg='white').place(x=630,y=350)
        self.e5=Entry(self.root,width=30,textvar=self.user4).place(x=730,y=350)
        self.l7=Label(self.root,text='Cost of Book :',font=('Times',13),bg='Black',fg='white').place(x=615,y=400)
        self.e6=Entry(self.root,width=30,textvar=self.user5).place(x=730,y=400)
        self.c=Button(self.root,width=7,height=2,text='Submit',font=10,bg='Black',fg='White',command=self.click).place(x=850,y=450)
        self.q=PhotoImage(file = "back1.png")
        self.label=Button(self.root,image=self.q,text='DAWN LIBRARY',command=self.click2).place(x=45,y=0)
        self.w=PhotoImage(file = "home1.png")
        self.label2=Button(self.root,image=self.w,text='DAWN LIBRARY',command=self.click1).place(x=0,y=0)
    def click(self):
        e=self.user.get()
        e1=self.user1.get()
        e2=self.user2.get()
        e3=self.user3.get()
        e4=self.user4.get()
        e5=self.user5.get()
  
        if e=='' or e1=='' or e2=='' or e3=='' or e4 =='' or e5=='':
            tk.messagebox.showinfo('warning','please fill up all boxes')
    
        else:
            self.co=mysql.connector.connect(host='localhost',user='root',password='rsd123',database='Library')
            self.c=self.co.cursor()
            self.c.execute("CREATE TABLE IF NOT EXISTS Book_details(Book_id integer(8),Book_name varchar(50),Author_name varchar(50),Catagory varchar(50),Publication varchar(50),Cost_of_Book varchar(10))")
            self.c.execute("insert into Book_details (Book_id,Book_name,Author_name,Catagory,Publication,Cost_of_Book) VALUES ({},'{}','{}','{}','{}','{}')".format(e,e1,e2,e3,e4,e5))
            self.co.commit()
            self.co.close()
            
            tk.messagebox.showinfo('successful','stored in database')
    def click1(self):
        import Home_page
    def click2(self):
        import book
root=Frame(height=768,width=1360).pack()
d=book(root)
