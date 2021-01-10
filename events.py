import mysql.connector as mc
from random import *
c=mc.connect(host='localhost',user='root', password ='mysql',database='proj_vidul')
if c.is_connected()==True:
    cur=c.cursor()
    