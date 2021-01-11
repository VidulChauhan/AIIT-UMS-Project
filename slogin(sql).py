import mysql.connector as msc
c=msc.connect(host='localhost',user='root',password='mysql',database='proj_vidul')
if c.is_connected()==True:
    cur=c.cursor()
    a='Saiit'
    p='spass'
    for i in range(28,100):
        id=a+str(i)
        pa=p+str(i)
        cur.execute('insert into slogin values("{}","{}")'.format(id,pa))
        c.commit()
        print('done')
