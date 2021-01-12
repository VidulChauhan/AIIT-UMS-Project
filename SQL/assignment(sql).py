import mysql.connector as msc
from random import *
from datetime import *
c=msc.connect(host='localhost',user='root',password='mysql',database='proj_vidul')
if c.is_connected()==True:
    cur=c.cursor()
    cur.execute('select sid from sprofile')
    d1=cur.fetchall()