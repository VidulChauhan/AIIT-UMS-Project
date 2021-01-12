import mysql.connector as mc
from random import *
c=mc.connect(host='localhost',user='root', password ='mysql',database='proj_vidul')
id='Saiit'
pas='spass'
id2='Taiit'
pas2='tpass'

if c.is_connected()==True:
    cur=c.cursor()
    cur.execute('select sph,fph,mph from sprofile')
    dat=cur.fetchall()

 
    
   
    for i in range(35,90):#tlogin
        try:
            

           
            ph=randrange(7512345968,9873645194)
            tid=id2 + str(i)
            tkey=pas2+ str(i)
            rec=(tid,tkey,ph)
            for j in dat:
                if ph not in j:
                    cur.execute('insert into adminlogin values("{}","{}",{})'.format(tid,tkey,ph))
                    c.commit()
                    print('ye hogaya')
        except:
            print('nahi hua ye ')
            continue    
    print('done')
        

