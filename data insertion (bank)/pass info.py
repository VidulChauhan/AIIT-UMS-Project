import  mysql.connector
import random as rd
c=mysql.connector.connect(host='localhost',user='root',password='mysql',database='proj_vidul')
if c.is_connected()==True:
    cur=c.cursor()
    cur.execute('select name from main_info')
    dat=cur.fetchall()
    cur.execute('select name from pass_info')
    dat1=cur.fetchall()
    #print(dat1[0])
    #list1=['vidul chauhan','shubham kumar','neha sharma','arnav sharma']
    for i in dat:
        print(i)
        if i not in dat1:
            n=i[0].split()
            p= n[0]+n[1][0]+'12'
            cur.execute('insert into pass_info values("{}",NULL,"{}")'.format((i[0]),p))
            c.commit()
        
    print('done.')      
            
        
        
        #print(n)
        #print(p)
        
        #a=rd.random
        #cur.execute()
        
    
