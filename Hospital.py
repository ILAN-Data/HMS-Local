from tkinter import *
from tkinter import messagebox 
import mysql.connector
import random
import datetime
con=mysql.connector.connect(host="localhost",user="root",password="admin")
cur=con.cursor()
con.autocommit=True
query="create database if not exists hospital"
cur.execute(query)
query="use hospital"
cur.execute(query)
query="create table if not exists verify(name varchar(20),dob varchar(10),gender varchar(10),bloodgroup varchar(10),mobile varchar(15))"
cur.execute(query)
query="create table if not exists members(name varchar(20),dob varchar(10),gender varchar(10),bloodgroup varchar(10),mobile varchar(15),cardno varchar(15))"
cur.execute(query)
query="create table if not exists cardno(cardno varchar(15))"
cur.execute(query)
query="create table if not exists doctors(Doctorname varchar(15),Time varchar(15),Number int(5))"
cur.execute(query)
query="create table if not exists patients(Cardno varchar(10),Doctor_name varchar(15),Date varchar(10))"
cur.execute(query)
query="create table if not exists numbers(x11 varchar(3))"
cur.execute(query)
query="truncate table numbers"
cur.execute(query)
query="insert into numbers values(0)"
cur.execute(query)
query="select date from patients"
cur.execute(query)
patient_date=cur.fetchall()
query="delete from patients where date!=%s"
cur.execute(query,(str(datetime.datetime.now().date()),))
if len(patient_date)!=0:
    if patient_date[0][0]!=str(datetime.datetime.now().date()):
        query="update doctors set Number=30"
        cur.execute(query)
    
def register():
    root2=Tk()
    def submit():
        global gen,E21,E22,E24,E25
        if str(E21.get())=="":
            E21=Entry(root2,font="10",bg="pink")
            E21.grid(row=4,column=1)
        if str(E22.get())=="DD/MM/YYYY":
            E22=Entry(root2,font="10",bg="pink")
            E22.insert(0,"DD/MM/YYYY")
            E22.grid(row=5,column=1)
        if str(gen.get())=="":
            gen=StringVar(root2)
            gen.set("Select")
            E23=OptionMenu(root2,gen,"MALE","FEMALE","OTHER")
            E23.grid(row=6,column=1)
        if str(E24.get())=="" or str(E24.get())=="Blood+or-":
            E24=Entry(root2,font="10",bg="pink")
            E24.insert(0,"Blood+or-")
            E24.grid(row=7,column=1)
        if str(E25.get())=="":
            E25=Entry(root2,font="10",bg="pink")
            E25.grid(row=8,column=1)
        if  str(E21.get())=="" or str(E22.get())=="DD/MM/YYYY" or str(gen.get())=="Select" or str(E24.get())=="" or str(E24.get())=="Blood+or-" or str(E25.get())=="":
            L2=Label(root2,text="Enter all fields correctly").grid(row=15,column=0)
        if str(E21.get())!="" and str(E22.get())!="DD/MM/YYYY" and str(gen.get())!="Select" and str(E24.get())!="" and str(E24.get())!="Blood+or-" and str(E25.get())!="":
            name=str(E21.get())
            dob=str(E22.get())
            gender=str(gen.get())
            bloodgroup=str(E24.get())
            mobile=str(E25.get())
            query="select * from verify where name=%s and mobile=%s"
            cur.execute(query,(name,mobile))
            check1=cur.fetchall()
            if check1==[]:
                query="insert into verify values(%s,%s,%s,%s,%s)"
                cur.execute(query,(name,dob,gender,bloodgroup,mobile))
                messagebox.showinfo("Note!","Application successfully uploaded pending for verfication")
                root2.destroy()
            else:
                messagebox.showinfo("Note!","Application already registered Status: pending")
                root2.destroy()
            
    root2.title("Registration Application")
    root2.geometry("+800+0")
    root2.geometry("400x900")
    root2.configure(bg="old lace")
    L2=Label(root2,text="                                           ",bg="old lace").grid(row=0,column=0)
    L2=Label(root2,text="  Apply For Card    ",font="times 18 bold italic underline",relief="raised",fg="white",bg="midnight blue").grid(row=1,column=1)
    L2=Label(root2,text="",bg="old lace").grid(row=2,column=0)
    L2=Label(root2,text="",bg="old lace").grid(row=3,column=0)
    L2=Label(root2,text="""Name : """,font="times 14 bold italic",width="11",relief="solid",bg="snow",fg="blue").grid(row=4,column=0)
    L2=Label(root2,text="""D.O.B: """,font="times 14 bold italic",width="11",relief="solid",bg="snow",fg="blue").grid(row=5,column=0)
    L2=Label(root2,text="""Gender: """,font="times 14 bold italic",width="11",relief="solid",bg="snow",fg="blue").grid(row=6,column=0)
    L2=Label(root2,text="""Blood Group: """,font="times 14 bold italic",width="11",relief="solid",bg="snow",fg="blue").grid(row=7,column=0)
    L2=Label(root2,text="""Mobile No: """,font="times 14 bold italic",width="11",relief="solid",bg="snow",fg="blue").grid(row=8,column=0)
    global E21,E22,gen,E24,E25
    E21=Entry(root2,font="10",justify="center")
    E22=Entry(root2,font="10",justify="center")
    E22.insert(0,"DD/MM/YYYY")
    gen=StringVar(root2)
    gen.set("Select")
    E23=OptionMenu(root2,gen,"MALE","FEMALE","OTHER")
    E24=Entry(root2,font="10",justify="center")
    E24.insert(0,"Blood+or-")
    E25=Entry(root2,font="10",justify="center")
    E21.grid(row=4,column=1)
    E22.grid(row=5,column=1)
    E23.grid(row=6,column=1)
    E24.grid(row=7,column=1)
    E25.grid(row=8,column=1)
    L2=Label(root2,text="**all caps**").grid(row=10,column=0)
    L2=Label(root2,text="",bg="old lace").grid(row=11,column=0)
    B1=Button(root2,text="SUBMIT Application",font="georgia 11 bold",relief="raised",bg="lime green",fg="white",command=submit).grid(row=12,column=1)

def cardno():
    m=2000
    query="select * from cardno"
    cur.execute(query)
    f=cur.fetchall()
    if len(f)==0:
        query="insert into cardno values(%s)"
        cur.execute(query,(m,))
        query="select * from cardno"
        cur.execute(query)
        f=cur.fetchall()
        query="delete from cardno"
        cur.execute(query)
        key=int(f[len(f)-1][0])
        key=str(key)
        i=random.randint(65,90)
        s=chr(i)
        no=str(key)+s
        query="insert into cardno values(%s)"
        key=int(key)+1
        cur.execute(query,(key,))
        return no
    else:
        query="select * from cardno"
        cur.execute(query)
        f=cur.fetchall()
        query="delete from cardno"
        cur.execute(query)
        key=int(f[len(f)-1][0])
        key=str(key)
        i=random.randint(65,90)
        s=chr(i)
        no=str(key)+s
        query="insert into cardno values(%s)"
        key=int(key)+1
        cur.execute(query,(key,))
        return no
        
def view():
    query="select * from numbers"
    cur.execute(query)
    global x11
    x11=int(cur.fetchall()[0][0])
    query="select * from members"
    cur.execute(query)
    q=cur.fetchall()
    root5=Tk()
    root5.title("CARD HOLDERS")
    root5.geometry("+0+0")
    root5.geometry("1200x1000")
    root5.configure(bg="azure")
    L5=Label(root5,text="S.No",font="15",relief="solid",width="15",height="2",bg="light blue").grid(row=0,column=0)
    L5=Label(root5,text="NAME",font="15",relief="solid",width="15",height="2",bg="light blue").grid(row=0,column=1)
    L5=Label(root5,text="DOB",font="15",relief="solid",width="15",height="2",bg="light blue").grid(row=0,column=2)
    L5=Label(root5,text="GENDER",font="15",relief="solid",width="15",height="2",bg="light blue").grid(row=0,column=3)
    L5=Label(root5,text="BLOOD GROUP",font="15",relief="solid",width="15",height="2",bg="light blue").grid(row=0,column=4)
    L5=Label(root5,text="MOBILE",font="15",relief="solid",width="15",height="2",bg="light blue").grid(row=0,column=5)
    L5=Label(root5,text="CARDNO",font="15",relief="solid",width="15",height="2",bg="light blue").grid(row=0,column=6)
    
    def edit():
        
        root6=Tk()
        root6.title("Edit window")
        root6.geometry("+1200+0")
        root6.geometry("400x900")
        root6.configure(bg="azure")
        e11=Entry(root6,font="Rockwell 11 bold")
        e11.grid(row=1,column=1)
        l11=Label(root6,text="Cardno:",font="Rockwell 13 bold",bg="light green",fg="white",width="8").grid(row=1,column=0)
        def grab():
            m=e11.get()
            query="select name,dob,gender,mobile from members where cardno=%s"
            cur.execute(query,(e11.get(),))
            a=cur.fetchall()
            if a!=[]:
                e21=Entry(root6,font="Rockwell 14 bold")
                e22=Entry(root6,font="Rockwell 14 bold")
                e23=Entry(root6,font="Rockwell 14 bold")
                e24=Entry(root6,font="Rockwell 14 bold")
                L21=Label(root6,text="Name",font="Rockwell 14 bold",relief="solid",width="10").grid(row=4,column=0)
                L21=Label(root6,text="DOB",font="Rockwell 14 bold",relief="solid",width="10").grid(row=5,column=0)
                L21=Label(root6,text="Gender",font="Rockwell 14 bold",relief="solid",width="10").grid(row=6,column=0)
                L21=Label(root6,text="Mobile",font="Rockwell 14 bold",relief="solid",width="10").grid(row=7,column=0)
                e21.grid(row=4,column=1)
                e22.grid(row=5,column=1)
                e23.grid(row=6,column=1)
                e24.grid(row=7,column=1)
                def done():
                    query="update members set name=%s,dob=%s,gender=%s,mobile=%s where cardno=%s"
                    cur.execute(query,(e21.get(),e22.get(),e23.get(),e24.get(),e11.get()))
                    root6.destroy()
                    root5.destroy()
                    view()
                    
                e21.insert(0,a[0][0])
                e22.insert(0,a[0][1])
                e23.insert(0,a[0][2])
                e24.insert(0,a[0][3])
                b21=Button(root6,text="Confirm",font="Rockwell 12 bold",bg="light sky blue",command=done).grid(row=8,column=1)
            else:
                L21=Label(root6,text="N/A",relief="groove",width="10").grid(row=4,column=0)
        b11=Button(root6,text="Grab",font="rockwell 11 bold",bg="black",fg="white",command=grab).grid(row=1,column=2)
    w=[]
    for i in q:
        L=[]
        for j in i:
            L.append(j)
        w.append(L)
        
    x22=len(w)
    def value_data():
        def scroll_up():
            global x11
            if x11!=0:
                x11-=5
                query="update numbers set x11=%s"
                cur.execute(query,(x11,))
                root5.destroy()
                view()
        def scroll_down():
            global x11
            if x11<=len(q)-6:
                x11+=5
                query="update numbers set x11=%s"
                cur.execute(query,(x11,))
                root5.destroy()
                view()
        c=1
        d=0
        for i in w[x11:x22]:
            L5=Label(root5,text=c+x11,font="15",relief="solid",width="15",height="2").grid(row=c,column=d)
            d=1
            for j in i:
                L5=Label(root5,text=j,font="15",relief="solid",width="15",height="2").grid(row=c,column=d)
                d=d+1
            c=c+1
            d=0
        b1up=Button(root5,text="↑↑",font="default 15 bold",relief="groove",width="7",bg="red",fg="white",command=scroll_up).grid(row=1,column=7)
        b1down=Button(root5,text="↓↓",font="default 15 bold",relief="groove",width="7",bg="lime green",fg="white",command=scroll_down).grid(row=2,column=7)
    value_data()
    b1=Button(root5,text="Edit",font="default 12 bold italic",relief="solid",width="5",bg="navy",fg="white",command=edit).grid(row=0,column=7)
def timings():
    def replace():
        Lw=list()
        Lm=list()
        w1=E111.get()
        w2=E112.get()
        w3=E113.get()
        w4=E114.get()
        w5=E115.get()
        w6=E116.get()
        w7=E117.get()
        w8=E118.get()
        w9=E119.get()
        w10=E120.get()
        Lw.append(w1)
        Lw.append(w2)
        Lw.append(w3)
        Lw.append(w4)
        Lw.append(w5)
        Lw.append(w6)
        Lw.append(w7)
        Lw.append(w8)
        Lw.append(w9)
        Lw.append(w10)

        m1=E211.get()
        m2=E212.get()
        m3=E213.get()
        m4=E214.get()
        m5=E215.get()
        m6=E216.get()
        m7=E217.get()
        m8=E218.get()
        m9=E219.get()
        m10=E220.get()

        Lm.append(m1)
        Lm.append(m2)
        Lm.append(m3)
        Lm.append(m4)
        Lm.append(m5)
        Lm.append(m6)
        Lm.append(m7)
        Lm.append(m8)
        Lm.append(m9)
        Lm.append(m10)
        
        num=0
        for i in List1:
            i[1]=Lw[num]
            i[0]=Lm[num]
            num+=1
        query="truncate table doctors"
        cur.execute(query)
        for i in range(len(List)):
            query="insert into doctors values(%s,%s,%s)"
            cur.execute(query,(List1[i][0],List1[i][1],List1[i][2]))
        message_info=messagebox .showinfo("Note!","Successfully changed the timings")
        root8.destroy()
        
    root8=Tk()
    root8.title("Timings")
    root8.geometry("+800+0")
    root8.geometry("400x900")
    query="select * from doctors"
    cur.execute(query)
    b1=cur.fetchall()
    List=b1
    if len(List)==0:
        staff()
    query="select * from doctors"
    cur.execute(query)
    b1=cur.fetchall()
    List=b1
    LL1=[]
    for i in List:
        LL2=[]
        LL2.append(i[0])
        LL2.append(i[1])
        LL2.append(i[2])
        LL1.append(LL2)
    List1=LL1
    
    L1=Label(root8,text="Doctor name",font="15",relief="solid",width="15",height="2",bg="light green").grid(row=0,column=1)
    L1=Label(root8,text="Timings",font="15",relief="solid",width="15",height="2",bg="light green").grid(row=0,column=2)

    E211=Entry(root8,font="17")
    E211.insert(0,List[0][0])
    E212=Entry(root8,font="17")
    E212.insert(0,List[1][0])
    E213=Entry(root8,font="17")
    E213.insert(0,List[2][0])
    E214=Entry(root8,font="17")
    E214.insert(0,List[3][0])
    E215=Entry(root8,font="17")
    E215.insert(0,List[4][0])
    E216=Entry(root8,font="17")
    E216.insert(0,List[5][0])
    E217=Entry(root8,font="17")
    E217.insert(0,List[6][0])
    E218=Entry(root8,font="17")
    E218.insert(0,List[7][0])
    E219=Entry(root8,font="17")
    E219.insert(0,List[8][0])
    E220=Entry(root8,font="17")
    E220.insert(0,List[9][0])

    E211.grid(row=1,column=1)
    E212.grid(row=2,column=1)
    E213.grid(row=3,column=1)
    E214.grid(row=4,column=1)
    E215.grid(row=5,column=1)
    E216.grid(row=6,column=1)
    E217.grid(row=7,column=1)
    E218.grid(row=8,column=1)
    E219.grid(row=9,column=1)
    E220.grid(row=10,column=1)

    E111=Entry(root8,font="17")
    E111.insert(0,List[0][1])
    E112=Entry(root8,font="17")
    E112.insert(0,List[1][1])
    E113=Entry(root8,font="17")
    E113.insert(0,List[2][1])
    E114=Entry(root8,font="17")
    E114.insert(0,List[3][1])
    E115=Entry(root8,font="17")
    E115.insert(0,List[4][1])
    E116=Entry(root8,font="17")
    E116.insert(0,List[5][1])
    E117=Entry(root8,font="17")
    E117.insert(0,List[6][1])
    E118=Entry(root8,font="17")
    E118.insert(0,List[7][1])
    E119=Entry(root8,font="17")
    E119.insert(0,List[8][1])
    E120=Entry(root8,font="17")
    E120.insert(0,List[9][1])
    
    E111.grid(row=1,column=2)
    E112.grid(row=2,column=2)
    E113.grid(row=3,column=2)
    E114.grid(row=4,column=2)
    E115.grid(row=5,column=2)
    E116.grid(row=6,column=2)
    E117.grid(row=7,column=2)
    E118.grid(row=8,column=2)
    E119.grid(row=9,column=2)
    E120.grid(row=10,column=2)
    L=Label(root8,text="").grid(row=11,column=2)
    B81=Button(root8,text="Finalize timings",font="Times 15 bold",bg="red",fg="white",command=replace).grid(row=12,column=1)
    
def password():
    def check():
        if e1.get()==passw1:
            F_pass.destroy()
            admin()
            password()
            
    def check1():
        if e1.get()==passw2:
            F_pass.destroy()
            view()
            password()
    def check2():
        if e1.get()==passw3:
            F_pass.destroy()
            timings()
            password()

    def Close():
        F_pass.destroy()

    F_pass=Frame(root)
    F_pass.configure(bg="sky blue")
    l1=Label(F_pass,text="Enter admin :",font="default 12 bold italic",relief="groove",width="25",bg="white",fg="red").pack()
    l1==Label(F_pass,text=" ",bg="sky blue").pack()
    e1=Entry(F_pass,font="Times 20 bold",fg="black",relief="groove",bd="4",width="10",justify="center")
    e1.pack()
    e1.config(show="*")
    l1==Label(F_pass,text=" ",bg="sky blue").pack()
    b1=Button(F_pass,text="Review Applicants",font="georgia 12 bold",relief="raised",width="20",height="2",bd="4",bg="orange",fg="white",command=check).pack()
    l1==Label(F_pass,text=" ",bg="sky blue").pack()
    b2=Button(F_pass,text="View Members",font="georgia 12 bold",relief="raised",width="20",height="2",bd="4",bg="blue",fg="white",command=check1).pack()
    l1==Label(F_pass,text=" ",bg="sky blue").pack()
    b3=Button(F_pass,text="""View Timings
And Updates""",font="georgia 12 bold",relief="raised",width="20",bd="4",bg="red",fg="white",command=check2).pack()
    l1==Label(F_pass,text=" ",bg="sky blue").pack()
    b4=Button(F_pass,text="Close",font="georgia 12 bold",relief="raised",width="20",bd="4",bg="purple1",fg="white",command=Close).pack()
    passw1="2004"
    passw2="2005"
    passw3="2006"
    F_pass.grid(row=5,column=1,columnspan=3,sticky="E")

def admin():
    query="select * from verify"
    cur.execute(query)
    val1=cur.fetchall()
    l1=val1
    root3=Tk()
    root3.title("Admin")
    root3.geometry("+0+0")
    root3.geometry("1150x1000")
    if len(l1)==0:
        word=" NO APPLICANTS! "
    else:
        word=""
    for i in range(len(l1)):
        L33=Label(root3,text=i+1,font="times 12 bold",relief="solid",width="15",height="2").grid(row=i+3,column=1)
                  
    L33=Label(root3,text="""TOTAL
APPLICANTS: """+str(len(l1))+ word,font="times 13 bold",bg="light blue").grid(row=0,column=1)
    L33=Label(root3,text="S.No",font="times 11 bold",relief="solid",width="15").grid(row=1,column=1)
               
    L33=Label(root3,text="Name",font="times 11 bold",relief="solid",width="15").grid(row=1,column=2)
    L33=Label(root3,text="DOB",font="times 11 bold",relief="solid",width="15").grid(row=1,column=3)
    L33=Label(root3,text="Gender",font="times 11 bold",relief="solid",width="15").grid(row=1,column=4)
    L33=Label(root3,text="Bloodgroup",font="times 11 bold",relief="solid",width="15").grid(row=1,column=5)
    L33=Label(root3,text="Mobile",font="times 11 bold",relief="solid",width="15").grid(row=1,column=6)
    a=3
    b=2
    value=0
    def approve():
        query="insert into members values(%s,%s,%s,%s,%s,%s)"
        cur.execute(query,(l1[0]+(cardno(),)))
        query="delete from verify where name=%s and mobile=%s"
        cur.execute(query,(l1[0][0],l1[0][4]))
        admin()
        root3.destroy()
            
    def decline():
        query="delete from verify where name=%s and mobile=%s"
        cur.execute(query,(l1[0][0],l1[0][4]))
        admin()
        root3.destroy()
            
    for i in l1:
        for j in i:
            L3=Label(root3,text=j,font="times 12 bold",relief="solid",width="15",height="2").grid(row=a,column=b)
            b=b+1
        b=2
        a=a+1
    b1=Button(root3,text="Approve",relief="raised",bg="light green",command=approve,font="10").grid(row=3,column=7)
    b2=Button(root3,text="Decline",relief="raised",bg="pink",command=decline,font="10").grid(row=3,column=8)     


    
def staff():
    Doctor_name=["Doctor1","Doctor2","Doctor3","Doctor4","Doctor5","Doctor6","Doctor7","Doctor8","Doctor9","Doctor10"]
    Time=["8:00","9:00","10:00","11:00","12:00","1:00","2:00","3:00","4:00","5:00"]
    Final=[]
    length=len(Doctor_name)
    for i in range(length):
        t=[]
        a1=random.choice(Doctor_name)
        a2=random.choice(Time)
        t.append(a1)
        t.append(a2)
        t.append(30)
        Final.append(t)
        Doctor_name.remove(a1)
        Time.remove(a2)
    for i in range(length):
        query="insert into doctors values(%s,%s,%s)"
        cur.execute(query,(Final[i][0],Final[i][1],Final[i][2]))
        
def appointment():
    code=E1.get()
    date=datetime.datetime.now().date()
    query="select * from doctors"
    cur.execute(query)
    doctor_variable=cur.fetchall()
    if len(doctor_variable)==0:
        staff()
    if code!="":
        try:
            import os
            query="select name,dob,gender from members where cardno=%s"
            cur.execute(query,(code,))
            data=cur.fetchall()
            name,dob,gender=data[0]
            root7=Tk()
            root7.geometry("540x900")
            root7.geometry("+660+0")
            root7.title("Doctors")
            L7=Label(root7,text="         ").grid(row=0,column=0)
            L7=Label(root7,text="Name: "+name,font="Rockwell 12 bold",relief="solid",bg="red",fg="white",height="2",width="25").grid(row=1,column=1)
            L7=Label(root7,text="Gender: "+gender,font="Rockwell 12 bold",relief="solid",bg="red",fg="white",height="2",width="20").grid(row=1,column=2)
            L9=Label(root7,text="").grid(row=2,column=1)
            L9=Label(root7,text="Date: "+str(date),font="Rockwell 12 bold",relief="solid",height="2",width="20").grid(row=3,column=1,columnspan=2)
            query="select * from doctors"
            cur.execute(query)
            data1=cur.fetchall()
            r=2
            c=0
            filedata=["Name: "+name+"\n","Cardno: "+code+"\n","Gender: "+gender+"\n","Date: "+str(date)+"\n"]
            L=[]
            for i in data1:
                l=[]
                l.append(i[0])
                l.append(i[1])
                L.append(l)
            def doctor1():
                query="select number from doctors where Doctorname=%s"
                cur.execute(query,(L[0][0],))
                T=cur.fetchall()[0][0]
                if T!=0:
                    N=31-T
                    root9=Tk()
                    root9.title("Confirm")
                    root9.geometry("200x100")
                    root9.geometry("+840+700")
                    root9.configure(background="black")
                    L9=Label(root9,text="Token No: "+str(N)+"""
"""+"Dr. "+L[0][0],font="Times 12 bold italic",relief="solid",bg="white",height="2",width="20").pack()
                    def complete():
                        filedata.extend(["Token No: "+str(N)+"\n","Doctor name: Dr."+L[0][0]+"\n","Time: "+L[0][1]+"\n"])
                        query="update doctors set number=number-1 where Doctorname=%s"
                        cur.execute(query,(L[0][0],))
                        query="insert into patients value(%s,%s,%s)"
                        cur.execute(query,(code,L[0][0],date))
                        f=open("appointment.txt","w")
                        f.writelines(filedata)
                        f.close()
                        root9.destroy()
                        root7.destroy()
                        E1.delete(0,END)
                        message=messagebox.showinfo("Note!","Success, CTRL+P to -[PRINT]- Token")
                        os.startfile("appointment.txt")
                        
                    B9=Button(root9,text="O.K",font="Times 12 bold",relief="groove",bg="red",fg="white",height="2",width="10",bd="6",command=complete).pack()
                else:
                    message=messagebox.showinfo("Note!","No tokens Available")
                

            def doctor2():
                query="select number from doctors where Doctorname=%s"
                cur.execute(query,(L[1][0],))
                T=cur.fetchall()[0][0]
                if T!=0:
                    N=31-T
                    root9=Tk()
                    root9.title("Confirm")
                    root9.geometry("200x100")
                    root9.geometry("+840+700")
                    root9.configure(background="black")
                    L9=Label(root9,text="Token No: "+str(N)+"""
"""+"Dr. "+L[1][0],font="Times 12 bold italic",relief="solid",bg="white",height="2",width="20").pack()
                    
                    def complete():
                        filedata.extend(["Token No: "+str(N)+"\n","Doctor name: Dr."+L[1][0]+"\n","Time: "+L[1][1]+"\n"])
                        query="update doctors set number=number-1 where Doctorname=%s"
                        cur.execute(query,(L[1][0],))
                        query="insert into patients value(%s,%s,%s)"
                        cur.execute(query,(code,L[1][0],date))
                        f=open("appointment.txt","w")
                        f.writelines(filedata)
                        f.close()
                        root9.destroy()
                        root7.destroy()
                        E1.delete(0,END)
                        message=messagebox.showinfo("Note!","Success, CTRL+P to -[PRINT]- Token")
                        os.startfile("appointment.txt")
                        
                    B9=Button(root9,text="O.K",font="Times 12 bold",relief="groove",bg="red",fg="white",height="2",width="10",bd="6",command=complete).pack()
                else:
                    message=messagebox.showinfo("Note!","No tokens Available")
            def doctor3():
                query="select number from doctors where Doctorname=%s"
                cur.execute(query,(L[2][0],))
                T=cur.fetchall()[0][0]
                if T!=0:
                    N=31-T
                    root9=Tk()
                    root9.title("Confirm")
                    root9.geometry("200x100")
                    root9.geometry("+840+700")
                    root9.configure(background="black")
                    L9=Label(root9,text="Token No: "+str(N)+"""
"""+"Dr. "+L[2][0],font="Times 12 bold italic",relief="solid",bg="white",height="2",width="20").pack()
                    
                    def complete():
                        filedata.extend(["Token No: "+str(N)+"\n","Doctor name: Dr."+L[2][0]+"\n","Time: "+L[2][1]+"\n"])
                        query="update doctors set number=number-1 where Doctorname=%s"
                        cur.execute(query,(L[2][0],))
                        query="insert into patients value(%s,%s,%s)"
                        cur.execute(query,(code,L[2][0],date))
                        f=open("appointment.txt","w")
                        f.writelines(filedata)
                        f.close()
                        root9.destroy()
                        root7.destroy()
                        E1.delete(0,END)
                        message=messagebox.showinfo("Note!","Success, CTRL+P to -[PRINT]- Token")
                        os.startfile("appointment.txt")
                        
                    B9=Button(root9,text="O.K",font="Times 12 bold",relief="groove",bg="red",fg="white",height="2",width="10",bd="6",command=complete).pack()
                else:
                    message=messagebox.showinfo("Note!","No tokens Available")

            def doctor4():
                query="select number from doctors where Doctorname=%s"
                cur.execute(query,(L[3][0],))
                T=cur.fetchall()[0][0]
                if T!=0:
                    N=31-T
                    root9=Tk()
                    root9.title("Confirm")
                    root9.geometry("200x100")
                    root9.geometry("+840+700")
                    root9.configure(background="black")
                    L9=Label(root9,text="Token No: "+str(N)+"""
"""+"Dr. "+L[3][0],font="Times 12 bold italic",relief="solid",bg="white",height="2",width="20").pack()
                    
                    def complete():
                        filedata.extend(["Token No: "+str(N)+"\n","Doctor name: Dr."+L[3][0]+"\n","Time: "+L[3][1]+"\n"])
                        query="update doctors set number=number-1 where Doctorname=%s"
                        cur.execute(query,(L[3][0],))
                        query="insert into patients value(%s,%s,%s)"
                        cur.execute(query,(code,L[3][0],date))
                        f=open("appointment.txt","w")
                        f.writelines(filedata)
                        f.close()
                        root9.destroy()
                        root7.destroy()
                        E1.delete(0,END)
                        message=messagebox.showinfo("Note!","Success, CTRL+P to -[PRINT]- Token")
                        os.startfile("appointment.txt")
                        
                    B9=Button(root9,text="O.K",font="Times 12 bold",relief="groove",bg="red",fg="white",height="2",width="10",bd="6",command=complete).pack()
                else:
                    message=messagebox.showinfo("Note!","No tokens Available")

            def doctor5():
                query="select number from doctors where Doctorname=%s"
                cur.execute(query,(L[4][0],))
                T=cur.fetchall()[0][0]
                if T!=0:
                    N=31-T
                    root9=Tk()
                    root9.title("Confirm")
                    root9.geometry("200x100")
                    root9.geometry("+840+700")
                    root9.configure(background="black")
                    L9=Label(root9,text="Token No: "+str(N)+"""
"""+"Dr. "+L[4][0],font="Times 12 bold italic",relief="solid",bg="white",height="2",width="20").pack()
                    
                    def complete():
                        filedata.extend(["Token No: "+str(N)+"\n","Doctor name: Dr."+L[4][0]+"\n","Time: "+L[4][1]+"\n"])
                        query="update doctors set number=number-1 where Doctorname=%s"
                        cur.execute(query,(L[4][0],))
                        query="insert into patients value(%s,%s,%s)"
                        cur.execute(query,(code,L[4][0],date))
                        f=open("appointment.txt","w")
                        f.writelines(filedata)
                        f.close()
                        root9.destroy()
                        root7.destroy()
                        E1.delete(0,END)
                        message=messagebox.showinfo("Note!","Success, CTRL+P to -[PRINT]- Token")
                        os.startfile("appointment.txt")
                        
                    B9=Button(root9,text="O.K",font="Times 12 bold",relief="groove",bg="red",fg="white",height="2",width="10",bd="6",command=complete).pack()
                else:
                    message=messagebox.showinfo("Note!","No tokens Available")

            def doctor6():
                query="select number from doctors where Doctorname=%s"
                cur.execute(query,(L[5][0],))
                T=cur.fetchall()[0][0]
                if T!=0:
                    N=31-T
                    root9=Tk()
                    root9.title("Confirm")
                    root9.geometry("200x100")
                    root9.geometry("+840+700")
                    root9.configure(background="black")
                    L9=Label(root9,text="Token No: "+str(N)+"""
"""+"Dr. "+L[5][0],font="Times 12 bold italic",relief="solid",bg="white",height="2",width="20").pack()
                    
                    def complete():
                        filedata.extend(["Token No: "+str(N)+"\n","Doctor name: Dr."+L[5][0]+"\n","Time: "+L[5][1]+"\n"])
                        query="update doctors set number=number-1 where Doctorname=%s"
                        cur.execute(query,(L[5][0],))
                        query="insert into patients value(%s,%s,%s)"
                        cur.execute(query,(code,L[5][0],date))
                        f=open("appointment.txt","w")
                        f.writelines(filedata)
                        f.close()
                        root9.destroy()
                        root7.destroy()
                        E1.delete(0,END)
                        message=messagebox.showinfo("Note!","Success, CTRL+P to -[PRINT]- Token")
                        os.startfile("appointment.txt")
                        
                    B9=Button(root9,text="O.K",font="Times 12 bold",relief="groove",bg="red",fg="white",height="2",width="10",bd="6",command=complete).pack()
                else:
                    message=messagebox.showinfo("Note!","No tokens Available")
                
            def doctor7():
                query="select number from doctors where Doctorname=%s"
                cur.execute(query,(L[6][0],))
                T=cur.fetchall()[0][0]
                if T!=0:
                    N=31-T
                    root9=Tk()
                    root9.title("Confirm")
                    root9.geometry("200x100")
                    root9.geometry("+840+700")
                    root9.configure(background="black")
                    L9=Label(root9,text="Token No: "+str(N)+"""
"""+"Dr. "+L[6][0],font="Times 12 bold italic",relief="solid",bg="white",height="2",width="20").pack()
                    
                    def complete():
                        filedata.extend(["Token No: "+str(N)+"\n","Doctor name: Dr."+L[6][0]+"\n","Time: "+L[6][1]+"\n"])
                        query="update doctors set number=number-1 where Doctorname=%s"
                        cur.execute(query,(L[6][0],))
                        query="insert into patients value(%s,%s,%s)"
                        cur.execute(query,(code,L[6][0],date))
                        f=open("appointment.txt","w")
                        f.writelines(filedata)
                        f.close()
                        root9.destroy()
                        root7.destroy()
                        E1.delete(0,END)
                        message=messagebox.showinfo("Note!","Success, CTRL+P to -[PRINT]- Token")
                        os.startfile("appointment.txt")
                        
                    B9=Button(root9,text="O.K",font="Times 12 bold",relief="groove",bg="red",fg="white",height="2",width="10",bd="6",command=complete).pack()
                else:
                    message=messagebox.showinfo("Note!","No tokens Available")

            def doctor8():
                query="select number from doctors where Doctorname=%s"
                cur.execute(query,(L[7][0],))
                T=cur.fetchall()[0][0]
                if T!=0:
                    N=31-T
                    root9=Tk()
                    root9.title("Confirm")
                    root9.geometry("200x100")
                    root9.geometry("+840+700")
                    root9.configure(background="black")
                    L9=Label(root9,text="Token No: "+str(N)+"""
"""+"Dr. "+L[7][0],font="Times 12 bold italic",relief="solid",bg="white",height="2",width="20").pack()
                    
                    def complete():
                        filedata.extend(["Token No: "+str(N)+"\n","Doctor name: Dr."+L[7][0]+"\n","Time: "+L[7][1]+"\n"])
                        query="update doctors set number=number-1 where Doctorname=%s"
                        cur.execute(query,(L[7][0],))
                        query="insert into patients value(%s,%s,%s)"
                        cur.execute(query,(code,L[7][0],date))
                        f=open("appointment.txt","w")
                        f.writelines(filedata)
                        f.close()
                        root9.destroy()
                        root7.destroy()
                        E1.delete(0,END)
                        message=messagebox.showinfo("Note!","Success, CTRL+P to -[PRINT]- Token")
                        os.startfile("appointment.txt")
                        
                    B9=Button(root9,text="O.K",font="Times 12 bold",relief="groove",bg="red",fg="white",height="2",width="10",bd="6",command=complete).pack()
                else:
                    message=messagebox.showinfo("Note!","No tokens Available")

            def doctor9():
                query="select number from doctors where Doctorname=%s"
                cur.execute(query,(L[8][0],))
                T=cur.fetchall()[0][0]
                if T!=0:
                    N=31-T
                    root9=Tk()
                    root9.title("Confirm")
                    root9.geometry("200x100")
                    root9.geometry("+840+700")
                    root9.configure(background="black")
                    L9=Label(root9,text="Token No: "+str(N)+"""
"""+"Dr. "+L[8][0],font="Times 12 bold italic",relief="solid",bg="white",height="2",width="20").pack()
                    
                    def complete():
                        filedata.extend(["Token No: "+str(N)+"\n","Doctor name: Dr."+L[8][0]+"\n","Time: "+L[8][1]+"\n"])
                        query="update doctors set number=number-1 where Doctorname=%s"
                        cur.execute(query,(L[8][0],))
                        query="insert into patients value(%s,%s,%s)"
                        cur.execute(query,(code,L[8][0],date))
                        f=open("appointment.txt","w")
                        f.writelines(filedata)
                        f.close()
                        root9.destroy()
                        root7.destroy()
                        E1.delete(0,END)
                        message=messagebox.showinfo("Note!","Success, CTRL+P to -[PRINT]- Token")
                        os.startfile("appointment.txt")
                        
                    B9=Button(root9,text="O.K",font="Times 12 bold",relief="groove",bg="red",fg="white",height="2",width="10",bd="6",command=complete).pack()
                else:
                    message=messagebox.showinfo("Note!","No tokens Available")

            def doctor10():
                query="select number from doctors where Doctorname=%s"
                cur.execute(query,(L[9][0],))
                T=cur.fetchall()[0][0]
                if T!=0:
                    N=31-T
                    root9=Tk()
                    root9.title("Confirm")
                    root9.geometry("200x100")
                    root9.geometry("+840+700")
                    root9.configure(background="black")
                    L9=Label(root9,text="Token No: "+str(N)+"""
"""+"Dr. "+L[9][0],font="Times 12 bold italic",relief="solid",bg="white",height="2",width="20").pack()
                    
                    def complete():
                        filedata.extend(["Token No: "+str(N)+"\n","Doctor name: Dr."+L[9][0]+"\n","Time: "+L[9][1]+"\n"])
                        query="update doctors set number=number-1 where Doctorname=%s"
                        cur.execute(query,(L[9][0],))
                        query="insert into patients value(%s,%s,%s)"
                        cur.execute(query,(code,L[9][0],date))
                        f=open("appointment.txt","w")
                        f.writelines(filedata)
                        f.close()
                        root9.destroy()
                        root7.destroy()
                        E1.delete(0,END)
                        message=messagebox.showinfo("Note!","Success, CTRL+P to -[PRINT]- Token")
                        os.startfile("appointment.txt")
                        
                    B9=Button(root9,text="O.K",font="Times 12 bold",relief="groove",bg="red",fg="white",height="2",width="10",bd="6",command=complete).pack()
                else:
                    message=messagebox.showinfo("Note!","No tokens Available")
            d={0:doctor1,1:doctor2,2:doctor3,3:doctor4,4:doctor5,5:doctor6,6:doctor7,7:doctor8,8:doctor9,9:doctor10}
            L9=Label(root7,text="").grid(row=4,column=1)
            L9=Label(root7,text="").grid(row=5,column=1)
            r=6
            c=1
            bg="orange"
            for i in range(0,len(d)):
                B=Button(root7,text="Dr. "+str(L[i][0])+"""
"""+"Time: "+str(L[i][1]),font="Rockwell 12 bold",relief="raised",bg=bg,height="3",width="20",command=d[i],bd="6").grid(row=r,column=c)
                if i%2==1:
                    c=1
                    r=r+1
                    L9=Label(root7,text="").grid(row=r,column=c)
                    r+=1
                   
                else:
                    c=c+1
          
                if c%2==0:
                    bg="light sky blue"
                else:
                    bg="orange"
        except:
            message=messagebox.showinfo("Note!","NO card exists")

def main():
    global root
    root=Tk()
    root.title("Hospital")
    root.configure(bg="antiquewhite")
    root.geometry("+1200+0")
    root.geometry("400x900")



    
    F_MAIN=Frame(root,bg="antiquewhite")
    L1=Label(F_MAIN,text=" Medical Id : ",font="Rockwell 16 bold",bg="red",fg="white",width="18").grid(row=1,column=1)
    L=Label(F_MAIN,text="")
    L.grid(row=2,column=0)
    global E1
    L2=Label(F_MAIN,text="Card No: ",font="Rockwell 15 bold",bg="dodgerblue",fg="white").grid(row=3,column=0)
    E1=Entry(F_MAIN,font="Rockwell 12 bold",width=20,bd="5",relief="sunken")
    E1.grid(row=3,column=1)

    
    L=Label(root,text="")
    L.grid(row=2,column=0)
    F_1=Frame(root,bg="black",bd="6",relief="raised")
    
    B1=Button(F_1,text="Get Appointment",font="Rockwell 14 bold",bg="orange",fg="white",width="18",command=appointment).grid(row=3,column=1)
    B1=Button(F_1,text=" Register Now",font="Rockwell 14 bold",bg="purple1",fg="white",width="18",command=register).grid(row=4,column=1)
    L=Label(F_1,text="",bg="black").grid(row=5,column=1)
    L=Label(F_1,text="",bg="black").grid(row=6,column=1)
    L=Label(F_1,text="",bg="black").grid(row=7,column=1)
    
    B1=Button(F_1,text=" Admin Access",font="Rockwell 12 bold",bg="deep sky blue",fg="white",width="15",command=password).grid(row=8,column=1)

    L=Label(root,text="").grid(row=4,column=1)
    F_MAIN.grid(row=1,column=1,columnspan=2)
    F_1.grid(row=3,column=2,sticky="E")

main()                                                 
