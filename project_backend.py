import mysql.connector as myc
from datetime import datetime, timezone
conn=myc.connect(host='localhost',user='root',password='12345',database='project_management')
cursor=conn.cursor()

def connect():
    conn=myc.connect(host='localhost',user='root',password='12345',database='project_management')
    cursor=conn.cursor()

def register(id,password,status):
    connect()
    q="insert into users values('"+id+"','"+password+"','"+status+"')"
    cursor.execute(q)
    conn.commit()
    conn.close()

def verify(id,password):
    connect()
    q="select status from users where id='"+str(id)+"' and password='"+password+"';"
    cursor.execute(q)
    data=cursor.fetchall()
    print(data)
    if not data:
        return "X"
    else:

        return data[0]
    

def add(sub,anum,wl,dd):
    connect()
    ref={"os":"CS3CO09","dbms":"CS3CO25","toc":"CS3CO10","cp":"CS3CO08"}
    code=ref[sub]
    date = datetime.now().strftime("%Y-%m-%d")
    due=datetime.strptime(dd,"%Y-%m-%d")
    q="insert into class_work values('"+code+"','"+sub+"',"+str(anum)+",'"+wl+"','"+str(date)+"','"+str(due)+"')"
    cursor.execute(q)
    conn.commit()
    conn.close()

def remove(sub,anum):
    connect()
    q="delete from class_work where assignment_num="+str(anum)+" and sub_name ='"+sub+"';"
    cursor.execute(q)
    conn.commit()
    conn.close()

def display(data):
    d=""
    n=0
    for row in data:
        for i in row:
            i=str(i)
            n+=len(i)+5
            d+=(str(i)+'  |  ')
        d+="\n"
        d+=( '_'*n)
    return d

def pending_admin(sub):
    connect()
    q="select id from "+user+" where status='s' and id not in(select id from "+sub+";"
    cursor.execute(q)
    data=cursor.fetchall()
    d=display(data)
    return d

def show_all():
    q="select * from class_work"
    cursor.execute(q)
    data=cursor.fetchall()
    d=display(data)
    return d

def show_pending(id):
    for i in ["os","toc","dbms","cp"]:
        q="select * from class_work where sub='"+i+"' and assignment_num not in (select assignment_num from '"+i+"' where id='"+id+"');"
        cursor.execute(q)
        data=cursor.fetchall()
        d=display(data)
    return d
        
def student_dict(sub):
    q="select id from users where status='s';"
    cursor.execute(q)
    data=cursor.fetchall()
    d=[]
    e=[]
    al=[]
    for i in data:
        if i[0]!=None:
            d.append(i[0])
            e.append(0)
    q="select distinct assignment_num from class_work where sub_name='"+sub+"';"
    cursor.execute(q)
    data=cursor.fetchall()
    for i in data:
        if i[0]!=None:
            al.append(i[0])
    return d,e,al

def student_mark(d,sub,anum):
    q="insert into "+sub+" values"
    for i in d:
        q+="('"+anum +"','"+i+"')"
    cursor.execute(q)
    conn.commit()
    conn.close()
    
    

