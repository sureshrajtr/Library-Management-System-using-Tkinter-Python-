from tkinter import *
import tkinter as tk
from tkinter import messagebox
import mysql.connector
from tkinter import ttk
co=mysql.connector.connect(host='localhost',user='root',password='12345678')
c=co.cursor()
c.execute("create database IF NOT exists School_M_S")
co.close()
co=mysql.connector.connect(host='localhost',user='root',password='12345678',database='school_m_s')
c=co.cursor()
c.execute("CREATE TABLE IF NOT EXISTS stu_info(stu_id varchar(15) UNIQUE,Name varchar(50),class varchar(50),D_O_B varchar(50),phone_no BIGINT,Father_Name varchar(10))")
c.execute("CREATE TABLE IF NOT EXISTS teachers_info(Teacher_id varchar(10)UNIQUE,Name varchar(50),D_O_B varchar(50),phone_no BIGINT)")
c.execute("CREATE TABLE IF NOT EXISTS fees_info(Stu_id varchar(10)UNIQUE,Name varchar(50),Class varchar(50),Total_fees integer(10),Balance_fees integer(10))")
c.execute("CREATE TABLE IF NOT EXISTS driver_info(Driver_id varchar(10),Name varchar(50),D_O_B varchar(10),phone_no BIGINT)")
c.execute("CREATE TABLE IF NOT EXISTS bus_info(Bus_no varchar(10),driver_name varchar(50),Route varchar(60),registration_no varchar(15))")
co.close()


class home_page:
    def __init__(self,root):
        self.root =Frame(root,height=768,width=1360).pack()
        
        self.b=PhotoImage(file = "school.png")
        self.label=Label(root,image=self.b,text='DAWN LIBRARY').place(x=0,y=0)
        self.s=PhotoImage(file = "stu1.png")
        self.b2=Button(root,command=self.click,image=self.s).place(x=200,y=243)
        self.i=PhotoImage(file = "teacher.png")
        self.b3=Button(root,text='click me',image=self.i,command=self.click1).place(x=550,y=243)
        self.r=PhotoImage(file ="fees.png")      
        self.b4=Button(root,text='click me',image=self.r,command=self.click2).place(x=900,y=243)
        self.e=PhotoImage(file ="transport.png")      
        self.b4=Button(root,text='click me',image=self.e,command=self.trans).place(x=1100,y=243)
    def click(self):
        stu_page(root)
    def click1(self):
        tech_page(root)
    def click2(self):
        fee_page(root)
    def trans(self):
        transport_page(root)
        
        
class stu_page():
    def __init__(self,root):
        self.root=Frame(root,width=1360,height=768)

        self.b=PhotoImage(file = "school.png")
        self.label=Label(root,image=self.b).place(x=0,y=0)

        self.c=PhotoImage(file = "stu1.png")
        self.B1=Button(root,image=self.c,command=self.click76).place(x=134,y=200)

        self.d=PhotoImage(file = "update1.png")
        self.B2=Button(root,image=self.d,command=self.click7).place(x=534,y=200)

        self.e=PhotoImage(file = "search1.png")
        self.B3=Button(root,image=self.e,command=self.click8).place(x=850,y=200)

        self.g=PhotoImage(file = "home1.png")
        self.B5=Button(root,image=self.g,command=self.click9).place(x=0,y=0)

    def click7(self):
        stu_form(root)
    def click9(self):
        home_page(root)
    def click76(self):
        stu_table(root)    
    def click8(self):
        stu_search(root)    




class tech_page():
    def __init__(self,root):
        self.root=Frame(root,width=1360,height=768)

        self.b=PhotoImage(file = "school.png")
        self.label=Label(root,image=self.b).place(x=0,y=0)

        self.c=PhotoImage(file = "teacher.png")
        self.B1=Button(root,image=self.c,command=self.tab).place(x=250,y=300)

        self.d=PhotoImage(file = "update2.png")
        self.B2=Button(root,image=self.d,command=self.lib_m3).place(x=600,y=300)

        self.e=PhotoImage(file = "search1.png")
        self.B3=Button(root,image=self.e,command=self.search_teachers).place(x=950,y=300)

        self.g=PhotoImage(file = "home1.png")
        self.B5=Button(root,image=self.g,command=self.Home_page).place(x=0,y=0)

    def lib_m3(self):
        teach_form(root)
    def Home_page(self):
        home_page(root)
    def search_teachers(self):
        teach_search(root)
    def tab(self):
        teacher_table(root)


class stu_form():
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
        self.b=PhotoImage(file = "lib.png")    
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
        self.l7=Label(root,text='Father name:',font=('Times',13),bg='Black',fg='white').place(x=605,y=400)
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
        co=mysql.connector.connect(host='localhost',user='root',password='12345678',database='school_m_s')
        c=co.cursor()
        c.execute("select (stu_id) from stu_info")
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
            self.co=mysql.connector.connect(host='localhost',user='root',password='12345678',database='school_m_s')
            self.c=self.co.cursor()
            self.c.execute("insert into stu_info(stu_id,Name,class,D_O_B,phone_no,Father_Name) VALUES ('{}','{}','{}','{}',{},'{}')".format(e,e1,e2,e3,e4,e5))
            self.co.commit()
            self.co.close()
            

            tk.messagebox.showinfo('successful','stored in database')
    def click12(self):
        home_page(root)
    def click13(self):
       stu_page(root)
###TEACHER_UPDATE        
class teach_form():
    def __init__(self,root):
        self.root =Frame(root,height=768,width=1360).pack()
        self.user1=StringVar()
        self.user2=StringVar()
        self.user3=StringVar()
        self.user4=IntVar()
        self.user5=StringVar()   
    
        self.a=PhotoImage(file = "back2.png")    
        self.l=Label(root,image=self.a,text='DAWN LIBRARY').place(x=0,y=0)
        self.b=PhotoImage(file = "lib.png")    
        self.l1=label=Label(root,image=self.b,text='DAWN LIBRARY').place(x=540,y=0)
        self.l3=Label(root,text='Teacher ID:',font=('Times',13),bg='Black',fg='white').place(x=630,y=200)
        self.e2=Entry(root,width=30,textvar=self.user1).place(x=730,y=200)
        self.l4=Label(root,text='Teacher Name :',font=('Times',13),bg='Black',fg='white').place(x=610,y=250)
        self.e3=Entry(root,width=30,textvar=self.user2).place(x=730,y=250)
        self.l5=Label(root,text='Date Of Birth:',font=('Times',13),bg='Black',fg='white').place(x=620,y=300)
        self.e4=Entry(root,width=30,textvar=self.user3).place(x=730,y=300)
        self.l6=Label(root,text='Phone No.:',font=('Times',13),bg='Black',fg='white').place(x=630,y=350)
        self.e5=Entry(root,width=30,textvar=self.user4).place(x=730,y=350)
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
        co=mysql.connector.connect(host='localhost',user='root',password='12345678',database='school_m_s')
        c=co.cursor()
        c.execute("select (Teacher_id) from teachers_info")
        b=c.fetchall()
        S=len(b)
        m=[]
        for i in range (S):
            m.append(b[i][0])
  
        if  e1=='' or e2=='' or e3=='' or e4 =='' :
            tk.messagebox.showinfo('warning','please fill up all boxes')
        elif e1 in m:
            tk.messagebox.showinfo('warning','Id Alredy Exist!!!')
            
        else:
            self.co=mysql.connector.connect(host='localhost',user='root',password='12345678',database='school_m_s')
            self.c=self.co.cursor()
            self.c.execute("insert into teachers_info (Teacher_id,Name,D_O_B,phone_no) VALUES ('{}','{}','{}',{})".format(e1,e2,e3,e4))
            self.co.commit()
            self.co.close()
            
            tk.messagebox.showinfo('successful','stored in database')
    def click18(self):
        home_page(root)
    def click19(self):  
        tech_page(root)

class stu_search():
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
        
        d=home_page(root)

    def click39(self):  
        
        d=stu_page(root)    
    def click21(self):
        self.d=self.user.get()
        self.co=mysql.connector.connect(host='localhost',user='root',password='12345678',database='school_m_s')
        self.c=self.co.cursor()
        self.s="select * from stu_info where stu_id="+str(self.d)
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

            self.label=Label(root,text="STU_ID       :"+str(r1),font=('Times',16),bg="light blue").place(x=500,y=150)
            self.label=Label(root,text="STU_NAME      :"+str(r2),font=('Times',16)).place(x=500,y=200)
            self.label=Label(root,text="Class        :"+str(r3),font=('Times',16)).place(x=500,y=250)
            self.label=Label(root,text="D_O_B         :"+str(r4),font=('Times',16)).place(x=500,y=300)
            self.label=Label(root,text="PHONE NO.     :"+str(r5),font=('Times',16)).place(x=500,y=350)
            self.label=Label(root,text="Father Name  :"+str(r6),font=('Times',16)).place(x=500,y=400)
            self.b1=Button(root,width=10,bg="black",fg="white",text="Delete",command=self.click22).place(x=580,y=470)

    def click22(self):
        self.d=self.user.get()
        self.co=mysql.connector.connect(host='localhost',user='root',password='12345678',database='school_m_s')
        self.c=self.co.cursor()
        self.s="delete from stu_info where stu_id="+str(self.d)
        self.c.execute(self.s)
        self.co.commit()
        self.co.close()
        tk.messagebox.showinfo('successful','Deleted from database')
        
###TEACHER_SEARCH
class teach_search():
    def __init__(self,root):
        self.user=StringVar()
        self.root=Frame(root,width=1360,height=768)
        self.b=PhotoImage(file = "school.png")
        self.label=Label(root,image=self.b).place(x=0,y=0)
        self.e1=Entry(root,width=30,textvar=self.user).place(x=134,y=200)
        self.b1=Button(root,width=10,bg="black",fg="white",text="search",command=self.click23).place(x=280,y=198)
        self.q=PhotoImage(file = "back1.png")
        self.label=Button(root,image=self.q,command=self.click49).place(x=45,y=0)
        self.w=PhotoImage(file = "home1.png")
        self.label2=Button(root,image=self.w,command=self.click48).place(x=0,y=0)
    def click48(self):
        
        d=home_page(root)

    def click49(self):  
        
        d=tech_page(root)    
    def click23(self):
        self.d=self.user.get()
        self.co=mysql.connector.connect(host='localhost',user='root',password='12345678',database='school_m_s')
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
            

          
            self.root=Frame(root,width=460,height=668).pack()
            self.d=PhotoImage(file = "back2.png")
            self.l1=Label(root,image=self.d).place(x=0,y=0)
            self.label=Label(root,text="TEACHER'S INFORMATION",font=('Times',40),bg="light blue").place(x=350,y=20)
            self.label=Label(root,text="TEACHER_ID       :"+str(r1),font=('Times',16),bg="light blue").place(x=500,y=150)
            self.label=Label(root,text="NAME      :"+str(r2),font=('Times',16)).place(x=500,y=200)
            self.label=Label(root,text="D_O_B         :"+str(r4),font=('Times',16)).place(x=500,y=250)
            self.label=Label(root,text="PHONE NO.     :"+str(r5),font=('Times',16)).place(x=500,y=300)
            self.b1=Button(root,width=10,bg="black",fg="white",text="Delete",command=self.click24).place(x=580,y=420)
class fee_page():
    def __init__(self,root):
        self.root =Frame(root,height=768,width=1360).pack()
        
        self.b=PhotoImage(file = "school.png")
        self.label=Label(root,image=self.b,text='DAWN LIBRARY').place(x=0,y=0)
        self.s=PhotoImage(file = "stu1.png")
        self.b2=Button(root,command=self.click,image=self.s).place(x=400,y=243)
        self.i=PhotoImage(file = "teacher.png")
        self.b3=Button(root,text='click me',image=self.i,command=self.click1).place(x=750,y=243)
        self.w=PhotoImage(file = "home1.png")
        self.label2=Button(root,image=self.w,command=self.click48).place(x=0,y=0)
    def click48(self):
        home_page(root)

        
    def click(self):
        fee_detail(root)
    def click1(self):
        fee_table(root)
class fee_detail():
    def __init__(self,root):
        self.root =Frame(root,height=768,width=1360).pack()    
        self.user=StringVar()
        self.user2=StringVar()
        self.user3=IntVar()
        self.user4=IntVar()
        self.d=PhotoImage(file = "back2.png")
        self.l1=Label(root,image=self.d).place(x=0,y=0)

        self.l2=Label(root,text="Steudent ID:",font=('Times',13),bg='Black',fg='white').place(x=780,y=150) 
        self.e1=tk.Entry(root,width=30,textvar=self.user).place(x=875,y=150)
        self.l4=Label(root,text='Student Name:',font=('Times',13),bg='Black',fg='white').place(x=760,y=200)
        self.l6=Label(root,text='Class:',font=('Times',13),bg='Black',fg='white').place(x=760,y=250)

        self.l3=Label(root,text='Total Fees:',font=('Times',13),bg='Black',fg='white').place(x=790,y=300) 
        self.e3=tk.Entry(root,width=30,textvar=self.user3).place(x=875,y=300)
        
        self.l2=Label(root,text='Balance Fees :',font=('Times',13),bg='Black',fg='white').place(x=755,y=350)
        self.e5=tk.Entry(root,width=30,textvar=self.user4).place(x=875,y=350)

        self.label=Button(root,height=2,width=12,text="submit",font=("times",11),bg="black",fg="white",command=self.click27).place(x=900,y=400)
        self.label2=Button(root,height=1,width=7,text="search",font=("times",11),bg="black",fg="white",command=self.click25).place(x=980,y=238)
        self.q=PhotoImage(file = "back1.png")
        self.label5=Button(root,image=self.q,command=self.click59).place(x=45,y=0)
        self.w=PhotoImage(file = "home1.png")
        self.label2=Button(root,image=self.w,command=self.click58).place(x=0,y=0)
    def click58(self):
        
        d=home_page(root)

    def click59(self):  
        
        d=fee_page(root)    
    def click25(self):   
        self.p=self.user.get()
        co=mysql.connector.connect(host='localhost',user='root',password='12345678',database='school_m_s')
        c=co.cursor()
        c.execute("select (stu_id) from stu_info")
        b=c.fetchall()
        S=len(b)
        m=[]
        for i in range (S):
            m.append(b[i][0])
        if self.p in m:
            self.co=mysql.connector.connect(host='localhost',user='root',password='12345678',database='school_m_s')
            self.c=self.co.cursor()
            n2="select * from stu_info where stu_id="+str(self.p)
            self.c.execute(n2)
            self.d1=self.c.fetchall()
            self.co.close()
            if self.d1==[]:
                tk.messagebox.showinfo('Sorry','Not Found In Database')
            else:     
                self.e2=tk.Label(self.root,text=self.d1[0][1],bg="white",font=("Times",12)).place(x=875,y=200)
                self.e2=tk.Label(self.root,text=self.d1[0][2],bg="white",font=("Times",12)).place(x=875,y=250)


        else:
            tk.messagebox.showinfo('WARNING','Invalid Id is Entered')

        
               
    


    def click27(self):
        g1=self.user.get()
        g2=self.d1[0][0]
        g3=self.d1[0][1]
        g4=self.user3.get()
        g5=self.user4.get()
        
        
        if g1=='' or g2==''or g3==''or g4=='':
            tk.messagebox.showinfo('warning','please fill up all boxes')

            
        else:
            print(g1,g2,g3,g4)
            self.co=mysql.connector.connect(host='localhost',user='root',password='12345678',database='school_m_s')
            self.c=self.co.cursor()
            self.s="insert into fees_info (Stu_Id,Name,Class,Total_fees,Balance_fees) VALUES ('{}','{}','{}',{},{})".format(g1,g2,g3,g4,g5)
            self.c.execute(self.s)
            self.co.commit()
            self.co.close()

            tk.messagebox.showinfo('successful','stored in database')        
class fee_table():
    def __init__(self,root):
        self.root =Frame(root,height=768,width=1360).pack()    
        self.user=StringVar()
        self.user2=StringVar()
        self.d=PhotoImage(file = "back2.png")
        self.l1=Label(root,image=self.d).place(x=0,y=0)
        
        self.l3=Label(root,text='Class:',font=('Times',13),bg='Black',fg='white').place(x=790,y=300) 
        self.e3=tk.Entry(root,width=30,textvar=self.user).place(x=875,y=300)
        
        self.l2=Label(root,text='Section(opt.)',font=('Times',13),bg='Black',fg='white').place(x=755,y=350)
        self.e5=tk.Entry(root,width=30,textvar=self.user2).place(x=875,y=350)

        self.label=Button(root,height=2,width=12,text="submit",font=("times",11),bg="black",fg="white",command=self.ckk).place(x=900,y=400)
        self.q=PhotoImage(file = "back1.png")
        self.label=Button(root,image=self.q,command=self.click49).place(x=45,y=0)
        self.w=PhotoImage(file = "home1.png")
        self.label2=Button(root,image=self.w,command=self.click48).place(x=0,y=0)
    def click49(self):
        
        d=fee_page(root)

    def click48(self):  
        
        d=home_page(root)    
    def ckk(self):  
        self.root = Tk()
        self.root.title("VISITORS")
        t=self.user.get()
        self.root.geometry("1600x1000+0+0")
        mainlabel =Label(self. root, text="VISITOR", font=("times new roman", 35), bg="MediumOrchid2")
        mainlabel.pack(side=TOP, fill=X)
        chat1 =ttk.Treeview(self.root,height=20 , columns=('stu_id', 'Name', 'Class','Total_fees','balance_fees'), selectmode="extended")
        chat1.heading('#0', text='stu_id', anchor=CENTER)
        chat1.heading('#1', text='Name', anchor=CENTER)
        chat1.heading('#2', text='Class', anchor=CENTER)
        chat1.heading('#3', text="Total_fees", anchor=CENTER)
        chat1.heading('#4', text="Balance_fees", anchor=CENTER)


        chat1.column('#1', stretch=YES, minwidth=50, width=100)
        chat1.column('#3', stretch=YES, minwidth=50, width=100)
        chat1.column('#2', stretch=YES, minwidth=50, width=300)
        chat1.column('#0', stretch=YES, minwidth=50, width=70)
        chat1.column('#4', stretch=YES, minwidth=50, width=100)

        vsb = ttk.Scrollbar(self.root, orient="vertical", command=chat1.yview)
        vsb.place(x=955, y=170, height=400 + 20)
        chat1.configure(yscrollcommand=vsb.set)
        chat1.place(x=400, y=170)
        ttk.Style().configure("Treeview", background="#383838", foreground="coral1")
        ttk.Style().configure("Treeview.heading", background="blue", foreground="palevioletRed1")
        self.root.configure(background="white")
        co=mysql.connector.connect(host='localhost',user='root',password='12345678',database='school_m_s')
        c=co.cursor()
        f='SELECT * FROM fees_info where Class='+str(t)
        c.execute(f)
        for row in c.fetchall():
            chat1.insert('', 0, text=row[0], values=(row[1], row[2], row[3],row[4],row[5]))
        
class stu_table():
    def __init__(self,root):
        self.root = Tk()
        self.root.title("VISITORS")
        self.root.geometry("1600x1000+0+0")
        mainlabel =Label(self. root, text="VISITOR", font=("times new roman", 35), bg="MediumOrchid2")
        mainlabel.pack(side=TOP, fill=X)
        chat1 =ttk.Treeview(self.root,height=20 , columns=('stu_id', 'Name', 'Class','D_O_B','phone_no','Father_Name'), selectmode="extended")
        chat1.heading('#0', text='stu_id', anchor=CENTER)
        chat1.heading('#1', text='Name', anchor=CENTER)
        chat1.heading('#2', text='Class', anchor=CENTER)
        chat1.heading('#3', text="D_O_B", anchor=CENTER)
        chat1.heading('#4', text="phone_no", anchor=CENTER)
        chat1.heading('#5', text="Father_Name", anchor=CENTER)


        chat1.column('#1', stretch=YES, minwidth=50, width=100)
        chat1.column('#3', stretch=YES, minwidth=50, width=100)
        chat1.column('#2', stretch=YES, minwidth=50, width=300)
        chat1.column('#0', stretch=YES, minwidth=50, width=70)
        chat1.column('#4', stretch=YES, minwidth=50, width=100)
        chat1.column('#5', stretch=YES, minwidth=50, width=100)

        vsb = ttk.Scrollbar(self.root, orient="vertical", command=chat1.yview)
        vsb.place(x=955, y=170, height=400 + 20)
        chat1.configure(yscrollcommand=vsb.set)
        chat1.place(x=400, y=170)
        ttk.Style().configure("Treeview", background="#383838", foreground="coral1")
        ttk.Style().configure("Treeview.heading", background="blue", foreground="palevioletRed1")
        self.root.configure(background="white")
        co=mysql.connector.connect(host='localhost',user='root',password='12345678',database='school_m_s')
        c=co.cursor()
        c.execute('SELECT * FROM stu_info')
        for row in c.fetchall():
            chat1.insert('', 0, text=row[0], values=(row[1], row[2], row[3],row[4],row[5]))

class teacher_table():
    def __init__(self,root):
        self.root = Tk()
        self.root.title("VISITORS")
        self.root.geometry("1600x1000+0+0")
        mainlabel =Label(self. root, text="STUDENT INFO", font=("times new roman", 35), bg="MediumOrchid2")
        mainlabel.pack(side=TOP, fill=X)
        chat1 =ttk.Treeview(self.root,height=20 , columns=('Teacher_id', 'Name', 'Class','DATE_of_birth','Phone_no'), selectmode="extended")
        chat1.heading('#0', text='Teacher_id', anchor=CENTER)
        chat1.heading('#1', text='Name', anchor=CENTER)
        chat1.heading('#2', text='Class', anchor=CENTER)
        chat1.heading('#3', text="DATE_of_birth", anchor=CENTER)
        chat1.heading('#4', text="Phone_no", anchor=CENTER)

        chat1.column('#0', stretch=YES, minwidth=50, width=70)
        chat1.column('#1', stretch=YES, minwidth=50, width=100)
        chat1.column('#2', stretch=YES, minwidth=50, width=300)
        chat1.column('#3', stretch=YES, minwidth=50, width=100)
        chat1.column('#4', stretch=YES, minwidth=50, width=300)

        vsb = ttk.Scrollbar(self.root, orient="vertical", command=chat1.yview)
        vsb.place(x=955, y=170, height=400 + 20)
        chat1.configure(yscrollcommand=vsb.set)
        chat1.place(x=400, y=170)
        ttk.Style().configure("Treeview", background="#383838", foreground="coral1")
        ttk.Style().configure("Treeview.heading", background="blue", foreground="palevioletRed1")
        self.root.configure(background="white")
        co=mysql.connector.connect(host='localhost',user='root',password='12345678',database='school_m_s')
        c=co.cursor()
        c.execute('SELECT * FROM teachers_info')
        for row in c.fetchall():
            chat1.insert('', 0, text=row[0], values=(row[1], row[2], row[3],row[4]))
#Driver_Details...........................................
class add_driver_details():
    def __init__(self,root):
        self.root =Frame(root,height=768,width=1360).pack()
        self.user1=StringVar()
        self.user2=StringVar()
        self.user3=StringVar()
        self.user4=IntVar()
        self.user5=StringVar()   
    
        self.a=PhotoImage(file = "back2.png")    
        self.l=Label(root,image=self.a,text='DAWN LIBRARY').place(x=0,y=0)
        self.b=PhotoImage(file = "lib.png")    
        self.l1=label=Label(root,image=self.b,text='DAWN LIBRARY').place(x=540,y=0)
        self.l3=Label(root,text='Driver ID:',font=('Times',13),bg='Black',fg='white').place(x=630,y=200)
        self.e2=Entry(root,width=30,textvar=self.user1).place(x=730,y=200)
        self.l4=Label(root,text='Driver Name :',font=('Times',13),bg='Black',fg='white').place(x=610,y=250)
        self.e3=Entry(root,width=30,textvar=self.user2).place(x=730,y=250)
        self.l5=Label(root,text='Date Of Birth:',font=('Times',13),bg='Black',fg='white').place(x=620,y=300)
        self.e4=Entry(root,width=30,textvar=self.user3).place(x=730,y=300)
        self.l6=Label(root,text='Phone No.:',font=('Times',13),bg='Black',fg='white').place(x=630,y=350)
        self.e5=Entry(root,width=30,textvar=self.user4).place(x=730,y=350)
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
        co=mysql.connector.connect(host='localhost',user='root',password='12345678',database='school_m_s')
        c=co.cursor()
        c.execute("select (Driver_id) from driver_info")
        b=c.fetchall()
        S=len(b)
        m=[]
        for i in range (S):
            m.append(b[i][0])
  
        if  e1=='' or e2=='' or e3=='' or e4 =='' :
            tk.messagebox.showinfo('warning','please fill up all boxes')
        elif e1 in m:
            tk.messagebox.showinfo('warning','Id Alredy Exist!!!')
            
        else:
            self.co=mysql.connector.connect(host='localhost',user='root',password='12345678',database='school_m_s')
            self.c=self.co.cursor()
            self.c.execute("insert into driver_info (Driver_id,Name,D_O_B,phone_no) VALUES ('{}','{}','{}',{})".format(e1,e2,e3,e4))
            self.co.commit()
            self.co.close()
            
            tk.messagebox.showinfo('successful','stored in database')
    def click19(self):
        transport_page(root)
    def click18(self):
        home_page(root)
class transport_page():
    def __init__(self,root):
        self.root =Frame(root,height=768,width=1360).pack()
        self.b=PhotoImage(file ="school.png")
        self.label=Label(root,image=self.b,text='DAWN LIBRARY').place(x=0,y=0)
        self.s=PhotoImage(file = "stu1.png")
        self.b2=Button(root,command=self.click,image=self.s).place(x=200,y=243)
        self.i=PhotoImage(file = "teacher.png")
        self.b3=Button(root,text='click me',image=self.i,command=self.click1).place(x=550,y=243)
        self.r=PhotoImage(file ="fees.png")      
        self.b4=Button(root,text='click me',image=self.r,command=self.click2).place(x=900,y=243)
        self.e=PhotoImage(file ="transport.png")      
        self.b4=Button(root,text='click me',image=self.e,command=self.trans).place(x=1100,y=243)
        self.g=PhotoImage(file = "home1.png")
        self.B5=Button(root,image=self.g,command=self.click9).place(x=0,y=0)

    def click7(self):
        stu_form(root)
    def click9(self):
        home_page(root)
    def click(self):
        drive_details(root)
    def click1(self):
        bus_details(root)
    def click2(self):
        add_bus_details(root)
    def trans(self):
        add_driver_details(root)
class driver_details():
    def __init__(self,root):
        self.root = Tk()
        self.root.title("VISITORS")
        self.root.geometry("1600x1000+0+0")
        mainlabel =Label(self. root, text="STUDENT INFO", font=("times new roman", 35), bg="MediumOrchid2")
        mainlabel.pack(side=TOP, fill=X)
        chat1 =ttk.Treeview(self.root,height=20 , columns=('Teacher_id', 'Name', 'Class','DATE_of_birth','Phone_no'), selectmode="extended")
        chat1.heading('#0', text='Teacher_id', anchor=CENTER)
        chat1.heading('#1', text='Name', anchor=CENTER)
        chat1.heading('#2', text='Class', anchor=CENTER)
        chat1.heading('#3', text="DATE_of_birth", anchor=CENTER)
        chat1.heading('#4', text="Phone_no", anchor=CENTER)

        chat1.column('#0', stretch=YES, minwidth=50, width=70)
        chat1.column('#1', stretch=YES, minwidth=50, width=100)
        chat1.column('#2', stretch=YES, minwidth=50, width=300)
        chat1.column('#3', stretch=YES, minwidth=50, width=100)
        chat1.column('#4', stretch=YES, minwidth=50, width=300)

        vsb = ttk.Scrollbar(self.root, orient="vertical", command=chat1.yview)
        vsb.place(x=955, y=170, height=400 + 20)
        chat1.configure(yscrollcommand=vsb.set)
        chat1.place(x=400, y=170)
        ttk.Style().configure("Treeview", background="#383838", foreground="coral1")
        ttk.Style().configure("Treeview.heading", background="blue", foreground="palevioletRed1")
        self.root.configure(background="white")
        co=mysql.connector.connect(host='localhost',user='root',password='12345678',database='school_m_s')
        c=co.cursor()
        c.execute('SELECT * FROM teachers_info')
        for row in c.fetchall():
            chat1.insert('', 0, text=row[0], values=(row[1], row[2], row[3],row[4]))
class add_bus_details():
    def __init__(self,root):
        self.root =Frame(root,height=768,width=1360).pack()
        self.user1=StringVar()
        self.user2=StringVar()
        self.user3=StringVar()
        self.user4=IntVar()
        self.user5=StringVar()   
    
        self.a=PhotoImage(file = "back2.png")    
        self.l=Label(root,image=self.a,text='DAWN LIBRARY').place(x=0,y=0)
        self.b=PhotoImage(file = "lib.png")    
        self.l1=label=Label(root,image=self.b,text='DAWN LIBRARY').place(x=540,y=0)
        self.l3=Label(root,text='BUS NO.:',font=('Times',13),bg='Black',fg='white').place(x=630,y=200)
        self.e2=Entry(root,width=30,textvar=self.user1).place(x=730,y=200)
        self.l4=Label(root,text='DRIVER NAME :',font=('Times',13),bg='Black',fg='white').place(x=610,y=250)
        self.e3=Entry(root,width=30,textvar=self.user2).place(x=730,y=250)
        self.l5=Label(root,text='ROUTE:',font=('Times',13),bg='Black',fg='white').place(x=620,y=300)
        self.e4=Entry(root,width=30,textvar=self.user3).place(x=730,y=300)
        self.l6=Label(root,text='REGISTRATION NO.:',font=('Times',13),bg='Black',fg='white').place(x=630,y=350)
        self.e5=Entry(root,width=30,textvar=self.user4).place(x=730,y=350)
        self.q=PhotoImage(file = "back1.png")
        self.label=Button(self.root,image=self.q,command=self.click19).place(x=45,y=0)
        self.w=PhotoImage(file = "home1.png")
        self.c=Button(root,width=7,height=2,text='Submit',font=10,bg='Black',fg='White',command=self.click17).place(x=750,y=450)
        self.label2=Button(self.root,image=self.w,command=self.click18).place(x=0,y=0)
    def click17(self):
       
        e1=self.user1.get()
        e2=self.user2.get()
        e3=self.user3.get()
        e4=self.user4.get()
        
        co=mysql.connector.connect(host='localhost',user='root',password='12345678',database='school_m_s')
        c=co.cursor()
        c.execute("select (Teacher_id) from teachers_info")
        b=c.fetchall()
        S=len(b)
        m=[]
        for i in range (S):
            m.append(b[i][0])
  
        if  e1=='' or e2=='' or e3=='' or e4 =='' :
            tk.messagebox.showinfo('warning','please fill up all boxes')
        elif e1 in m:
            tk.messagebox.showinfo('warning','Id Alredy Exist!!!')
            
        else:
            self.co=mysql.connector.connect(host='localhost',user='root',password='12345678',database='school_m_s')
            self.c=self.co.cursor()
            self.c.execute("insert into teachers_info (Teacher_id,Name,D_O_B,phone_no) VALUES ('{}','{}','{}',{})".format(e1,e2,e3,e4))
            self.co.commit()
            self.co.close()
            
            tk.messagebox.showinfo('successful','stored in database')
    def click18(self):
        home_page(root)
    def click19(self):  
        transport_page(root)

class bus_details():
    def __init__(self,root):
        self.root = Tk()
        self.root.title("VISITORS")
        self.root.geometry("1600x1000+0+0")
        mainlabel =Label(self. root, text="STUDENT INFO", font=("times new roman", 35), bg="MediumOrchid2")
        mainlabel.pack(side=TOP, fill=X)
        chat1 =ttk.Treeview(self.root,height=20 , columns=('Teacher_id', 'Name', 'Class','DATE_of_birth','Phone_no'), selectmode="extended")
        chat1.heading('#0', text='Teacher_id', anchor=CENTER)
        chat1.heading('#1', text='Name', anchor=CENTER)
        chat1.heading('#2', text='Class', anchor=CENTER)
        chat1.heading('#3', text="DATE_of_birth", anchor=CENTER)
        chat1.heading('#4', text="Phone_no", anchor=CENTER)

        chat1.column('#0', stretch=YES, minwidth=50, width=70)
        chat1.column('#1', stretch=YES, minwidth=50, width=100)
        chat1.column('#2', stretch=YES, minwidth=50, width=300)
        chat1.column('#3', stretch=YES, minwidth=50, width=100)
        chat1.column('#4', stretch=YES, minwidth=50, width=300)

        vsb = ttk.Scrollbar(self.root, orient="vertical", command=chat1.yview)
        vsb.place(x=955, y=170, height=400 + 20)
        chat1.configure(yscrollcommand=vsb.set)
        chat1.place(x=400, y=170)
        ttk.Style().configure("Treeview", background="#383838", foreground="coral1")
        ttk.Style().configure("Treeview.heading", background="blue", foreground="palevioletRed1")
        self.root.configure(background="white")
        co=mysql.connector.connect(host='localhost',user='root',password='12345678',database='school_m_s')
        c=co.cursor()
        c.execute('SELECT * FROM teachers_info')
        for row in c.fetchall():
            chat1.insert('', 0, text=row[0], values=(row[1], row[2], row[3],row[4]))
        
        
root=Tk()
d=home_page(root)
root.resizable(False, False)
root.mainloop()


