from tkinter import *
from project_backend import *
class login():
    def call(frame,user_var,passw_var):
        name=user_var.get()
        password=passw_var.get()
        v=verify(name,password)
        if  "t" in v:
            frame.destroy()
            next=selection_admin()
            next.screen()
        elif "s" in v:
            frame.destroy()
            next=selection_student()
            next.screen()  

        
    def reg_call(frame,user_var,passw_var,status_var):
        name=user_var.get()
        password=passw_var.get()
        status=status_var.get()
        register(name,password,status)
        frame.destroy()
        next=login()
        next.screen()



    def register(frame):
        frame.destroy()
        frame=Frame(root,height=400,width=600)
        frame.grid(row=0, column=0, sticky='nsew')
        user_var=StringVar()
        passw_var=StringVar()
        status_var=StringVar()
        status_var.set("s")
        frame=Frame(root,height=400,width=600)
        frame.grid(row=0, column=0, sticky='nsew')
        label1 = Label(frame, text="Id") 
        label2 = Label(frame, text="password")
        entry_1 = Entry(frame,textvariable=user_var)
        entry_2 = Entry(frame,textvariable=passw_var,show="*")
        label3 = Label(frame, text="Status")
        r1 = Radiobutton(frame, text="Student", variable=status_var, value="s")
        r1.place(relx=.5,rely=.5,anchor=CENTER,x=40,y=20)
        r2 = Radiobutton(frame, text="Teacher", variable=status_var, value="t")
        r2.place(relx=.5,rely=.5,anchor=CENTER,x=120,y=20)
        label1.place(relx=.5, rely=.5,anchor= CENTER,x=-50,y=-20)
        label2.place(relx=.5, rely=.5,anchor= CENTER,x=-60,y=0)
        entry_1.place(relx=.5, rely=.5,anchor= CENTER,x=40,y=-20)
        entry_2.place(relx=.5, rely=.5,anchor= CENTER,x=40,y=0)
        label3.place(relx=.5, rely=.5,anchor= CENTER,x=-50,y=20)
        register = Button(frame, text="Register",command=lambda:login.reg_call(frame,user_var,passw_var,status_var))
        register.place(relx=.5,rely=.5,anchor=CENTER,x=-40,y=60)
        back = Button(frame, text="Back",command=lambda:login.back(frame))
        back.place(relx=.5,rely=.5,anchor=CENTER,x=40,y=60)

    def back(frame):
        frame.destroy()
        back=login()
        back.screen()

    def screen(self):
        super()
        user_var=StringVar()
        passw_var=StringVar()
        frame=Frame(root,height=400,width=600)
        frame.grid(row=0, column=0, sticky='nsew')
        label1 = Label(frame, text="Id") 
        label2 = Label(frame, text="password")
        entry_1 = Entry(frame,textvariable=user_var)
        entry_2 = Entry(frame,textvariable=passw_var,show="*")
        label1.place(relx=.5, rely=.5,anchor= CENTER,x=-47,y=-10)
        label2.place(relx=.5, rely=.5,anchor= CENTER,x=-60,y=10)
        entry_1.place(relx=.5, rely=.5,anchor= CENTER,x=40,y=-10)
        entry_2.place(relx=.5, rely=.5,anchor= CENTER,x=40,y=10)

        submit = Button(frame, text="Login",command=lambda:login.call(frame,user_var,passw_var))
        submit.place(relx=.5,rely=.5,anchor=CENTER,x=-40,y=40)
        submit = Button(frame, text="Register",command=lambda:login.register(frame))
        submit.place(relx=.5,rely=.5,anchor=CENTER,x=40,y=40)
        root.mainloop()
    
        
class selection_student:
    def call(frame):
        frame.destroy()
        next=login()
        next.screen()
        


    def screen(self):
        super()
        frame=Frame(root,height=400,width=600)
        frame.grid(row=0, column=0, sticky='nsew')
        incomplete=Button(frame,text="Show all pending assignments")
        select=Button(frame,text="Show all assignments")
        logout=Button(frame,text="logout",command=lambda:selection_student.call(frame))
        select.place(relx=.5, rely=.5,anchor= CENTER,y=-50)
        incomplete.place(relx=.5, rely=.5,anchor= CENTER)
        logout.place(relx=.5, rely=.5,anchor= CENTER,y=50)
        root.mainloop()

class selection_admin:
    def call(frame):
        frame.destroy()
        next=login()
        next.screen()
        
    def back(frame):
        frame.destroy()
        back=selection_admin()
        back.screen()

    def pending_display(frame):
        frame.destroy()
        frame=Frame(root,height=400,width=600)
        frame.grid(row=0, column=0, sticky='nsew')
        sub=StringVar()
        sub.set("OS")
        r1 = Radiobutton(frame, text="OS", variable=sub, value="os")
        r1.place(relx=.5,rely=.5,anchor=CENTER,x=-90,y=-60)
        r2 = Radiobutton(frame, text="DMBS", variable=sub, value="dbms")
        r2.place(relx=.5,rely=.5,anchor=CENTER,x=-30,y=-60)
        r3 = Radiobutton(frame, text="CP", variable=sub, value="cp")
        r3.place(relx=.5,rely=.5,anchor=CENTER,x=30,y=-60)
        r4 = Radiobutton(frame, text="TOC", variable=sub, value="toc")
        r4.place(relx=.5,rely=.5,anchor=CENTER,x=90,y=-60)
        show=Button(frame,text="show",command=lambda:selection_admin.show_remaining(frame,sub))
        show.place(relx=.5,rely=.5,anchor=CENTER,x=-40,y=100)
        back=Button(frame,text="Back",command=lambda:selection_admin.back(frame))
        back.place(relx=.5,rely=.5,anchor=CENTER,x=40,y=100)
    def show_remaining(frame,sub):
        frame.destroy()
        frame=Frame(root,height=400,width=600)
        frame.grid(row=0, column=0, sticky='nsew')
        anum=0
        sub=sub.get()
        text=pending_admin(sub)
        label=Label(frame,text=text)
        label.place(relx=.5,rely=.5,anchor=CENTER)
    def remove_display(frame):
        frame.destroy()
        frame=Frame(root,height=400,width=600)
        frame.grid(row=0, column=0, sticky='nsew')
        sub=StringVar()
        sub.set("OS")
        anum=StringVar()
        r1 = Radiobutton(frame, text="OS", variable=sub, value="os")
        r1.place(relx=.5,rely=.5,anchor=CENTER,x=-90,y=-60)
        r2 = Radiobutton(frame, text="DMBS", variable=sub, value="dbms")
        r2.place(relx=.5,rely=.5,anchor=CENTER,x=-30,y=-60)
        r3 = Radiobutton(frame, text="CP", variable=sub, value="cp")
        r3.place(relx=.5,rely=.5,anchor=CENTER,x=30,y=-60)
        r4 = Radiobutton(frame, text="TOC", variable=sub, value="toc")
        r4.place(relx=.5,rely=.5,anchor=CENTER,x=90,y=-60)
        label=Label(frame,text="Assignment number")
        entry=Entry(frame,textvariable=anum)
        remove=Button(frame,text="Remove",command=lambda:selection_admin.remove_sub())
        label.place(relx=.5,rely=.5,anchor=CENTER,x=-100,y=0)
        entry.place(relx=.5,rely=.5,anchor=CENTER,x=25,y=0)
        remove.place(relx=.5,rely=.5,anchor=CENTER,x=-40,y=50)
        back=Button(frame,text="Back",command=lambda:selection_admin.back(frame))
        back.place(relx=.5,rely=.5,anchor=CENTER,x=40,y=50)

    def remove_sub(frame,sub,anum):
        sub=sub.get()
        anum=anum.get()
        remove(sub,anum)
        frame.destroy()
        frame=Frame(root,height=400,width=600)
        frame.grid(row=0, column=0, sticky='nsew')
        selection.admin.back()


        
    def add_display(frame):
        frame.destroy()
        frame=Frame(root,height=400,width=600)
        frame.grid(row=0, column=0, sticky='nsew')
        sub=StringVar()
        sub.set("OS")
        anum=StringVar()
        wl=StringVar()
        dd=StringVar()
        r1 = Radiobutton(frame, text="OS", variable=sub, value="os")
        r2 = Radiobutton(frame, text="DMBS", variable=sub, value="dbms")
        r3 = Radiobutton(frame, text="CP", variable=sub, value="cp")        
        r4 = Radiobutton(frame, text="TOC", variable=sub, value="toc")
        Label1=Label(frame,text="Assignment num")
        Label2=Label(frame,text="Work link")
        Label3=Label(frame,text="Due date")
        entry1=Entry(frame,textvariable=anum)
        entry2=Entry(frame,textvariable=wl)
        entry3=Entry(frame,textvariable=dd)
        submit=Button(frame,text="Submit",command=lambda:selection_admin.get_add(frame,sub,anum,wl,dd))
        r1.place(relx=.5,rely=.5,anchor=CENTER,x=-90,y=-70)
        r2.place(relx=.5,rely=.5,anchor=CENTER,x=-30,y=-70)
        r3.place(relx=.5,rely=.5,anchor=CENTER,x=30,y=-70)
        r4.place(relx=.5,rely=.5,anchor=CENTER,x=90,y=-70)
        Label1.place(relx=.5,rely=.5,anchor=CENTER,x=-100,y=-40)
        Label2.place(relx=.5,rely=.5,anchor=CENTER,x=-80,y=0)
        Label3.place(relx=.5,rely=.5,anchor=CENTER,x=-80,y=40)
        entry1.place(relx=.5,rely=.5,anchor=CENTER,x=25,y=-40)
        entry2.place(relx=.5,rely=.5,anchor=CENTER,x=25,y=0)
        entry3.place(relx=.5,rely=.5,anchor=CENTER,x=25,y=40)
        submit.place(relx=.5,rely=.5,anchor=CENTER,x=-40,y=100)
        back=Button(frame,text="Back",command=lambda:selection_admin.back(frame))
        back.place(relx=.5,rely=.5,anchor=CENTER,x=40,y=100)
  
    def get_add(frame,sub,anum,wl,dd):
        sub=sub.get()
        anum=anum.get()
        wl=wl.get()
        dd=dd.get()
        add(sub,anum,wl,dd)
        frame.destroy()
        frame=Frame(root,height=400,width=600)
        frame.grid(row=0, column=0, sticky='nsew')
        selection.admin.back()
    


    
    def screen(self):
        super()
        frame=Frame(root,height=400,width=600)
        frame.grid(row=0, column=0, sticky='nsew')
        add=Button(frame,text="Add assignment",command=lambda:selection_admin.add_display(frame))
        remove=Button(frame,text="Remove assignment",command=lambda:selection_admin.remove_display(frame))
        pending=Button(frame,text="Show all pending assignments",command=lambda:selection_admin.pending_display(frame))
        mark=Button(frame,text="Mark complete",command=lambda:selection_admin.subject(frame))
        logout=Button(frame,text="logout",command=lambda:selection_admin.call(frame))
        add.place(relx=.5, rely=.5,anchor= CENTER,y=-60)
        remove.place(relx=.5, rely=.5,anchor= CENTER,y=-30)
        pending.place(relx=.5, rely=.5,anchor= CENTER)
        mark.place(relx=.5, rely=.5,anchor= CENTER,y=30)
        logout.place(relx=.5, rely=.5,anchor= CENTER,y=60)
        root.mainloop()
  
root=Tk()
root.geometry("600x400")
root.title(string='Project Manager')
w=login()
w.screen()
