import mysql.connector as msc
from random import *
c=msc.connect(host='localhost',user='root',password='mysql',database='proj_vidul')
if c.is_connected()==True:
    cur=c.cursor()
    cur.execute('select sid,course,year from sprofile')
    d=cur.fetchall()
    print(d)
    l=['A+','A','B+','B','C+','C','D']
    

    for i in d:
        try:

            if i[2]=='1st year':
                cur.execute('insert into marks values("{}","{}",NULL,NULL,NULL,NULL,NULL,NULL,NULL)'.format(i[0],randrange(1,100)))
                c.commit()
            if i[2]=='2nd year':
                cur.execute('insert into marks values("{}","{}","{}","{}",NULL,NULL,NULL,NULL,NULL)'.format(i[0],randrange(1,100),randrange(1,100),randrange(1,100)))
                c.commit()
            if i[2]=='3rd year':
                cur.execute('insert into marks values("{}","{}","{}","{}","{}","{}",NULL,NULL,NULL)'.format(i[0],randrange(1,100),randrange(1,100),randrange(1,100),randrange(1,100),randrange(1,100)))
                c.commit()
            if i[2]=='Final year':
                if i[1].startswith('B.TECH')==True:
                    cur.execute('insert into marks values("{}","{}","{}","{}","{}","{}","{}","{}",NULL)'.format(i[0],randrange(1,100),randrange(1,100),randrange(1,100),randrange(1,100),randrange(1,100),randrange(1,100),randrange(1,100)))
                    c.commit()
                if i[1].startswith('M.TECH')==True or i[1].startswith('M.sc')==True:
                    cur.execute('insert into marks values("{}","{}","{}","{}",NULL,NULL,NULL,NULL,NULL)'.format(i[0],randrange(1,100),randrange(1,100),randrange(1,100)))
                    c.commit()
                if i[1].startswith('B.sc')==True:
                    cur.execute('insert into marks values("{}","{}","{}","{}","{}","{}",NULL,NULL,NULL)'.format(i[0],randrange(1,100),randrange(1,100),randrange(1,100),randrange(1,100),randrange(1,100)))
                    c.commit()
                else:
                    continue    
        except:
            continue            


               
            

