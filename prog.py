from tkinter import *
import tkinter as tk
from tkinter import messagebox
import mysql.connector
from tkinter import ttk
from datetime import timedelta, date
#==================================SQL_creations==================================#
db='Library5'
pasw='rsd123'
co=mysql.connector.connect(host='localhost',user='root',password=pasw)
c=co.cursor()
c.execute("create database IF NOT exists Library5")
co.close()
co=mysql.connector.connect(host='localhost',user='root',password=pasw,database=db)
c=co.cursor()
c.execute("CREATE TABLE IF NOT EXISTS T_issue_details(Teacher_Id varchar(30),Teacher_Name varchar(40),Book_Id varchar(10),Book_Name varchar(50),issued_date varchar(15),Return_date varchar(15))")
c.execute("CREATE TABLE IF NOT EXISTS issue_details(Stu_Id varchar(30),Stu_Name varchar(40),Book_Id varchar(10),Book_Name varchar(50),issued_date varchar(15),Return_date varchar(15))")
c.execute("CREATE TABLE IF NOT EXISTS Book_details(Book_id integer(8) UNIQUE,Book_name varchar(50),Author_name varchar(50),Catagory varchar(50),Publication varchar(50),Cost_of_Book varchar(10))")
c.execute("CREATE TABLE IF NOT EXISTS stu_info1(stu_id varchar(15) UNIQUE,Name varchar(50),class varchar(50),D_O_B varchar(50),phone_no BIGINT,Accadmic_year varchar(10))")
c.execute("CREATE TABLE IF NOT EXISTS teachers_info(Teacher_id varchar(10)UNIQUE,Name varchar(50),D_O_B varchar(50),phone_no BIGINT,Accadmic_year varchar(50))")
co.close()
#===================================HOME_PAGE=====================================#
class home_page:
    def __init__(self,root):
        self.root =Frame(root,height=768,width=1360).pack()
        self.b=PhotoImage(file = "lib.png")
        self.label=Label(root,image=self.b,text='DAWN LIBRARY').place(x=0,y=0)
        self.c=PhotoImage(file = "BOOK3.png")
        self.b1=Button(root,image=self.c,command=self.click).place(x=80,y=243)
        self.s=PhotoImage(file = "stu1.png")
        self.b2=Button(root,command=self.click1,image=self.s).place(x=400,y=243)
        self.i=PhotoImage(file = "teacher.png")
        self.b3=Button(root,text='click me',image=self.i,command=self.click2).place(x=750,y=243)
        self.r=PhotoImage(file = "issue3.png")      
        self.b4=Button(root,text='click me',image=self.r,command=self.click3).place(x=1100,y=243)
    def click(self):
        book_page(root)
    def click1(self):
        stu_page(root)
    def click2(self):
        teachers_page(root)
    def click3(self):
       issue_page(root)
#==================================BOOK_PAGE=================================#    
class book_page:
    def __init__(self,root):
        self.root=Frame(root,width=1360,height=768).pack()
        self.b=PhotoImage(file = "lib.png")
        self.label=Label(self.root,image=self.b).place(x=0,y=0)
        self.c=PhotoImage(file = "book33.png")
        self.B=Button(self.root,image=self.c,command=self.clic6).place(x=250,y=300)
        self.d=PhotoImage(file = "update2.png")
        self.B1=Button(self.root,image=self.d,command=self.click4).place(x=600,y=300)
        self.e=PhotoImage(file = "search1.png")
        self.B2=Button(self.root,image=self.e,command=self.click6).place(x=950,y=300)
        self.w=PhotoImage(file = "home1.png")
        self.label=Button(self.root,image=self.w,text='DAWN LIBRARY',command=self.click5).place(x=0,y=0)
    def click4(self):
        book_update(root)
    def click5(self):
        home_page(root)
    def click6(self):
        book_search(root)
    def clic6(self):
       book_table(root)
#===================================STU_PAGE==================================#    
class stu_page:
    def __init__(self,root):
        self.root=Frame(root,width=1360,height=768)
        self.b=PhotoImage(file = "lib.png")
        self.label=Label(root,image=self.b).place(x=0,y=0)
        self.c=PhotoImage(file = "stu12.png")
        self.B1=Button(root,image=self.c,command=self.click76).place(x=134,y=200)
        self.d=PhotoImage(file = "update1.png")
        self.B2=Button(root,image=self.d,command=self.click7).place(x=534,y=200)
        self.e=PhotoImage(file = "search12.png")
        self.B3=Button(root,image=self.e,command=self.click8).place(x=850,y=200)
        self.g=PhotoImage(file = "home1.png")
        self.B5=Button(root,image=self.g,command=self.click9).place(x=0,y=0)
    def click7(self):
        stu_update(root)
    def click9(self):
        home_page(root)
    def click8(self):
       stu_search(root)
    def click76(self):
       stu_table(root)
#==================================TEACHER_PAGE================================#   
class teachers_page:
    def __init__(self,root):
        self.root=Frame(root,width=1360,height=768)
        self.b=PhotoImage(file = "lib.png")
        self.label=Label(root,image=self.b).place(x=0,y=0)
        self.c=PhotoImage(file = "teacher1.png")
        self.B1=Button(root,image=self.c,command=self.tab).place(x=250,y=300)
        self.d=PhotoImage(file = "update3.png")
        self.B2=Button(root,image=self.d,command=self.lib_m3).place(x=600,y=300)
        self.e=PhotoImage(file = "search13.png")
        self.B3=Button(root,image=self.e,command=self.search_teachers).place(x=950,y=300)
        self.g=PhotoImage(file = "home1.png")
        self.B5=Button(root,image=self.g,command=self.Home_page).place(x=0,y=0)
    def lib_m3(self):
        teach_update(root)
    def Home_page(self):
        home_page(root)
    def search_teachers(self):
        teach_search(root)
    def tab(self):
        teacher_table(root)
#=====================================ISSUE_PAGE==============================#
class issue_page:
    def __init__(self,root):
        self.root=Frame(root,width=1360,height=768).pack()
        self.b=PhotoImage(file = "lib.png")
        self.label=Label(self.root,image=self.b).place(x=0,y=0)
        self.c=PhotoImage(file = "issue2.png")
        self.B=Button(self.root,image=self.c,command=self.click28).place(x=200,y=300)
        self.d=PhotoImage(file = "return1.png")
        self.B1=Button(self.root,image=self.d,command=self.click284).place(x=600,y=300)
        self.e=PhotoImage(file = "issue1.png")
        self.B2=Button(self.root,image=self.e,command=self.cli).place(x=980,y=300)
        self.w=PhotoImage(file = "home1.png")
        self.label=Button(root,image=self.w,text='DAWN LIBRARY',command=self.click10).place(x=0,y=0)
    def click10(self):
        home_page(root)
    def click28(self):
        c_issue_book(root)
    def click284(self):
        c_return_book(root)
    def cli(self):
        c_issue_table(root)
#=====================================STU_UPDATE==============================#                
class stu_update:
    def __init__(self,root):
        self.root =Frame(root,height=768,width=1360).pack()
        self.user=StringVar()
        self.user1=StringVar()
        self.user2=StringVar()
        self.user3=StringVar()
        self.user4=IntVar()
        self.user5=StringVar()   
        self.a=PhotoImage(file = "back2.png")    
        self.l1=label=Label(root,image=self.a,text='DAWN LIBRARY').place(x=0,y=0)
        self.b=PhotoImage(file = "lib1.png")    
        self.l1=Label(root,image=self.b,text='DAWN LIBRARY').place(x=540,y=0)
        self.l2=Label(root,text='Student ID:',font=('Times',13),bg='Black',fg='white').place(x=635,y=150)
        self.e1=Entry(root,width=30,textvar=self.user).place(x=730,y=150)
        self.l3=Label(root,text='Student Name:',font=('Times',13),bg='Black',fg='white').place(x=610,y=200)
        self.e2=Entry(root,width=30,textvar=self.user1).place(x=730,y=200)
        self.l4=Label(root,text='Class  :',font=('Times',13),bg='Black',fg='white').place(x=655,y=250)
        self.e3=Entry(root,width=30,textvar=self.user2).place(x=730,y=250)
        self.l5=Label(root,text='Date Of Birth:',font=('Times',13),bg='Black',fg='white').place(x=610,y=300)
        self.e4=Entry(root,width=30,textvar=self.user3).place(x=730,y=300)
        self.l6=Label(root,text='Phone No. :',font=('Times',13),bg='Black',fg='white').place(x=630,y=350)
        self.e5=Entry(root,width=30,textvar=self.user4).place(x=730,y=350)
        self.l7=Label(root,text='Accedmic Year:',font=('Times',13),bg='Black',fg='white').place(x=605,y=400)
        self.e6=Entry(root,width=30,textvar=self.user5).place(x=730,y=400)
        self.c=Button(root,width=7,height=2,text='Submit',font=10,bg='Black',fg='White',command=self.click11).place(x=750,y=450)
        self.q=PhotoImage(file = "back1.png")
        self.label=Button(root,image=self.q,text='DAWN LIBRARY',command=self.click13).place(x=45,y=0)
        self.w=PhotoImage(file = "home1.png")
        self.label2=Button(root,image=self.w,text='DAWN LIBRARY',command=self.click12).place(x=0,y=0)
    def click11(self):
        e=self.user.get()
        e1=self.user1.get()
        e2=self.user2.get()
        e3=self.user3.get()
        e4=self.user4.get()
        e5=self.user5.get()
        co=mysql.connector.connect(host='localhost',user='root',password=pasw,database=db)
        c=co.cursor()
        c.execute("select (stu_id) from stu_info1")
        b=c.fetchall()
        m=[]
        S=len(b)
        for i in range (S):
           m.append(b[i][0])
        if e=='' or e1=='' or e2=='' or e3=='' or e4 =='' or e5=='':
            tk.messagebox.showinfo('warning','please fill up all boxes')
        elif e in m:
            tk.messagebox.showinfo('warning','Id Alredy Exist')
        else:
            self.co=mysql.connector.connect(host='localhost',user='root',password=pasw,database=db)
            self.c=self.co.cursor()
            self.c.execute("insert into stu_info1 (stu_id,Name,class,D_O_B,phone_no,Accadmic_year) VALUES ('{}','{}','{}','{}',{},'{}')".format(e,e1,e2,e3,e4,e5))
            self.co.commit()
            self.co.close()
            tk.messagebox.showinfo('successful','stored in database')
    def click12(self):
        home_page(root)
    def click13(self):
       stu_page(root)
#======================================BOOK_UPDATE=============================#       
class book_update:
    def __init__(self,root):
        self.root =Frame(root,height=768,width=1360).pack()
        self.user=IntVar()
        self.user1=StringVar()
        self.user2=StringVar()
        self.user3=StringVar()
        self.user4=StringVar()
        self.user5=StringVar()   
        self.a=PhotoImage(file = "back2.png")    
        self.l1=label=Label(root,image=self.a,text='DAWN LIBRARY').place(x=0,y=0)
        self.b=PhotoImage(file = "lib1.png")    
        self.l1=label=Label(root,image=self.b,text='DAWN LIBRARY').place(x=540,y=0)
        self.l2=Label(root,text='Book ID:',font=('Times',13),bg='Black',fg='white').place(x=650,y=150)
        self.e1=Entry(root,width=30,textvar=self.user).place(x=730,y=150)
        self.l3=Label(root,text='Book Name :',font=('Times',13),bg='Black',fg='white').place(x=630,y=200)
        self.e2=Entry(root,width=30,textvar=self.user1).place(x=730,y=200)
        self.l4=Label(root,text='Author Name :',font=('Times',13),bg='Black',fg='white').place(x=620,y=250)
        self.e3=Entry(root,width=30,textvar=self.user2).place(x=730,y=250)
        self.l5=Label(root,text='Catagory :',font=('Times',13),bg='Black',fg='white').place(x=650,y=300)
        self.e4=Entry(root,width=30,textvar=self.user3).place(x=730,y=300)
        self.l6=Label(root,text='Publication :',font=('Times',13),bg='Black',fg='white').place(x=630,y=350)
        self.e5=Entry(root,width=30,textvar=self.user4).place(x=730,y=350)
        self.l7=Label(root,text='Cost of Book :',font=('Times',13),bg='Black',fg='white').place(x=615,y=400)
        self.e6=Entry(root,width=30,textvar=self.user5).place(x=730,y=400)
        self.c=Button(root,width=7,height=2,text='Submit',font=10,bg='Black',fg='White',command=self.click14).place(x=850,y=450)
        self.q=PhotoImage(file = "back1.png")
        self.label=Button(root,image=self.q,text='DAWN LIBRARY',command=self.click16).place(x=45,y=0)
        self.w=PhotoImage(file = "home1.png")
        self.label2=Button(root,image=self.w,text='DAWN LIBRARY',command=self.click15).place(x=0,y=0)
    def click14(self):
        e=self.user.get()
        e1=self.user1.get()
        e2=self.user2.get()
        e3=self.user3.get()
        e4=self.user4.get()
        e5=self.user5.get()
        co=mysql.connector.connect(host='localhost',user='root',password=pasw,database=db)
        c=co.cursor()
        c.execute("select (Book_id) from Book_details")
        b=c.fetchall()
        S=len(b)
        m=[]
        for i in range (S):
            m.append(b[i][0])
        if e=='' or e1=='' or e2=='' or e3=='' or e4 =='' or e5=='':
            tk.messagebox.showinfo('warning','please fill up all boxes')
        elif e in m:
            tk.messagebox.showinfo('warning','Id Alredy Exist')
        else:
            self.co=mysql.connector.connect(host='localhost',user='root',password=pasw,database=db)
            self.c=self.co.cursor()
            self.c.execute("insert into Book_details (Book_id,Book_name,Author_name,Catagory,Publication,Cost_of_Book) VALUES ({},'{}','{}','{}','{}','{}')".format(e,e1,e2,e3,e4,e5))
            self.co.commit()
            self.co.close()
            tk.messagebox.showinfo('successful','stored in database')
    def click15(self):
        home_page(root)
    def click16(self):
        book_page(root)
#=======================================TEACH_UPDATE==========================#     
class teach_update:
    def __init__(self,root):
        self.root =Frame(root,height=768,width=1360).pack()
        self.user1=StringVar()
        self.user2=StringVar()
        self.user3=StringVar()
        self.user4=IntVar()
        self.user5=StringVar()   
        self.a=PhotoImage(file = "back2.png")    
        self.l=Label(root,image=self.a,text='DAWN LIBRARY').place(x=0,y=0)
        self.b=PhotoImage(file = "lib1.png")    
        self.l1=label=Label(root,image=self.b,text='DAWN LIBRARY').place(x=540,y=0)
        self.l3=Label(root,text='Teacher ID:',font=('Times',13),bg='Black',fg='white').place(x=630,y=200)
        self.e2=Entry(root,width=30,textvar=self.user1).place(x=730,y=200)
        self.l4=Label(root,text='Teacher Name :',font=('Times',13),bg='Black',fg='white').place(x=610,y=250)
        self.e3=Entry(root,width=30,textvar=self.user2).place(x=730,y=250)
        self.l5=Label(root,text='Date Of Birth:',font=('Times',13),bg='Black',fg='white').place(x=620,y=300)
        self.e4=Entry(root,width=30,textvar=self.user3).place(x=730,y=300)
        self.l6=Label(root,text='Phone No.:',font=('Times',13),bg='Black',fg='white').place(x=630,y=350)
        self.e5=Entry(root,width=30,textvar=self.user4).place(x=730,y=350)
        self.l7=Label(root,text='Accedmic Year :',font=('Times',13),bg='Black',fg='white').place(x=605,y=400)
        self.e6=Entry(root,width=30,textvar=self.user5).place(x=730,y=400)
        self.c=Button(root,width=7,height=2,text='Submit',font=10,bg='Black',fg='White',command=self.click17).place(x=750,y=450)
        self.q=PhotoImage(file = "back1.png")
        self.label=Button(self.root,image=self.q,command=self.click19).place(x=45,y=0)
        self.w=PhotoImage(file = "home1.png")
        self.label2=Button(self.root,image=self.w,command=self.click18).place(x=0,y=0)
    def click17(self):
        e1=self.user1.get()
        e2=self.user2.get()
        e3=self.user3.get()
        e4=self.user4.get()
        e5=self.user5.get()
        co=mysql.connector.connect(host='localhost',user='root',password=pasw,database=db)
        c=co.cursor()
        c.execute("select (Book_id) from Book_details")
        b=c.fetchall()
        S=len(b)
        m=[]
        for i in range (S):
            m.append(b[i][0])
        if  e1=='' or e2=='' or e3=='' or e4 =='' or e5=='':
            tk.messagebox.showinfo('warning','please fill up all boxes')
        elif e1 in m:
            tk.messagebox.showinfo('warning','Id Alredy Exist!!!')
        else:
            self.co=mysql.connector.connect(host='localhost',user='root',password=pasw,database=db)
            self.c=self.co.cursor()
            self.c.execute("insert into teachers_info (Teacher_id,Name,D_O_B,phone_no,Accadmic_year) VALUES ('{}','{}','{}',{},'{}')".format(e1,e2,e3,e4,e5))
            self.co.commit()
            self.co.close()
            tk.messagebox.showinfo('successful','stored in database')
    def click18(self):
        home_page(root)
    def click19(self):  
        teachers_page(root)
#==================================BOOK_SEARCH=============================#
class book_search:
    def __init__(self,root):
        self.user=StringVar()
        self.root=Frame(root,width=1360,height=768)
        self.b=PhotoImage(file = "search2.png")
        self.label=Label(root,image=self.b).place(x=0,y=0)
        self.label2=Label(root,text="SEARCH BOOK DETAILS",font=("times",31),bg="black",fg="white").place(x=360,y=10)
        self.e1=Entry(root,width=30,textvar=self.user,bg="black",fg="white").place(x=774,y=250)
        self.b1=Button(root,width=10,bg="black",fg="white",text="search",command=self.click).place(x=830,y=288)
        self.q=PhotoImage(file = "back1.png")
        self.label=Button(root,image=self.q,command=self.clickh9).place(x=45,y=0)
        self.w=PhotoImage(file = "home1.png")
        self.label2=Button(root,image=self.w,command=self.clickh8).place(x=0,y=0)
    def clickh8(self):
        home_page(root)
    def clickh9(self):  
        book_page(root)    
    def clickh19(self):  
        book_search(root)    
    def click(self):
        self.d=self.user.get()
        self.co=mysql.connector.connect(host='localhost',user='root',password=pasw,database=db)
        self.c=self.co.cursor()
        self.s="select * from Book_details where Book_id="+str(self.d)
        self.g=self.c.execute(self.s)
        self.q=self.c.fetchall()
        print(self.q)
        if self.q==[]:
            tk.messagebox.showinfo('sorry','not found in database')
        else:
            r1=self.q[0][0]
            r2=self.q[0][1]
            r3=self.q[0][2]
            r4=self.q[0][3]
            r5=self.q[0][4]
            r6=self.q[0][5]
            self.root=Frame(root,width=460,height=668).pack()
            self.d=PhotoImage(file = "back2.png")
            self.l1=Label(root,image=self.d).place(x=0,y=0)
            self.label=Label(root,text="BOOK INFORMATION",font=('Times',40),bg="light blue").place(x=350,y=20)
            self.q=PhotoImage(file = "back1.png")
            self.label=Button(root,image=self.q,command=self.clickh19).place(x=45,y=0)
            self.w=PhotoImage(file = "home1.png")
            self.label2=Button(root,image=self.w,command=self.clickh8).place(x=0,y=0)
            self.label=Label(root,text="BOOK_ID       :"+str(r1),font=('Times',16),bg="light blue").place(x=500,y=150)
            self.label=Label(root,text="BOOK_NAME      :"+str(r2),font=('Times',16)).place(x=500,y=200)
            self.label=Label(root,text="Author_name      :"+str(r3),font=('Times',16)).place(x=500,y=250)
            self.label=Label(root,text="Catagory        :"+str(r4),font=('Times',16)).place(x=500,y=300)
            self.label=Label(root,text="Publication  :"+str(r5),font=('Times',16)).place(x=500,y=350)
            self.label=Label(root,text="Cost_of_Book   :"+str(r6),font=('Times',16)).place(x=500,y=400)
            self.b1=Button(root,width=10,bg="black",fg="white",text="Delete",command=self.click20).place(x=580,y=470)
    def click20(self):
        self.d=self.user.get()
        self.co=mysql.connector.connect(host='localhost',user='root',password=pasw,database=db)
        self.c=self.co.cursor()
        self.s="delete from book_details where Book_id="+str(self.d)
        self.g=self.c.execute(self.s)
        self.co.commit()
        self.co.close()
        tk.messagebox.showinfo('successful','Deleted from database')
#==========================================STU_SEARCH===========================#        
class stu_search:
    def __init__(self,root):
        self.root=Frame(root,width=1360,height=768)
        self.user=StringVar()
        self.b=PhotoImage(file = "search2.png")
        self.label=Label(root,image=self.b).place(x=0,y=0)
        self.label2=Label(root,text="SEARCH STUDENT DETAILS",font=("times",31),bg="black",fg="white").place(x=360,y=10)
        self.e1=Entry(root,width=30,textvar=self.user,bg="black",fg="white").place(x=774,y=250)
        self.b1=Button(root,width=10,bg="black",fg="white",text="search",command=self.click21).place(x=830,y=288)
        self.q=PhotoImage(file = "back1.png")
        self.label=Button(root,image=self.q,command=self.click39).place(x=45,y=0)
        self.w=PhotoImage(file = "home1.png")
        self.label2=Button(root,image=self.w,command=self.click38).place(x=0,y=0)
    def click38(self):
        home_page(root)
    def click9(self):
        stu_search(root)
    def click39(self):  
        stu_page(root)    
    def click21(self):
        self.d=self.user.get()
        self.co=mysql.connector.connect(host='localhost',user='root',password=pasw,database=db)
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
            self.l1=Label(root,image=self.d).place(x=0,y=0)
            self.label=Label(root,text="STUDENT'S INFORMATION",font=('Times',40),bg="light blue").place(x=350,y=20)
            self.q=PhotoImage(file = "back1.png")
            self.label=Button(root,image=self.q,command=self.click9).place(x=45,y=0)
            self.w=PhotoImage(file = "home1.png")
            self.label2=Button(root,image=self.w,command=self.click38).place(x=0,y=0)
            self.label=Label(root,text="STU_ID       :"+str(r1),font=('Times',16),bg="light blue").place(x=500,y=150)
            self.label=Label(root,text="STU_NAME      :"+str(r2),font=('Times',16)).place(x=500,y=200)
            self.label=Label(root,text="Class        :"+str(r3),font=('Times',16)).place(x=500,y=250)
            self.label=Label(root,text="D_O_B         :"+str(r4),font=('Times',16)).place(x=500,y=300)
            self.label=Label(root,text="PHONE NO.     :"+str(r5),font=('Times',16)).place(x=500,y=350)
            self.label=Label(root,text="ACCM.YEAR    :"+str(r6),font=('Times',16)).place(x=500,y=400)
            self.b1=Button(root,width=10,bg="black",fg="white",text="Delete",command=self.click22).place(x=580,y=470)
    def click22(self):
        self.d=self.user.get()
        self.co=mysql.connector.connect(host='localhost',user='root',password=pasw,database=db)
        self.c=self.co.cursor()
        self.s="delete from stu_info1 where stu_id="+str(self.d)
        self.c.execute(self.s)
        self.co.commit()
        self.co.close()
        tk.messagebox.showinfo('successful','Deleted from database')
#======================================TEACH_SEARCH==============================#
class teach_search:
    def __init__(self,root):
        self.user=StringVar()
        self.root=Frame(root,width=1360,height=768)
        self.b=PhotoImage(file = "search2.png")
        self.label=Label(root,image=self.b).place(x=0,y=0)
        self.label2=Label(root,text="SEARCH TEACHER DETAILS",font=("times",31),bg="black",fg="white").place(x=360,y=10)
        self.e1=Entry(root,width=30,textvar=self.user,bg="black",fg="white").place(x=774,y=250)
        self.b1=Button(root,width=10,bg="black",fg="white",text="search",command=self.click23).place(x=830,y=288)
        self.q=PhotoImage(file = "back1.png")
        self.label=Button(root,image=self.q,command=self.click49).place(x=45,y=0)
        self.w=PhotoImage(file = "home1.png")
        self.label2=Button(root,image=self.w,command=self.click48).place(x=0,y=0)
    def click48(self):
        home_page(root)
    def click49(self):
        teachers_page(root)
    def click9(self):
        teach_search(root)
    def click23(self):
        self.d=self.user.get()
        self.co=mysql.connector.connect(host='localhost',user='root',password=pasw,database=db)
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
            self.l1=Label(root,image=self.d).place(x=0,y=0)
            self.label=Label(root,text="TEACHER'S INFORMATION",font=('Times',40),bg="light blue").place(x=350,y=20)
            self.q=PhotoImage(file = "back1.png")
            self.label=Button(root,image=self.q,command=self.click9).place(x=45,y=0)
            self.w=PhotoImage(file = "home1.png")
            self.label2=Button(root,image=self.w,command=self.click48).place(x=0,y=0)
            self.label=Label(root,text="TEACHER_ID       :"+str(r1),font=('Times',16),bg="light blue").place(x=500,y=150)
            self.label=Label(root,text="NAME      :"+str(r2),font=('Times',16)).place(x=500,y=200)
            self.label=Label(root,text="D_O_B         :"+str(r4),font=('Times',16)).place(x=500,y=250)
            self.label=Label(root,text="PHONE NO.     :"+str(r5),font=('Times',16)).place(x=500,y=300)
            self.label=Label(root,text="ACCM.YEAR    :"+str(r6),font=('Times',16)).place(x=500,y=350)
            self.b1=Button(root,width=10,bg="black",fg="white",text="Delete",command=self.click24).place(x=580,y=420)
    def click24(self):
        self.d=self.user.get()
        self.co=mysql.connector.connect(host='localhost',user='root',password=pasw,database=db)
        self.c=self.co.cursor()
        self.s="delete from teachers_info where Teacher_id="+str(self.d)
        self.g=self.c.execute(self.s)
        self.co.commit()
        self.co.close()
        tk.messagebox.showinfo('successful','Deleted from database')
#==============================ISSUE_BOOK===========================#      
class issue_book():
    def __init__(self,root):
        self.root =Frame(root,height=768,width=1360,bg='White').pack()
        self.user=StringVar()
        self.user2=StringVar()
        self.user3=StringVar()
        self.user4=StringVar()
        self.d=PhotoImage(file = "back2.png")
        self.l1=Label(root,image=self.d).place(x=0,y=0)
        self.l2=Label(root,text="Steudent ID:",font=('Times',13),bg='Black',fg='white').place(x=780,y=150) 
        self.e1=tk.Entry(root,width=30,textvar=self.user).place(x=875,y=150)
        self.l4=Label(root,text='Student Name:',font=('Times',13),bg='Black',fg='white').place(x=760,y=200)
        self.e3=tk.Entry(root,width=30,textvar=self.user3).place(x=875,y=250)
        self.l3=Label(root,text='BOOK ID:',font=('Times',13),bg='Black',fg='white').place(x=790,y=250) 
        self.l2=Label(root,text='BOOK NAME :',font=('Times',13),bg='Black',fg='white').place(x=755,y=300)
        self.label=Button(root,height=2,width=12,text="submit",font=("times",11),bg="black",fg="white",command=self.click27).place(x=900,y=350)
        self.label2=Button(root,height=1,width=7,text="search",font=("times",11),bg="black",fg="white",command=self.click25).place(x=980,y=188)
        self.label3=Button(root,height=1,width=7,text="search",font=("times",11),bg="black",fg="white",command=self.click26).place(x=980,y=290)
        self.q=PhotoImage(file = "back1.png")
        self.label5=Button(root,image=self.q,command=self.click59).place(x=45,y=0)
        self.w=PhotoImage(file = "home1.png")
        self.label2=Button(root,image=self.w,command=self.click58).place(x=0,y=0)
    def click58(self):
        home_page(root)
    def click59(self):  
        issue_page(root)    
    def click25(self):   
        self.p=self.user.get()
        co=mysql.connector.connect(host='localhost',user='root',password=pasw,database=db)
        c=co.cursor()
        c.execute("select (stu_id) from stu_info1")
        b=c.fetchall()
        S=len(b)
        m=[]
        for i in range (S):
            m.append(b[i][0])
        if self.p in m:
            self.co=mysql.connector.connect(host='localhost',user='root',password=pasw,database=db)
            self.c=self.co.cursor()
            self.n2="select (Name) from stu_info1 where stu_id="+str(self.p)
            self.q=self.c.execute(self.n2)
            self.f1=self.c.fetchall()
            self.d1=self.f1
            self.co.close()
            if self.d1==[]:
                tk.messagebox.showinfo('Sorry','Not Found In Database')
            else:     
                self.e2=tk.Label(root,text=self.d1,bg="white",font=("Times",12)).place(x=875,y=200)
        else:
            tk.messagebox.showinfo('WARNING','Invalid Id is Entered')
    def click26(self):
        self.p2=self.user3.get()
        co=mysql.connector.connect(host='localhost',user='root',password=pasw,database=db)
        c=co.cursor()
        c.execute("select (Book_id) from Book_details")
        b=c.fetchall()
        S=len(b)
        m=[]
        for i in range (S):
            m.append(b[i][0])
        if self.p2 in m:
            self.co=mysql.connector.connect(host='localhost',user='root',password=pasw,database=db)
            self.c=self.co.cursor()
            self.n1="select (Book_name) from book_details where Book_id="+str(self.p2)
            self.c.execute(self.n1)
            self.f2=self.c.fetchall()
            self.d2=self.f2
            self.co.close()
            if self.d1==[]:
                tk.messagebox.showinfo('Sorry','Not Found In Database')
            else:
                self.e5=tk.Label(root,text=self.d2,bg="white",font=("Times",12)).place(x=875,y=300)
        else:
          tk.messagebox.showinfo('Warning','Invalid Id is Entered')  
    def click27(self):
        g1=self.user.get()
        g2=self.d1[0][0]
        g3=self.user3.get()
        g4=self.d2[0][0]
        g5=str(date.today())
        g6=str(date.today() + timedelta(days=10))
        if g1=='' or g2==''or g3==''or g4=='':
            tk.messagebox.showinfo('warning','please fill up all boxes')
        else:
            print(g1,g2,g3,g4)
            self.co=mysql.connector.connect(host='localhost',user='root',password=pasw,database=db)
            self.c=self.co.cursor()
            self.s="insert into issue_details (Stu_Id,Stu_Name,Book_Id,Book_Name,issued_date,Return_date) VALUES ('{}','{}','{}','{}','{}','{}')".format(g1,g2,g3,g4,g5,g6)
            self.c.execute(self.s)
            self.co.commit()
            self.co.close()
            tk.messagebox.showinfo('successful','stored in database')
#==================================RETURN_BOOK=============================#
class return_book():
    def __init__(self,root):
        self.root =Frame(root,height=768,width=1360,bg='White').pack()
        self.user=StringVar()
        self.user2=StringVar()
        self.user3=StringVar()
        self.user4=StringVar()
        self.d=PhotoImage(file = "back2.png")
        self.l1=Label(root,image=self.d).place(x=0,y=0)
        self.l2=Label(root,text='Student ID:',font=('Times',13),bg='Black',fg='white').place(x=780,y=150) 
        self.e1=tk.Entry(root,width=30,textvar=self.user).place(x=875,y=150)
        self.l4=Label(root,text='Student Name:',font=('Times',13),bg='Black',fg='white').place(x=760,y=200)
        self.e3=tk.Entry(root,width=30,textvar=self.user3).place(x=875,y=250)
        self.l3=Label(root,text='BOOK ID:',font=('Times',13),bg='Black',fg='white').place(x=790,y=250) 
        self.l5=Label(root,text='issued_date:',font=('Times',13),bg='Black',fg='white').place(x=760,y=350)
        self.l5=Label(root,text='return_date:',font=('Times',13),bg='Black',fg='white').place(x=760,y=400)
        self.l2=Label(root,text='BOOK NAME :',font=('Times',13),bg='Black',fg='white').place(x=755,y=300)
        self.label=Button(root,height=1,width=7,text="search",font=("times",11),bg="black",fg="white",command=self.click31).place(x=1000,y=360)
        self.label2=Button(root,height=1,width=7,text="search",font=("times",11),bg="black",fg="white",command=self.click29).place(x=1000,y=200)
        self.label3=Button(root,height=1,width=7,text="search",font=("times",11),bg="black",fg="white",command=self.click30).place(x=1000,y=280)
        self.label4=Button(root,height=1,width=7,text="submit",font=("times",11),bg="black",fg="white",command=self.click311).place(x=900,y=450)
        self.q=PhotoImage(file = "back1.png")
        self.label=Button(root,image=self.q,command=self.click69).place(x=45,y=0)
        self.w=PhotoImage(file = "home1.png")
        self.label2=Button(root,image=self.w,command=self.click68).place(x=0,y=0)
    def click68(self):
        home_page(root)
    def click69(self):  
        issue_page(root)    
    def click29(self):   
        self.p=self.user.get()
        self.co=mysql.connector.connect(host='localhost',user='root',password=pasw,database=db)
        self.c=self.co.cursor()
        self.n2="select (Stu_Name) from issue_details where stu_id="+str(self.p)
        self.q=self.c.execute(self.n2)
        self.f1=self.c.fetchall()
        self.d1=self.f1
        self.co.close()
        if self.d1==[]:
             tk.messagebox.showinfo('Sorry','Not Found In Database')
        else:     
            self.e2=tk.Label(root,text=self.d1,bg="white",font=("Times",12)).place(x=875,y=200)
    def click30(self):
        self.p2=self.user3.get()
        self.co=mysql.connector.connect(host='localhost',user='root',password=pasw,database=db)
        self.c=self.co.cursor()
        self.n1="select (Book_Name) from issue_details where Book_id="+str(self.p2)
        self.c.execute(self.n1)
        self.f2=self.c.fetchall()
        self.d2=self.f2
        self.co.close()
        if self.d2==[]:
             tk.messagebox.showinfo('Sorry','Not Found In Database')
        else:
            self.e5=tk.Label(root,text=self.d2,bg="white",font=("Times",12)).place(x=875,y=300)
    def click31(self):
        self.p2=self.user3.get()
        self.co=mysql.connector.connect(host='localhost',user='root',password=pasw,database=db)
        self.c=self.co.cursor()
        self.n1="select * from issue_details where Book_Id="+str(self.p2)
        self.c.execute(self.n1)
        self.f2=self.c.fetchall()
        self.d3=self.f2
        self.co.close()
        if self.d1==[]:
             tk.messagebox.showinfo('Sorry','Not Found In Database')
        else:
            self.e6=tk.Label(root,text=self.d3[0][4],bg="white",font=("Times",12)).place(x=875,y=350)
            self.e7=tk.Label(root,text=self.d3[0][5],bg="white",font=("Times",12)).place(x=875,y=400)
    def click311(self):
        self.p2=self.user3.get()
        self.co=mysql.connector.connect(host='localhost',user='root',password=pasw,database=db)
        self.c=self.co.cursor()
        self.n1="delete from issue_details where Book_Id="+str(self.p2)
        self.c.execute(self.n1)
        self.co.commit()        
        self.co.close()
        tk.messagebox.showinfo('THANK YOU!!','THANK U FOR RETURNING SAFELY')

#===============================student_table=========================================#        
class stu_table():
    def __init__(self,root):
        self.root = Tk()
        self.root.title("STU_TABLE")
        self.root.geometry("1600x1000+0+0")
        mainlabel =Label(self. root, text="STUDENT INFO", font=("times new roman", 35), bg="MediumOrchid2")
        mainlabel.pack(side=TOP, fill=X)
        chat1 =ttk.Treeview(self.root,height=20 , columns=('Stu_Id', 'Stu_Name', 'Class',"DATE_of_birth",'Phone_no','Acc._year'), selectmode="extended")
        chat1.heading('#0', text='Stu_Id', anchor=CENTER)
        chat1.heading('#1', text='Stu_Name', anchor=CENTER)
        chat1.heading('#2', text='Class', anchor=CENTER)
        chat1.heading('#3', text="D_O_B", anchor=CENTER)
        chat1.heading('#4', text="Phone_no.", anchor=CENTER)
        chat1.heading('#5', text="Acc._year", anchor=CENTER)
        chat1.column('#0', stretch=YES, minwidth=50, width=70)
        chat1.column('#1', stretch=YES, minwidth=50, width=150)
        chat1.column('#2', stretch=YES, minwidth=50, width=50)
        chat1.column('#3', stretch=YES, minwidth=50, width=70)
        chat1.column('#4', stretch=YES, minwidth=50, width=120)
        chat1.column('#5', stretch=YES, minwidth=50, width=70)
        vsb = ttk.Scrollbar(self.root, orient="vertical", command=chat1.yview)
        vsb.place(x=1050, y=170, height=400 + 20)
        chat1.configure(yscrollcommand=vsb.set)
        chat1.place(x=400, y=170)
        ttk.Style().configure("Treeview", background="#383838", foreground="coral1")
        ttk.Style().configure("Treeview.heading", background="blue", foreground="palevioletRed1")
        self.root.configure(background="white")
        co=mysql.connector.connect(host='localhost',user='root',password=pasw,database=db)
        c=co.cursor()
        c.execute('SELECT * FROM stu_info1')
        for row in c.fetchall():
            chat1.insert('', 0, text=row[0], values=(row[1], row[2], row[3],row[4],row[5]))     
#=========================================Book_Table==========================================#
class book_table():
    def __init__(self,root):
        self.root = Tk()
        self.root.title("Book_table")
        self.root.geometry("1600x1000+0+0")
        mainlabel =Label(self. root, text="BOOK INFO", font=("times new roman", 35), bg="MediumOrchid2")
        mainlabel.pack(side=TOP, fill=X)
        chat1 =ttk.Treeview(self.root,height=20 , columns=('Stu_Id', 'Stu_Name', 'Class',"DATE_of_birth",'Phone_no','Acc._year'), selectmode="extended")
        chat1.heading('#0', text='Book_Id', anchor=CENTER)
        chat1.heading('#1', text='Book_Name', anchor=CENTER)
        chat1.heading('#2', text='Author_name ', anchor=CENTER)
        chat1.heading('#3', text="Catagory", anchor=CENTER)
        chat1.heading('#4', text="Publication", anchor=CENTER)
        chat1.heading('#5', text="Cost_of_Book", anchor=CENTER)
        chat1.column('#0', stretch=YES, minwidth=50, width=70)
        chat1.column('#1', stretch=YES, minwidth=50, width=200)
        chat1.column('#2', stretch=YES, minwidth=50, width=100)
        chat1.column('#3', stretch=YES, minwidth=50, width=100)
        chat1.column('#4', stretch=YES, minwidth=50, width=120)
        chat1.column('#5', stretch=YES, minwidth=50, width=70)
        vsb = ttk.Scrollbar(self.root, orient="vertical", command=chat1.yview)
        vsb.place(x=1060, y=170, height=400 + 20)
        chat1.configure(yscrollcommand=vsb.set)
        chat1.place(x=400, y=170)
        ttk.Style().configure("Treeview", background="#383838", foreground="coral1")
        ttk.Style().configure("Treeview.heading", background="blue", foreground="palevioletRed1")
        self.root.configure(background="white")
        co=mysql.connector.connect(host='localhost',user='root',password=pasw,database=db)
        c=co.cursor()
        c.execute('SELECT * FROM book_details')
        for row in c.fetchall():
            chat1.insert('', 0, text=row[0], values=(row[1], row[2], row[3],row[4],row[5]))
#==========================================Issue_Table================================#
class issue_table():
    def __init__(self,root):
        self.root = Tk()
        self.root.title("Issue_table")
        self.root.geometry("1600x1000+0+0")
        mainlabel =Label(self. root, text="ISSUE INFO", font=("times new roman", 35), bg="MediumOrchid2")
        mainlabel.pack(side=TOP, fill=X)
        chat1 =ttk.Treeview(self.root,height=20 , columns=('Stu_Id', 'Stu_Name', 'Class',"DATE_of_birth",'Phone_no','Acc._year'), selectmode="extended")
        chat1.heading('#0', text='Stu_Id', anchor=CENTER)
        chat1.heading('#1', text='Stu_Name', anchor=CENTER)
        chat1.heading('#2', text='Book_Id ', anchor=CENTER)
        chat1.heading('#3', text="Book_Name", anchor=CENTER)
        chat1.heading('#4', text="issued_date", anchor=CENTER)
        chat1.heading('#5', text="Return_date", anchor=CENTER)
        chat1.column('#0', stretch=YES, minwidth=50, width=70)
        chat1.column('#1', stretch=YES, minwidth=50, width=200)
        chat1.column('#2', stretch=YES, minwidth=50, width=100)
        chat1.column('#3', stretch=YES, minwidth=50, width=100)
        chat1.column('#4', stretch=YES, minwidth=50, width=120)
        chat1.column('#5', stretch=YES, minwidth=50, width=70)
        vsb = ttk.Scrollbar(self.root, orient="vertical", command=chat1.yview)
        vsb.place(x=1060, y=170, height=400 + 20)
        chat1.configure(yscrollcommand=vsb.set)
        chat1.place(x=400, y=170)
        ttk.Style().configure("Treeview", background="#383838", foreground="coral1")
        ttk.Style().configure("Treeview.heading", background="blue", foreground="palevioletRed1")
        self.root.configure(background="white")
        co=mysql.connector.connect(host='localhost',user='root',password=pasw,database=db)
        c=co.cursor()
        c.execute('SELECT * FROM issue_details')
        for row in c.fetchall():
            chat1.insert('', 0, text=row[0], values=(row[1], row[2], row[3],row[4],row[5]))  
#=============================================T_issue_Table================================#
class T_issue_table():
    def __init__(self,root):
        self.root = Tk()
        self.root.title("T_issue table")
        self.root.geometry("1600x1000+0+0")
        mainlabel =Label(self. root, text="Teacher Issue Info", font=("times new roman", 35), bg="MediumOrchid2")
        mainlabel.pack(side=TOP, fill=X)
        chat1 =ttk.Treeview(self.root,height=20 , columns=('Stu_Id', 'Stu_Name', 'Class',"DATE_of_birth",'Phone_no','Acc._year'), selectmode="extended")
        chat1.heading('#0', text='Teacher_Id', anchor=CENTER)
        chat1.heading('#1', text='Teacher_Name', anchor=CENTER)
        chat1.heading('#2', text='Book_Id ', anchor=CENTER)
        chat1.heading('#3', text="Book_Name", anchor=CENTER)
        chat1.heading('#4', text="issued_date", anchor=CENTER)
        chat1.heading('#5', text="Return_date", anchor=CENTER)
        chat1.column('#0', stretch=YES, minwidth=50, width=70)
        chat1.column('#1', stretch=YES, minwidth=50, width=200)
        chat1.column('#2', stretch=YES, minwidth=50, width=100)
        chat1.column('#3', stretch=YES, minwidth=50, width=100)
        chat1.column('#4', stretch=YES, minwidth=50, width=120)
        chat1.column('#5', stretch=YES, minwidth=50, width=70)
        vsb = ttk.Scrollbar(self.root, orient="vertical", command=chat1.yview)
        vsb.place(x=1060, y=170, height=400 + 20)
        chat1.configure(yscrollcommand=vsb.set)
        chat1.place(x=400, y=170)
        ttk.Style().configure("Treeview", background="#383838", foreground="coral1")
        ttk.Style().configure("Treeview.heading", background="blue", foreground="palevioletRed1")
        self.root.configure(background="white")
        co=mysql.connector.connect(host='localhost',user='root',password=pasw,database=db)
        c=co.cursor()
        c.execute('SELECT * FROM T_issue_details')
        for row in c.fetchall():
            chat1.insert('', 0, text=row[0], values=(row[1], row[2], row[3],row[4],row[5])) 
#========================================Teacher_Tabel=================================#
class teacher_table():
    def __init__(self,root):
        self.root = Tk()
        self.root.title("Teacher_table")
        self.root.geometry("1600x1000+0+0")
        mainlabel =Label(self. root, text="TEACHER INFO", font=("times new roman", 35), bg="MediumOrchid2")
        mainlabel.pack(side=TOP, fill=X)
        chat1 =ttk.Treeview(self.root,height=20 , columns=('Teacher_Id', 'Teacher_Name',"D_O_B",'Phone_no','Acc._year'), selectmode="extended")
        chat1.heading('#0', text='Teacher_Id', anchor=CENTER)
        chat1.heading('#1', text='Teacher_Name', anchor=CENTER)
        chat1.heading('#2', text="D_O_B", anchor=CENTER)
        chat1.heading('#3', text="Phone_no.", anchor=CENTER)
        chat1.heading('#4', text="Acc._year", anchor=CENTER)
        chat1.column('#0', stretch=YES, minwidth=50, width=70)
        chat1.column('#1', stretch=YES, minwidth=50, width=150)
        chat1.column('#2', stretch=YES, minwidth=50, width=70)
        chat1.column('#3', stretch=YES, minwidth=50, width=70)
        chat1.column('#4', stretch=YES, minwidth=50, width=120)
        vsb = ttk.Scrollbar(self.root, orient="vertical", command=chat1.yview)
        vsb.place(x=1050, y=170, height=400 + 20)
        chat1.configure(yscrollcommand=vsb.set)
        chat1.place(x=400, y=170)
        ttk.Style().configure("Treeview", background="#383838", foreground="coral1")
        ttk.Style().configure("Treeview.heading", background="blue", foreground="palevioletRed1")
        self.root.configure(background="white")
        co=mysql.connector.connect(host='localhost',user='root',password=pasw,database=db)
        c=co.cursor()
        c.execute('SELECT * FROM teachers_info')
        for row in c.fetchall():
            chat1.insert('', 0, text=row[0], values=(row[1], row[2], row[3],row[4]))     
#==========================================T_issue_book============================#
class T_issue_book():
    def __init__(self,master):
        self.master = master
        self.root =Frame(master,height=768,width=1360,bg='White').pack()
        self.user=StringVar()
        self.user2=StringVar()
        self.user3=StringVar()
        self.user4=StringVar()
        self.d=PhotoImage(file = "back2.png")
        self.l1=Label(root,image=self.d).place(x=0,y=0)
        self.l2=Label(root,text='Teacher ID:',font=('Times',13),bg='Black',fg='white').place(x=780,y=150) 
        self.e1=tk.Entry(root,width=30,textvar=self.user).place(x=875,y=150)
        self.l4=Label(root,text='Teacher Name:',font=('Times',13),bg='Black',fg='white').place(x=760,y=200)
        self.e3=tk.Entry(root,width=30,textvar=self.user3).place(x=875,y=250)
        self.l3=Label(root,text='BOOK ID:',font=('Times',13),bg='Black',fg='white').place(x=790,y=250) 
        self.l2=Label(root,text='BOOK NAME :',font=('Times',13),bg='Black',fg='white').place(x=755,y=300)
        self.label=Button(root,height=2,width=12,text="submit",font=("times",11),bg="black",fg="white",command=self.click27).place(x=900,y=350)
        self.label2=Button(root,height=1,width=7,text="search",font=("times",11),bg="black",fg="white",command=self.click25).place(x=980,y=188)
        self.label3=Button(root,height=1,width=7,text="search",font=("times",11),bg="black",fg="white",command=self.click26).place(x=980,y=290)
        self.q=PhotoImage(file = "back1.png")
        self.label5=Button(root,image=self.q,command=self.click59).place(x=45,y=0)
        self.w=PhotoImage(file = "home1.png")
        self.label2=Button(root,image=self.w,command=self.click58).place(x=0,y=0)
    def click58(self):
        home_page(root)
    def click59(self):  
        issue_page(root)    
    def click25(self):   
        self.p=self.user.get()
        co=mysql.connector.connect(host='localhost',user='root',password=pasw,database=db)
        c=co.cursor()
        c.execute("select (stu_id) from stu_info1")
        b=c.fetchall()
        S=len(b)
        m=[]
        for i in range (S):
            m.append(b[i][0])
        if self.p in m:    
            self.co=mysql.connector.connect(host='localhost',user='root',password=pasw,database=db)
            self.c=self.co.cursor()
            self.n2="select (Name) from teachers_info where Teacher_id="+str(self.p)
            self.q=self.c.execute(self.n2)
            self.f1=self.c.fetchall()
            self.d1=self.f1
            self.co.close()
            if self.d1==[]:
                tk.messagebox.showinfo('Sorry','Not Found In Database')
            else:
                self.e2=tk.Label(self.root,text=self.d1,bg="white",font=("Times",12)).place(x=875,y=200)
        else:
            tk.messagebox.showinfo('Warning','Invalid Id is Entered')
    def click26(self):
        self.p2=self.user3.get()
        co=mysql.connector.connect(host='localhost',user='root',password=pasw,database=db)
        c=co.cursor()
        c.execute("select (stu_id) from stu_info1")
        b=c.fetchall()
        S=len(b)
        m=[]
        for i in range (S):
            m.append(b[i][0])
        if self.p2 in m:    
            self.co=mysql.connector.connect(host='localhost',user='root',password=pasw,database=db)
            self.c=self.co.cursor()
            self.n1="select (Book_name) from book_details where Book_id="+str(self.p2)
            self.c.execute(self.n1)
            self.f2=self.c.fetchall()
            self.d2=self.f2
            self.co.close()
            if self.d1==[]:
                 tk.messagebox.showinfo('Sorry','Not Found In Database')
            else:
                self.e5=tk.Label(root,text=self.d2,bg="white",font=("Times",12)).place(x=875,y=300)
        else:
             tk.messagebox.showinfo('Warning','Invalid Id is Entered')
    def click27(self):
        g1=self.user.get()
        g2=self.d1[0][0]
        g3=self.user3.get()
        g4=self.d2[0][0]
        g5=str(date.today())
        g6=str(date.today() + timedelta(days=10))
        if g1=='' or g2==''or g3==''or g4=='':
            tk.messagebox.showinfo('warning','please fill up all boxes')
        else:
            print(g1,g2,g3,g4)
            self.co=mysql.connector.connect(host='localhost',user='root',password=pasw,database=db)
            self.c=self.co.cursor()
            self.s="insert into T_issue_details (Teacher_Id,Teacher_Name,Book_Id,Book_Name,issued_date,Return_date) VALUES ('{}','{}','{}','{}','{}','{}')".format(g1,g2,g3,g4,g5,g6)
            self.c.execute(self.s)
            self.co.commit()
            self.co.close()
            tk.messagebox.showinfo('successful','stored in database')
#=================================T_return_book=========================#
class T_return_book():
    def __init__(self,master):
        self.master = master
        self.root =Frame(master,height=768,width=1360,bg='White').pack()
        self.user=StringVar()
        self.user2=StringVar()
        self.user3=StringVar()
        self.user4=StringVar()
        self.d=PhotoImage(file = "back2.png")
        self.l1=Label(root,image=self.d).place(x=0,y=0)
        self.l2=Label(root,text='Teacher ID:',font=('Times',13),bg='Black',fg='white').place(x=780,y=150) 
        self.e1=tk.Entry(root,width=30,textvar=self.user).place(x=875,y=150)
        self.l4=Label(root,text='Teacher Name:',font=('Times',13),bg='Black',fg='white').place(x=760,y=200)
        self.e3=tk.Entry(root,width=30,textvar=self.user3).place(x=875,y=250)
        self.l3=Label(root,text='BOOK ID:',font=('Times',13),bg='Black',fg='white').place(x=790,y=250) 
        self.l5=Label(root,text='issued_date:',font=('Times',13),bg='Black',fg='white').place(x=760,y=350)
        self.l5=Label(root,text='return_date:',font=('Times',13),bg='Black',fg='white').place(x=760,y=400)
        self.l2=Label(root,text='BOOK NAME :',font=('Times',13),bg='Black',fg='white').place(x=755,y=300)
        self.label=Button(root,height=1,width=7,text="search",font=("times",11),bg="black",fg="white",command=self.click31).place(x=1000,y=360)
        self.label2=Button(root,height=1,width=7,text="search",font=("times",11),bg="black",fg="white",command=self.click29).place(x=1000,y=200)
        self.label3=Button(root,height=1,width=7,text="search",font=("times",11),bg="black",fg="white",command=self.click30).place(x=1000,y=280)
        self.label4=Button(root,height=1,width=7,text="submit",font=("times",11),bg="black",fg="white",command=self.click300).place(x=900,y=450)
        self.q=PhotoImage(file = "back1.png")
        self.label=Button(root,image=self.q,command=self.click69).place(x=45,y=0)
        self.w=PhotoImage(file = "home1.png")
        self.label2=Button(root,image=self.w,command=self.click68).place(x=0,y=0)
    def click68(self):
        home_page(root)
    def click69(self):
        issue_page(root)    
    def click29(self):   
        self.p=self.user.get()
        self.co=mysql.connector.connect(host='localhost',user='root',password=pasw,database=db)
        self.c=self.co.cursor()
        self.n2="select (Teacher_Name) from T_issue_details where Teacher_id="+str(self.p)
        self.q=self.c.execute(self.n2)
        self.f1=self.c.fetchall()
        self.d1=self.f1
        self.co.close()
        if self.d1==[]:
             tk.messagebox.showinfo('Sorry','Not Found In Database')
        else:     
            self.e2=tk.Label(root,text=self.d1,bg="white",font=("Times",12)).place(x=875,y=200)
    def click30(self):
        self.p2=self.user3.get()
        self.co=mysql.connector.connect(host='localhost',user='root',password=pasw,database=db)
        self.c=self.co.cursor()
        self.n1="select (Book_Name) from T_issue_details where Book_id="+str(self.p2)
        self.c.execute(self.n1)
        self.f2=self.c.fetchall()
        self.d2=self.f2
        self.co.close()
        if self.d2==[]:
             tk.messagebox.showinfo('Sorry','Not Found In Database')
        else:
            self.e5=tk.Label(root,text=self.d2,bg="white",font=("Times",12)).place(x=875,y=300)
    def click300(self):
        self.p2=self.user3.get()
        self.co=mysql.connector.connect(host='localhost',user='root',password=pasw,database=db)
        self.c=self.co.cursor()
        self.n1='delete from T_issue_details where Book_id='+str(self.p2)
        self.c.execute(self.n1)
        self.co.commit()
        self.co.close()
        tk.messagebox.showinfo('THANK YOU!!','THANK U FOR RETURNING SAFELY')
    def click31(self):
        self.p2=self.user3.get()
        self.co=mysql.connector.connect(host='localhost',user='root',password=pasw,database=db)
        self.c=self.co.cursor()
        self.n1="select * from issue_details where Book_Id="+str(self.p2)
        self.c.execute(self.n1)
        self.f2=self.c.fetchall()
        self.d3=self.f2
        self.co.close()
        
        if self.d3==[]:
             tk.messagebox.showinfo('Sorry','Not Found In Database')
        else:
            self.e6=tk.Label(root,text=self.d3[0][4],bg="white",font=("Times",12)).place(x=875,y=350)
            self.e7=tk.Label(root,text=self.d3[0][5],bg="white",font=("Times",12)).place(x=875,y=400)
#===================================C_issue_book===================================#                
class c_issue_book():
    def __init__(self,root):
        root=Tk()
        root.configure(bg='Black')
        self.label=Button(root,text='Issue To Teacher',bg="Blue",command=self.ck).place(x=45,y=0)
        self.label3=Button(root,text='Issue To Student',bg="Blue",command=self.ck2).place(x=45,y=50)
    def ck(self):
        T_issue_book(root)
    def ck2(self):
        issue_book(root)
#===================================C_return_book===================================#        
class c_return_book():
    def __init__(self,root):
        root=Tk()
        root.configure(bg='Black')
        self.label=Button(root,text='''Return Teacher's Book''',bg="Blue",command=self.ck).place(x=45,y=0)
        self.label3=Button(root,text='''Return Student's Book''',bg="Blue",command=self.ck2).place(x=45,y=50)
    def ck(self):
        T_return_book(root)
    def ck2(self):
        return_book(root)        
#===================================C_issue_table====================================#
class c_issue_table():
    def __init__(self,root):
        root=Tk()
        root.configure(bg='Black')
        self.label=Button(root,text='''Teacher's Issue Details''',bg="Blue",command=self.ck).place(x=45,y=0)
        self.label3=Button(root,text='''Student's Issue Details''',bg="Blue",command=self.ck2).place(x=45,y=50)
    def ck(self):
        T_issue_table(root)
    def ck2(self):
        issue_table(root)
#==================================login========================================#        
class login():
    def __init__(self,root):
        self.root =Frame(root,height=166,width=240,bg='White').pack()

        self.d=PhotoImage(file = "rss.png")
        self.l1=Label(root,image=self.d).place(x=0,y=0)
        self.user=StringVar()
        self.user2=StringVar()
        l2=Label(root,text='USER NAME:',font=('Times',10),bg='Black',fg='white').place(x=0,y=50) 
        e1=tk.Entry(root,width=30,textvar=self.user).place(x=85,y=50)
        l4=Label(root,text='PASSWORD:',font=('Times',10),bg='Black',fg='white').place(x=0,y=80)
        e2=tk.Entry(root,width=30,textvar=self.user2).place(x=85,y=80)
        label=Button(root,text='Login',bg="BLACK",fg='White',command=self.log).place(x=100,y=120)
    def log(self):
        USER='dawnlibrary'
        password='dawn123'
        e1=self.user.get()
        e2=self.user2.get()
        if e1==USER and e2==password:
            home_page(root)
        else:
            tk.messagebox.showinfo('WARNING!','INVALID USER ID OR PASSWORD')
#=================main_fiunction==========================#
root=Tk()
login(root)
root.geometry("+80+10")
root.resizable(False, False)
root.mainloop()
