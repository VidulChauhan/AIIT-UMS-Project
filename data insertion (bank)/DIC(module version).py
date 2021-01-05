def pr():
    import mysql.connector
    import random as rd
    c=mysql.connector.connect(host='localhost',user='root',password='mysql',database='project_vidul')
    if c.is_connected()==True:
        print('connected.')
        cur=c.cursor()
        cur.execute('select name from user_info')
        dat=cur.fetchall()
        cur.execute('select account_no from user_info')
        dat1=cur.fetchall()
    #print(dat)
    #print(dat1)
        list1=['sanjay','aahan','vidul','srishti','neha','rafiq','nayra','shubham','sundar','amit','rahul','neelam','zoya','sudhir','jethalal','kyra','kiara','kareena','arnav','sidhharth']
        list2=['chauhan','kumar','khan','bhardwaj','sharma','singh','gaur','yadav','gupta','garg']
        print(len(list1)*len(list2))
        for i in range(0,500):
            cur.execute('select name from user_info')
            dat=cur.fetchall()
            cur.execute('select account_no from user_info')
            dat1=cur.fetchall()
            e1=rd.choice(list1)
            e2=rd.choice(list2)
            n=e1+' '+e2#yaha naam bana
            nt=('{}'.format(n),)#matching ke liye
        #print(nt)
            an=rd.randrange(12345678,9876543210)#yaha acc_no bana
            ant=('{}'.format(an),)#matching ke liye
        #print(ant)
            d1=rd.randint(1990,2020)
            d2=rd.randint(1,12)
            d3=rd.randint(1,30)
            d=str(d1)+'-'+str(d2)+'-'+str(d3)#date bani
            dt=('{}'.format(d),)
        #print(dt)
        
        #print(dat[0][0],dat1[0][0])
            if nt not in dat and ant not in dat1:
                cur.execute('insert into user_info values("{}","{}","{}")'.format(n,an,d))
                c.commit()
            #print('yes')
            else:
             #print('noe')
                continue
        cur.execute('select * from user_info')
        q=cur.fetchall()
        print(len(q))
