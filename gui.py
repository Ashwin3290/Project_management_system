from tkinter import *
class login():
 
    def call(frame,user_var,passw_var):
        name=user_var.get()
        password=passw_var.get()
        x=["Ash","Admin"]
        y=["hi","master"]
        if name in x and password in y and x.index(name)==y.index(password):
            if name=="Admin":
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
        
    
    def subject(frame,x):
        frame.destroy()
        frame=Frame(root,height=400,width=600)
        frame.grid(row=0, column=0, sticky='nsew')
        ds=Button(frame,text="Data science")
        os=Button(frame,text="Operating system")
        toc=Button(frame,text="Theory of computation")
        cp=Button(frame,text="Computer Programming II")
        ds.place(relx=.5, rely=.5,anchor= CENTER,y=-40,command=lambda:eval("selection_admin."+x+"(frame)"))
        os.place(relx=.5, rely=.5,anchor= CENTER,y=-10,command=lambda:eval("selection_admin."+x+"(frame)"))
        toc.place(relx=.5, rely=.5,anchor= CENTER,y=10,command=lambda:eval("selection_admin."+x+"(frame)"))
        cp.place(relx=.5, rely=.5,anchor= CENTER,y=40,command=lambda:eval("selection_admin."+x+"(frame)"))

    def remove(frame):
        label=Label(frame,text="Enter assignment number")
        num_var=StringVar()
        entry=Entry(frame,num_var)
        remove=Button(frame,text="Remove")
        label.place(relx=.5,rely=.5,anchor= CENTER,y=-10)
        remove.place(relx=.5,rely=.5,anchor= CENTER,y=10)
        
    def add(frame):
        
        entry1=Entry(frame,)
        entry2=Entry(frame,)
        entry3=Entry(frame,)
        entry4=Entry(frame,)
        entry5=Entry(frame,)


    
    def screen(self):
        super()
        frame=Frame(root,height=400,width=600)
        frame.grid(row=0, column=0, sticky='nsew')
        add=Button(frame,text="Add assignment",command=lambda:selection_admin.subject(frame))
        remove=Button(frame,text="Remove assignment",command=lambda:selection_admin.subject(frame))
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
