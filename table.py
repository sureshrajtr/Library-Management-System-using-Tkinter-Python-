from tkinter import *
import mysql.connector
class stu_table():
    def __init__(self,root):

        
        for i in range(total_row):
            for j in range(total_cols):
                self.e=Label(root,text=z[i][j],bg="black",fg="Blue",font=('Arial',16)).grid(row=i,column=j)
                

co=mysql.connector.connect(host='localhost',user='root',password='rsd123',database='Library')
c=co.cursor()
w= c.execute("select * from stu_info1")
z=c.fetchall()
total_row=len(z)
total_cols=len(z[0])

                
root=Tk()
d=stu_table(root)
