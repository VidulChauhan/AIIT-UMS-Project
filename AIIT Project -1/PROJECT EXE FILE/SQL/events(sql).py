import mysql.connector as mc
from random import *
c=mc.connect(host='localhost',user='root', password ='mysql',database='proj_vidul')
if c.is_connected()==True:
    cur=c.cursor()
    cur.execute('create table if not exists events(Eid varchar(5) NOT NULL,event varchar(1500) NOT NULL,date date);')
    events=[('E01','Pre-final optional tests to be conducted in march, for further details contact examination committee','2020-12-16'),
    ('E02','The Techfest 2020 is postponed due to Covid-19, new dates will be announced soon.','2020-11-29'),
    ('E03',('Students are requested to go through the new guidelines for the code of the conduct during this pandemic, '
    'issued by the STC (Student welfare committee) listed on every online platform and also individually sent to students rooms in circulars '),'2021-01-01'),
    ('E04','All hostels will be fumigated on 15th january, kindly cooperate with the concerned staff.','2020-01-05'),
    ('E05',('All students are invited to join the online assembly to kickstart a energetic new year, 2021. more details'
    ' are shared on corresponding discord channels and groups.'),'2020-01-02')]
    for i in events:
        cur.execute('insert into events values("{}","{}","{}")'.format(i[0],i[1],i[2])) 
        c.commit()  
    print('done bro')     