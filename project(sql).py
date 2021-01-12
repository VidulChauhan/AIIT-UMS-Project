import mysql.connector as msc
from random import *
c=msc.connect(host='localhost',user='root',password='mysql',database='proj_vidul')
if c.is_connected()==True:
    cur=c.cursor()
    cur.execute('select sid from sprofile')
    d1=cur.fetchall()
    m=['Practical file','3d demonstration of geometry','Prussian mathematics']
    p=['Investigatory project','Miniature petrol engine build','Demonstation of particle acceleration','Newtonian Physics']
    c=['Investigatory project','Exploring liquid Nitrogen','Explaning Equilibrium']
    cs=['Android application','IOS application','']