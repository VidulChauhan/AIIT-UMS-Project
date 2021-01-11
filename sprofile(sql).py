import mysql.connector as msc
from random import *
from tkinter import messagebox
c=msc.connect(host='localhost',user='root',password='mysql',database='proj_vidul')
if c.is_connected()==True:
    cur=c.cursor()


    cur.execute('select sid,addm_no from sprofile')
    s1=cur.fetchall()
    for i in s1:
        cur.execute('update sprofile set addm_no="{}" where sid="{}"'.format(('S'+i[1][1:]),i[0]))
        print('S'+i[1][1:],i[0])
        c.commit()
messagebox.showinfo('','done.')

              
                           



    

