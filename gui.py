from tkinter import *
class login():
 
    def call(frame,user_var,passw_var):
        name=user_var.get()
        password=passw_var.get()
        x=["Ash",""]
        y=["hi",""]
        if name in x and password in y and x.index(name)==y.index(password):
            if name=="":
                frame.destroy()
                next=selection_admin()
                next.screen()
            else:
                frame.destroy()
                next=selection_student()
                next.screen()   
        
    def screen(self):
        super()
        user_var=StringVar()
        passw_var=StringVar()
        frame=Frame(root,height=400,width=600)
        frame.grid(row=0, column=0, sticky='nsew')
        label1 = Label(frame, text="Login") 
        label2 = Label(frame, text="password")
        entry_1 = Entry(frame,textvariable=user_var)
        entry_2 = Entry(frame,textvariable=passw_var)
        label1.place(relx=.5, rely=.5,anchor= CENTER,x=-50,y=-10)
        label2.place(relx=.5, rely=.5,anchor= CENTER,x=-60,y=10)
        entry_1.place(relx=.5, rely=.5,anchor= CENTER,x=40,y=-10)
        entry_2.place(relx=.5, rely=.5,anchor= CENTER,x=40,y=10)

        submit = Button(frame, text="Login",command=lambda:login.call(frame,user_var,passw_var))
        submit.place(relx=.5,rely=.5,anchor=CENTER,y=40)
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
        
    
    def subject_add(frame,x):
        frame.destroy()
        frame=Frame(root,height=400,width=600)
        frame.grid(row=0, column=0, sticky='nsew')
        ds=Button(frame,text="Data science",command=lambda:selection_admin.add_display(frame,'os'))
        os=Button(frame,text="Operating system",command=lambda:selection_admin.add_display(frame,'ds'))
        toc=Button(frame,text="Theory of computation",command=lambda:selection_admin.add_display(frame,'toc'))
        cp=Button(frame,text="Computer Programming II",command=lambda:selection_admin.add_display(frame,'cp'))
        ds.place(relx=.5, rely=.5,anchor= CENTER,y=-60)
        os.place(relx=.5, rely=.5,anchor= CENTER,y=-20)
        toc.place(relx=.5, rely=.5,anchor= CENTER,y=20)
        cp.place(relx=.5, rely=.5,anchor= CENTER,y=60)

    def subject_remove(frame,x):
        frame.destroy()
        frame=Frame(root,height=400,width=600)
        frame.grid(row=0, column=0, sticky='nsew')
        print("selection_admin."+x+"(frame,'ds')")
        ds=Button(frame,text="Data science",command=lambda:selection_admin.remove_display(frame,'os'))
        os=Button(frame,text="Operating system",command=lambda:selection_admin.remove_display(frame,'ds'))
        toc=Button(frame,text="Theory of computation",command=lambda:selection_admin.remove_display(frame,'toc'))
        cp=Button(frame,text="Computer Programming II",command=lambda:selection_admin.remove_display(frame,'cp'))
        ds.place(relx=.5, rely=.5,anchor= CENTER,y=-60)
        os.place(relx=.5, rely=.5,anchor= CENTER,y=-20)
        toc.place(relx=.5, rely=.5,anchor= CENTER,y=20)
        cp.place(relx=.5, rely=.5,anchor= CENTER,y=60)

    def remove_display(frame,sub):
        frame.destroy()
        frame=Frame(root,height=400,width=600)
        frame.grid(row=0, column=0, sticky='nsew')
        label=Label(frame,text="Assignment number")
        num_var=StringVar()
        entry=Entry(frame,textvariable=num_var)
        remove=Button(frame,text="Remove")
        label.place(relx=.5,rely=.5,anchor=CENTER,x=-100,y=0)
        entry.place(relx=.5,rely=.5,anchor=CENTER,x=25,y=0)
        remove.place(relx=.5,rely=.5,anchor=CENTER,y=50)

        
    def add_display(frame,sub):
        frame.destroy()
        frame=Frame(root,height=400,width=600)
        frame.grid(row=0, column=0, sticky='nsew')
        anum=StringVar()
        wl=StringVar()
        dd=StringVar()
        Label1=Label(frame,text="Assignment num")
        Label2=Label(frame,text="Work link")
        Label3=Label(frame,text="Due date")
        entry1=Entry(frame,textvariable=anum)
        entry2=Entry(frame,textvariable=wl)
        entry3=Entry(frame,textvariable=dd)
        submit=Button(frame,text="submit")#command=lambda:pdm.add())
        Label1.place(relx=.5,rely=.5,anchor=CENTER,x=-100,y=-40)
        Label2.place(relx=.5,rely=.5,anchor=CENTER,x=-80,y=0)
        Label3.place(relx=.5,rely=.5,anchor=CENTER,x=-80,y=40)
        entry1.place(relx=.5,rely=.5,anchor=CENTER,x=25,y=-40)
        entry2.place(relx=.5,rely=.5,anchor=CENTER,x=25,y=0)
        entry3.place(relx=.5,rely=.5,anchor=CENTER,x=25,y=40)
        submit.place(relx=.5,rely=.5,anchor=CENTER,y=100)


    
    def screen(self):
        super()
        frame=Frame(root,height=400,width=600)
        frame.grid(row=0, column=0, sticky='nsew')
        add=Button(frame,text="Add assignment",command=lambda:selection_admin.subject_add(frame,"add_display"))
        remove=Button(frame,text="Remove assignment",command=lambda:selection_admin.subject_remove(frame,"remove_display"))
        pending=Button(frame,text="Show all pending assignments",command=lambda:selection_admin.subject(frame))
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
