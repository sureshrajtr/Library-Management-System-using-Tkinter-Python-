c.execute("create table if not exists driver_info(Driver_id varchar(10),Name varchar(50),D_O_B varchar(10),phone_no bigint())")
class driver_details():
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
        co=mysql.connector.connect(host='localhost',user='root',password=pasw,database=db)
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
            self.co=mysql.connector.connect(host='localhost',user='root',password=pasw,database=db)
            self.c=self.co.cursor()
            self.c.execute("insert into driver_info (Driver_id,Name,D_O_B,phone_no) VALUES ('{}','{}','{}',{})".format(e1,e2,e3,e4))
            self.co.commit()
            self.co.close()
            
            tk.messagebox.showinfo('successful','stored in database')
