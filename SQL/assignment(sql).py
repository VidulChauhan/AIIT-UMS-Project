import mysql.connector as msc
from random import *
from datetime import *
c=msc.connect(host='localhost',user='root',password='mysql',database='proj_vidul')
if c.is_connected()==True:
    cur=c.cursor()
    cur.execute('select sid from sprofile')
    d1=cur.fetchall()
    a=['Calculus-I','Calculus-II','Complex Algebra','Linear Programming','3d geometry','Inverse functions',
    'Fluids-I','Fluids-II','Kinematics','Force','Rotation','Gravitation',
    'Chemical kinetics-II','Coordination complexes','Organic chemistry-I','Organic chemistry-II','Organic chemistry-III'
    ,'Organic chemistry-IV','Data structures','Algorithms','Problem-Solving-II']

    dat=date(2020,10,29)


    def cr():
        while True:
            r1=choices(a,k=1)[0]
            day1=randint(20,40)
            day2=randint(25,50)
            dat1=dat+timedelta(days=day1)
            dat2=dat1+timedelta(days=day2)
            rec=r1+','+str(dat1)+','+str(dat2)
            if l.count(rec)==0:
                return rec 
            if l.count(rec)!=0:
                continue
    for i in d1:        
        q=randint(1,5)
        l=[]
        for k in range(q):
            e=cr()
            l.append(e)        
        if len(l)!=5:
            for h in range(5-len(l)):
                l.append('NULL,NULL,NULL')
        if len(l)==5:
            #cur=c.cursor()
            print(l)
            cur.execute('insert into assignments values("{}","{}","{}","{}","{}","{}")'.format(i[0],l[0],l[1],l[2],l[3],l[4]))
            c.commit()
            print('done')
        
    