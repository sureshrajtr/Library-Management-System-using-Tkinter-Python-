root=Tk()
        co=mysql.connector.connect(host='localhost',user='root',password=pasw,database=db)
        c=co.cursor()
        w= c.execute("select * from stu_info1")
        z=c.fetchall()
        total_row=len(z)
        total_cols=len(z[0]) 
        scrollbar = Scrollbar(root)
        scrollbar.pack( side = RIGHT, fill = Y )
        mylist = Listbox(root,height=20,width=160, yscrollcommand = scrollbar.set )
        mylist.pack()
        scrollbar.config( command = mylist.yview )
        for i in range(total_row):
            for j in range(total_cols):
                self.e=Entry(root,width=15,fg="Black",font=('Arial',16,"bold"))
                self.e.insert(END,z[i][j])
                self.e.place(y=i*50,x=j*150)          
