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
    p=['Final sem','Previous sem']


            
   
    for k in l:
        am=randint(28999,169999)
        t=choice(q)
        t0=choice(p)
        cur.execute('insert into fees values("{}","{}","{}","{}")'.format(k,t0,am,t))
        c.commit()
print('ho giya')
