import mysql.connector as mc
from random import *
c=mc.connect(host='localhost',user='root', password ='mysql',database='proj_vidul')
if c.is_connected()==True:
    cur=c.cursor()
    cur.execute('select sid from sprofile')
    a1=cur.fetchall()
    l=[]
    for i in a1:
        l.append(i[0])
    print(l)
    q=['Pending','Paid']
    p=['Current sem','Previous sem']


            

    for k in l:
        try:
            am=randint(28999,169999)
            t=choice(q)
            t0=choice(p)
            cur.execute('insert into fees values("{}","{}","{}","{}")'.format(k,t0,am,t))
            c.commit()
        except:
            continue
print('ho giya')


cur.execute('select * from fees')
d0=cur.fetchall()
for p in d0:
    try:
        if p[3]=='Pending':            
            cur.execute('update fees set due_date="End of semester" where sid="{}"'.format(p[0]))
            c.commit()
    except:
        continue

