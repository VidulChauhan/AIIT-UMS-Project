import mysql.connector as msc
from random import *
from datetime import *
c=msc.connect(host='localhost',user='root',password='mysql',database='proj_vidul')
if c.is_connected()==True:
    cur=c.cursor()
    cur.execute('select sid from sprofile')
    d1=cur.fetchall()
    
    #cur.execute('create table if not exists ')
    m1=['Practical file','3d demonstration of geometry','Prussian mathematics : Background']
    p1=['Investigatory project : Physics','Miniature petrol engine build','Demonstation of particle acceleration','Newtonian Physics']
    c1=['Investigatory project : Chemistry','Exploring liquid Nitrogen','Explaning Thermodynamics']
    cs=['Android application','IOS application','Developing an AI assistant',"Integrating AI's into mainstream softwares"]
    n1=['Exploring dark matter : philosophy','Making Gold nanoparticles from scrap','What is Time : philosophy']
    lis=[m1,p1,c1,cs,n1]
    dat=date(2020,11,29)

    def cr():
        while True:
            r=choice(lis)
            r1=choice(r)
            day=randint(15,110)
            dat1=dat+timedelta(days=day)
            rec=r1+','+str(dat1)
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
                l.append('NULL,NULL')
        if len(l)==5:
            #cur=c.cursor()
            cur.execute('insert into projects values("{}","{}","{}","{}","{}","{}")'.format(i[0],l[0],l[1],l[2],l[3],l[4]))
            c.commit()
            print('done')

            
