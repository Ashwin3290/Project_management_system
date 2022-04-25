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
    print(q)
    cursor.execute(q)
    conn.commit()
    conn.close()
def verify(id,password):
    connect()
    q="select status from users where id='"+str(id)+"' and password='"+password+"';"
    cursor.execute(q)
    data=cursor.fetchall()
    d=data[0]
    if len(data)==0:
        return data[0]
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

def pending_admin(sub):
    connect()
    #q="select id from "+user+" where id not in(select id from "+sub+";"
    q="select * from class_work"
    cursor.execute(q)
    data=cursor.fetchall()
    print(data)
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
