import mysql.connector as mc
from random import *
import sys
c=mc.connect(host='localhost',user='root', password ='mysql',database='proj_vidul')
if c.is_connected()==True:
    cur=c.cursor()
    cur.execute('create table if not exists  att1(sid varchar(10) primary key,present varchar(4) NOT NULL)')
    cur.execute('select sid from sprofile')
    d1=cur.fetchall()
    cur.execute('select sid from att1')
    d2=cur.fetchall()
    
    #print(d1)
    #total days i am taking 180
    def a1():
        count=0
        while True:  #for low 60-75%  
            try:    
                r=choice(d1)
                r2=randint(108,134)
                if r not in d2 :
                    cur.execute('insert into att1 values("{}","{}")'.format(r[0],r2))
                    c.commit()
                    print('done')
                    count+=1
                if count==14:
                    break
                else:
                    continue
            except:
                print('error')
                continue
        #sys.exit()
    def a2():
        c5=0    
        while True:# for critical  45-60%    
                try:    
                    r3=choice(d1)
                    r4=randint(81,107)
                    if r3 not in d2 :
                        cur.execute('insert into att1 values("{}","{}")'.format(r3[0],r4))
                        c.commit()
                        print('done')
                        c5+=1
                    if c5==7:
                        break
                    else:
                        continue
                except:
                    print('error')
                    continue
        
    def a3():            
        c1=0
        while True: #for adequate 75-90%   
                try:    
                    r5=choice(d1)
                    r6=randint(135,162)
                    if r5 not in d2 :
                        cur.execute('insert into att1 values("{}","{}")'.format(r5[0],r6))
                        c.commit()
                        print('done')
                        c1+=1
                    if c1==38:
                        break
                    else:
                        continue
                except:
                    print('error')
                    continue                    
        
    def a4():            
        c2=0
        while True: # for good 90-100%
                try:    
                    r7=choice(d1)
                    r8=randint(163,180)
                    if r7 not in d2 :
                        cur.execute('insert into att1 values("{}","{}")'.format(r7[0],r8))
                        c.commit()
                        print('done')
                        c2+=1
                    if c2==14:
                        break 
                    else:
                        continue
                except:
                    print('error')
                    continue                           
        
    a1()   
    a2()
    a3()
    a4() 
            
