try:
    #import start
    import mysql.connector as db                    ### EXTERNAL INSTALL ###     
    from random import *
    import time as t
    from tkinter import *   
    ph=PhotoImage
    lb=Label
    bt=Button
    fr=Frame
    ent=Entry
    from tkinter import messagebox
    msgb=messagebox   
    tx=Text       
    msg=Message
    cv=Canvas
    from datetime import *
    dt=datetime    
    day=dt.now().strftime('%A')
    month=dt.now().strftime('%B')
    DD=str(dt.now().day)
    YY=str(dt.now().year)
    DATE=day+', '+DD+' '+month+' '+YY
    curtime=dt.now().time()

    ##############  MAIN WINDOW   ############## 

    win=Tk()
    width=int(((win.winfo_screenwidth()*0.9875)//2)-575)
    height=int(((win.winfo_screenheight()*0.95)//2)-325)
    win.geometry('1150x650+{}+{}'.format(width,height))
    win.title('Advanced Institute of Innovation and Technology')
    win.configure(bg='#000000')
    win.resizable(False,False)

    p=ph(file = 'images/titlelogo.png')
    p1=ph(file = 'images/main.png')
    p2=ph(file = 'images/loginbutton1.png') 
    p3=ph(file = 'images/loginbutton2.png')
    p6=ph(file = 'images/divbar.png')
    p7=ph(file = 'images/gobutton.png') 
    p8=ph(file = 'images/backbutton.png')
    p9=ph(file = 'images/aiit.png')
    p10=ph(file = 'images/signout.png')
    p11=ph(file = 'images/profile2.png')
    p12=ph(file = 'images/assignments2.png')
    p13=ph(file = 'images/fee2.png')
    p14=ph(file = 'images/projects2.png')
    p15=ph(file = 'images/events2.png')
    p16=ph(file = 'images/attendance2.png')
    p17=ph(file = 'images/about2.png')
    p18=ph(file = 'images/marks2.png')
    p19=ph(file = 'images/passreset2.png')
    p20=ph(file = 'images/hb.png')
    p21=ph(file = 'images/loginbg2.png')
    p23=ph(file = 'images/loginbarbg.png')
    p24=ph(file = 'images/sidbar.png')
    p25=ph(file = 'images/profilebg.png')
    p26=ph(file = 'images/boyicon.png')
    p27=ph(file = 'images/girlicon.png')
    p28=ph(file = 'images/editbutton.png')
    p29=ph(file = 'images/abtbg.png')
    p30=ph(file = 'images/apassr.png')
    p32=ph(file = 'images/spassr.png')
    p33=ph(file = 'images/txbar bg.png')
    p34=ph(file = 'images/marksbg.png')
    p35=ph(file = 'images/+admin.png')
    p36=ph(file = 'images/+student.png')
    p37=ph(file = 'images/paid1.png')
    p38=ph(file = 'images/paid2.png')
    p39=ph(file = 'images/paid3.png')
    p40=ph(file = 'images/eventbg.png')
    p41=ph(file = 'images/chartlegend.png')
    p42=ph(file = 'images/projectbg.png')
    p43=ph(file = 'images/assignmentbg.png')
    p44=ph(file = 'images/smallbar(lightbrown).png')
    p45=ph(file = 'images/txbar(small).png')
    p46=ph(file = 'images/txbar(lightbrown).png')
    p48=ph(file = 'images/-administrator.png')
    p49=ph(file = 'images/-student.png')
    p50=ph(file = 'images/smallbar(black).png')
    p51=ph(file = 'images/savebt.png')
    p52=ph(file = 'images/cancelbt.png')
    
    #title bar icon change

    win.iconphoto(None,p)

    global str_date
    def str_date(a):
        a=a.split('-')
        return date(int(a[0]),int(a[1]),int(a[2]))

##################################################################### MINOR ANIMATIONS ###########################################################
    
    from PIL import ImageTk,Image
    def ZOOM(img):
        path=img.cget('file')
        image=Image.open(path)    
        image1=ImageTk.PhotoImage(image)
        width=round(image1.width()+(0.035*image1.width()))
        height=round(image1.height()+(0.035*image1.height()))
        zoom_image=image.resize((width,height),Image.ANTIALIAS)
        new_image=ImageTk.PhotoImage(zoom_image)
        return new_image
    
    global ANIMATE
    def ANIMATE(b,img):
        def zoom(i):
            image=ZOOM(img)
            b.configure(image=image)
            b.image=image
        def reverse(i):
            b.configure(image=img)
            b.image=img
        b.bind('<Enter>',zoom)
        b.bind('<Leave>',reverse)

                                            ###############################################################
#############################################################         ADMIN SIDE        ###########################################################
                                            ###############################################################
    
    def adminhome():#####################################################################  COMPLETED #############################################################
        f1.place_forget()

        global f2
        f2=fr(win,bd=0,height=650,width=1150,bg='#000000')#bigger one
        f2.place(relx=0.5,rely=0.5,anchor='center') 

        global f3
        f3=fr(win,bd=0,height=100,width=1150,bg='#232323')#smaller one OVER F2
        f3.place(relx=0.5,rely=0,anchor='center')       

        l28=lb(f3,text=DATE,bd=0,font=('SF Pro Display',13),bg='#232323',fg='#FFFFFF') 
        l28.place(relx=0.715,rely=0.755,anchor='center')

        l29=lb(f2,bd=0,bg='#000000',fg='#FFFFFF',font=('SF Pro Display',22,'bold'))
        l29.place(relx=0.5,rely=0.105,anchor='center')

        #####################  GREETING ACCORDING TO TIME ####################

        if curtime>=time(0,00,00) and curtime<time(11,59,59):
            l29.configure(text='Good morning !')
        if curtime>=time(12,00,00) and curtime<time(17,59,59):
            l29.configure(text='Good afternoon !')
        if curtime>=time(18,00,00) and curtime<time(23,59,59):
            l29.configure(text='Good evening !')       
        
        l5=lb(f3,image = p9,bd=0)
        l5.place(relx=0.05,rely=0.75,anchor = 'center')

        b6=bt(f3,image=p10,bd=0,bg='#232323',activebackground = '#232323',command = main)
        b6.place(relx=0.95,rely=0.75,anchor = 'center')
        ANIMATE(b6,p10)

        global f4
        f4=fr(f2,height=520,width=875,bd=0,bg='#000000') # OVER F2 BELOW F3
        f4.place(relx=0.5,rely=0.535,anchor='center')

        b7=bt(f4,image=p11,bd=0,bg='#000000',activebackground='#000000',command=sprofile) # profile
        b7.place(relx=0.1385,rely=0.236,anchor='center')
        ANIMATE(b7,p11)

        b8=bt(f4,image=p12,bd=0,bg='#000000',activebackground='#000000',command=assignments) #assignments
        b8.place(relx=0.466,rely=0.688,anchor='center')
        ANIMATE(b8,p12)
        
        b9=bt(f4,image=p14,bd=0,bg='#000000',activebackground='#000000',command=projects) # projects
        b9.place(relx=0.392,rely=0.182,anchor='center')
        ANIMATE(b9,p14)

        b10=bt(f4,image=p18,bd=0,bg='#000000',activebackground='#000000',command=marks) # marks
        b10.place(relx=0.7515,rely=0.182,anchor='center')
        ANIMATE(b10,p18)

        b11=bt(f4,image=p16,bd=0,bg='#000000',activebackground='#000000',command=attendance) # attendance
        b11.place(relx=0.13855,rely=0.62,anchor='center')
        ANIMATE(b11,p16)

        b12=bt(f4,image=p15,bd=0,bg='#000000',activebackground='#000000',command=events) # events
        b12.place(relx=0.13855,rely=0.8825,anchor='center')
        ANIMATE(b12,p15)

        b13=bt(f4,image=p19,bd=0,bg='#000000',activebackground='#000000',command=passr) # passreset
        b13.place(relx=0.738,rely=0.52,anchor='center')
        ANIMATE(b13,p19)

        b14=bt(f4,image=p17,bd=0,bg='#000000',activebackground='#000000',command=about) # about
        b14.place(relx=0.912,rely=0.52,anchor='center')
        ANIMATE(b14,p17)
        
        b15=bt(f4,image=p13,bd=0,bg='#000000',activebackground='#000000',command=fee_details) # fee
        b15.place(relx=0.8263,rely=0.828,anchor='center')
        ANIMATE(b15,p13)

        b16=bt(f3,image=p20,bd=0,bg='#232323',activebackground ='#232323',command=adminhome) # adminhome button
        b16.place(relx=0.5,rely=0.75,anchor='center')
        ANIMATE(b16,p20)

        b39=bt(f2,image=p35,bd=0,bg='#000000',activebackground='#000000',command=addadmin) # add administrator 
        b39.place(relx=0.01,rely=0.115,anchor='w')
        ANIMATE(b39,p35)

        b40=bt(f2,image=p36,bd=0,bg='#000000',activebackground='#000000',command=addstudent) # add student
        b40.place(relx=0.01,rely=0.175,anchor='w')
        ANIMATE(b40,p36)

        def delstudent():
            lb(f2,image = p50,bd=0).place(relx=0.9375,rely=0.5,anchor='center')

            global dsid   ###   0.235 ---> rely
            dsid=ent(f2,bd=0,bg='#FFFFFF',font=('SF Pro Display',12),width=6)# ID 
            dsid.place(relx=0.9375,rely=0.5,anchor='center')
            dsid.insert(0,'Enter ID') 

            dbcur.execute('select id from slogin')
            d20=dbcur.fetchall()    
        
            def del1():
                a=0
                if dsid.get()=='' or dsid.get()=='Enter ID':
                    msgb.showwarning('Invalid entry',   'Please enter ID.   ')
                    a+=1
                if (dsid.get()!='' and dsid.get()!='Enter ID') and ((dsid.get(),) not in d20):
                    msgb.showwarning('Invalid entry',   'Please enter valid ID.   ')
                    a+=1
                else:
                    if (a==0) and ((dsid.get(),) in d20):
                        try:
                            dbcur.execute('delete from sprofile where sid="{}"'.format(dsid.get()))
                            dbcur.execute('delete from marks where sid="{}"'.format(dsid.get()))
                            dbcur.execute('delete from slogin where id="{}"'.format(dsid.get()))
                            dbcur.execute('delete from projects where sid="{}"'.format(dsid.get()))
                            dbcur.execute('delete from attendance where sid="{}"'.format(dsid.get()))
                            dbcur.execute('delete from fees where sid="{}"'.format(dsid.get()))
                            dbcur.execute('delete from assignments where sid="{}"'.format(dsid.get()))
                            dbcon.commit()
                            msgb.showinfo('Message','Account deleted successfully.')
                            adminhome()
                        except :
                            msgb.showwarning('Unexpected error','There was an error deleting that account\nPlease try again later.')
                            adminhome()

            bt(f2,text='delete',bd=0,bg='#000000',fg='#CF3327',font=('SF Pro Display',12),activebackground='#000000',command=del1).place(                
                relx=0.9377,rely=0.55,anchor='w')

            bt(f2,text='cancel',bd=0,bg='#000000',fg='#FFFFFF',font=('SF Pro Display',12),activebackground='#000000',command=adminhome).place(
                relx=0.9373,rely=0.55,anchor='e')

        def deladmin():
            lb(f2,image = p50,bd=0).place(relx=0.9375,rely=0.5,anchor='center')

            global daid 
            daid=ent(f2,bd=0,bg='#FFFFFF',font=('SF Pro Display',12),width=6)# ID 
            daid.place(relx=0.9375,rely=0.5,anchor='center')
            daid.insert(0,'Enter ID') 

            dbcur.execute('select id from adminlogin')
            d21=dbcur.fetchall() 

            def del2():
                a=0
                if daid.get()=='' or daid.get()=='Enter ID':
                    msgb.showwarning('Invalid entry',   'Please enter ID.   ')
                    a+=1
                if (daid.get()!='' and daid.get()!='Enter ID') and ((daid.get(),) not in d21):
                    msgb.showwarning('Invalid entry',   'Please enter valid ID.   ')
                    a+=1
                else:                       
                    if (a==0) and ((daid.get(),) in d21):
                        if (daid.get()==aid.get()):
                            msgb.showwarning('Message','Please login from another ID to delete this one.')
                            adminhome()
                        else:
                            try:
                                dbcur.execute('delete from adminlogin where id="{}"'.format(daid.get()))
                                dbcon.commit()
                                msgb.showinfo('Message','Account deleted successfully.')
                                adminhome()
                            except:
                                msgb.showwarning('Unexpected error','There was an error deleting that account\nPlease try again later.')
                                adminhome()

            bt(f2,text='delete',bd=0,bg='#000000',fg='#CF3327',font=('SF Pro Display',12),activebackground='#000000',command=del2).place(                
                relx=0.9377,rely=0.55,anchor='w')  

            bt(f2,text='cancel',bd=0,bg='#000000',fg='#FFFFFF',font=('SF Pro Display',12),activebackground='#000000',command=adminhome).place(
                relx=0.9373,rely=0.55,anchor='e')
        
        b57=bt(f2,image=p48,bd=0,bg='#000000',activebackground='#000000',command=deladmin)
        b57.place(relx=0.99,rely=0.115,anchor='e')
        ANIMATE(b57,p48)

        b58=bt(f2,image=p49,bd=0,bg='#000000',activebackground='#000000',command=delstudent)
        b58.place(relx=0.99,rely=0.175,anchor='e')
        ANIMATE(b58,p49)

        l11=lb(f3,image=p24,bd=0)
        l11.place(relx=0.35,rely=0.75,anchor='center')

        l12=lb(f3,text='Student ID ',font=('SF Pro Display',13),bd=0,bg='#232323',fg='#FFFFFF')
        l12.place(relx=0.275,rely=0.75,anchor='center')

        global sid
        sid=ent(f3,bd=0,font=('SF Pro Display',13),width=6)# sid for profile
        sid.place(relx=0.35,rely=0.75,anchor='center')


    def addstudent():  ###########################################  COMPLETED  ###############################################################
        f4.place_forget()
        global f12
        f12=fr(f2,height=500,width=855,bd=0,bg='#000000') 
        f12.place(relx=0.5,rely=0.535,anchor='center')

        l6=lb(f12,text='Add Student account',font=('SF Pro Display',38,'bold'),bd=0,bg='#000000', fg='#FFFFFF')
        l6.place(relx=0,rely=0.05,anchor='w')     

        l83=lb(f12,image=p25,bd=0)            
        l83.place(relx=0.5,rely=0.55,anchor='center')
    
        lb(f12,image = p33,bd=0).place(relx=0.29,rely=0.29,anchor='w')
        s1=ent(f12,bd=0,bg='#F2F2F2',font=('SF Pro Display',14),width=13) # for student name
        s1.place(relx=0.298,rely=0.29,anchor='w')        
        
        lb(f12,image = p33,bd=0).place(relx=0.29,rely=0.383,anchor='w')
        s2=ent(f12,bd=0,bg='#F2F2F2',font=('SF Pro Display',14),width=13) # for student mobile
        s2.place(relx=0.298,rely=0.383,anchor='w')
        
        lb(f12,image = p33,bd=0).place(relx=0.29,rely=0.475,anchor='w')
        s3=ent(f12,bd=0,bg='#F2F2F2',font=('SF Pro Display',14),width=13) # for current year
        s3.place(relx=0.298,rely=0.475,anchor='w')        
        
        lb(f12,image = p33,bd=0).place(relx=0.6925,rely=0.29,anchor='w')
        s4=ent(f12,bd=0,bg='#F2F2F2',font=('SF Pro Display',14),width=13) # for student admission
        s4.place(relx=0.7005,rely=0.29,anchor='w')        
        
        lb(f12,image = p33,bd=0).place(relx=0.6925,rely=0.383,anchor='w')
        s5=ent(f12,bd=0,bg='#F2F2F2',font=('SF Pro Display',14),width=13) # for course
        s5.place(relx=0.7005,rely=0.383,anchor='w')
                
        lb(f12,image = p44,bd=0).place(relx=0.825,rely=0.473,anchor='w')
        s6=ent(f12,bd=0,bg='#F2F2F2',font=('SF Pro Display',14),width=7) # for blood group
        s6.place(relx=0.833,rely=0.473,anchor='w')
        
        lb(f12,image = p44,bd=0).place(relx=0.095,rely=0.485,anchor='center')
        s7=ent(f12,bd=0,bg='#F2F2F2',font=('SF Pro Display',14),width=6) # for gender
        s7.place(relx=0.095,rely=0.485,anchor='center')
        s7.insert(0,'M/F')
        
        lb(f12,image = p33,bd=0).place(relx=0.29,rely=0.688,anchor='w')
        s8=ent(f12,bd=0,bg='#F2F2F2',font=('SF Pro Display',14),width=13) # for father's name
        s8.place(relx=0.298,rely=0.688,anchor='w')        
        
        lb(f12,image = p33,bd=0).place(relx=0.29,rely=0.782,anchor='w')
        s9=ent(f12,bd=0,bg='#F2F2F2',font=('SF Pro Display',14),width=13) # father's number
        s9.place(relx=0.298,rely=0.782,anchor='w')       
        
        lb(f12,image = p33,bd=0).place(relx=0.78,rely=0.688,anchor='w')
        s10=ent(f12,bd=0,bg='#F2F2F2',font=('SF Pro Display',14),width=13) # for mother's name
        s10.place(relx=0.788,rely=0.688,anchor='w')        

        lb(f12,image = p33,bd=0).place(relx=0.78,rely=0.782,anchor='w')
        s11=ent(f12,bd=0,bg='#F2F2F2',font=('SF Pro Display',14),width=13) # mother's number
        s11.place(relx=0.788,rely=0.782,anchor='w')        
        
        lb(f12,image = p44,bd=0).place(relx=0.5425,rely=0.473,anchor='w')
        s12=ent(f12,bd=0,bg='#F2F2F2',font=('SF Pro Display',14),width=7) # ID 
        s12.place(relx=0.5505,rely=0.473,anchor='w')        

        def nstudent_save():            
            a=0
            b=0
            d=0
            ad=0
            sg=0
            e=0
            s=0
            sget=[s1.get(),s2.get(),s3.get(),s4.get(),s5.get(),
                s6.get(),s7.get(),s8.get(),s9.get(),s10.get(),
                s11.get(),s12.get()]
            l=['1st year','2nd year','3rd year','Final year']
            l2=['+A','+B','+O','-O','+AB','-AB','-A','-B']           
            dbcur.execute('select * from sprofile')
            global d11
            d11=dbcur.fetchall()
            for g in sget:
                if g=='':
                    sg+=1
            for c in s1.get(): # sname checked.
                if c.isdigit()==True:
                    a+=1
            for c1 in s8.get(): # fname checked.
                if c1.isdigit()==True:
                    a+=1
            for c2 in s10.get(): # mname checked.
                if c2.isdigit()==True:
                    a+=1                  
            for no in s2.get(): # sph cheked.
                if no.isdigit()!=True:
                    b+=1 
            for no1 in s9.get(): # fph cheked.
                if no1.isdigit()!=True:
                    b+=1
            for no2 in s11.get(): # mph checked.
                if no2.isdigit()!=True:
                    b+=1              
            for w1 in s5.get(): # course checked.
                if w1.isdigit()==True:
                    d+=1
            for i1 in s12.get()[5:]:
                if i1 in list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'):
                    s+=1
            for a1 in s4.get()[1:]:
                if a1 in list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'):
                    ad+=1

            if sg!=0:
                msgb.showwarning('Invalid entry','Please enter data in all fields before saving.')                
            if sg==0:                    
                if s12.get().startswith('Saiit')==False or s!=0:
                    msgb.showwarning("Invalid entry","Please enter valid ID.\nIt should start with 'Saiit',\nand should have a relevant unique number suffixed")        
                    e+=1
                if a!=0:
                    msgb.showwarning('Invalid entry','Names cannot contain numbers, please try again.')
                    e+=1
                if len(s2.get())!=10 or len(s9.get())!=10 or len(s11.get())!=10 or b!=0:
                    msgb.showwarning('Invalid entry','Phone number is invalid, please try again.') 
                    e+=1               
                if s3.get() not in l: #year checked.
                    msgb.showwarning('Invalid entry','    Please check year.    ')   
                    e+=1         
                if s4.get().startswith('S')==False or ad!=0:    # admission number checked                
                    msgb.showwarning('Invalid entry',"Admission number is not valid,\nIt can only begin with a 'S'\nPlease try again.")
                    e+=1                
                if d!=0:   
                    msgb.showwarning('Invalid entry','Course is not valid, please try again.')   
                    e+=1             
                if s6.get() not in l2: # blood group checked.
                    msgb.showwarning('Invalid entry','Please check blood group and try again.') 
                    e+=1               
                if s7.get() not in ['male','female','Male','Female','M','F','m','f']:   # gender checked.
                    msgb.showwarning('Invalid entry','Please check gender and try again.')
                    e+=1
                else:
                    if tuple(sget) in d11:
                        msgb.showwarning('Repeated entry','This record already exists. ')
                    if tuple(sget) not in d11 and e==0:                        
                        try:                       
                            dbcur.execute("insert into sprofile values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')"
                            .format(
                                s12.get(),
                                s4.get(),
                                s1.get(),
                                s8.get(),
                                s10.get(),
                                s2.get(),                                 
                                s9.get(),
                                s11.get(),
                                s5.get(),
                                s3.get(),
                                s7.get(),
                                s6.get())) 
                            dbcur.execute("insert into marks values('{}','NULL','NULL','NULL','NULL','NULL','NULL','NULL','NULL')".format(s12.get()))
                            dbcur.execute('insert into slogin values("{}","NULL")'.format(s12.get()))
                            dbcur.execute('insert into fees values("{}","NULL","NULL","NULL","NULL")'.format(s12.get()))
                            dbcur.execute('insert into projects values("{}","NULL,NULL","NULL,NULL","NULL,NULL","NULL,NULL","NULL,NULL")'.format(s12.get()))
                            dbcur.execute('insert into attendance values("{}","NULL")'.format(s12.get()))
                            dbcur.execute('insert into assignments values("{}","NULL,NULL,NULL","NULL,NULL,NULL","NULL,NULL,NULL","NULL,NULL,NULL","NULL,NULL,NULL")'.format(s12.get()))
                            dbcon.commit()
                            msgb.showinfo('Message','Account added successfully.')
                            msgb.showinfo('Message','Since this will be a new account, therefore all other data branches such as password,assignments,attendance,etc are also not set-up.\n'
                                        'For now, all information regarding acedemics including credentials has been set to NULL.\n'
                                        'You can change this in the future. ')
                            adminhome()
                        except:
                            msgb.showwarning('Unexpected error','Please check all fields or try again later.')

        b41=bt(f12,image=p51,bd=0,font=('SF Pro Display',15),bg='#000000',fg='#249ADF',activebackground='#000000',command=nstudent_save)
        b41.place(relx=0.95,rely=0.1,anchor='center')
        ANIMATE(b41,p51)

        b42=bt(f12,image=p52,bd=0,font=('sf pro display',15),bg='#000000',fg='#CF3327',activebackground='#000000',command=adminhome)  
        b42.place(relx=0.85,rely=0.1,anchor='center')
        ANIMATE(b42,p52)


    def addadmin(): ######################################################################### COMPLETED ###########################################################
        dbcur.execute('select * from adminlogin')
        d12=dbcur.fetchall()        
        f4.place_forget()
        global f13
        f13=fr(f2,height=500,width=855,bd=0,bg='#000000') 
        f13.place(relx=0.5,rely=0.535,anchor='center')
        
        l6=lb(f13,text='Add Administrator account',font=('SF Pro Display',38,'bold'),bd=0,bg='#000000', fg='#FFFFFF')
        l6.place(relx=0,rely=0.05,anchor='w')     

        l84=lb(f13,image=p29,bd=0)            
        l84.place(relx=0.5,rely=0.55,anchor='center')

        l85=lb(f13,text='ID',bd=0,font=('SF Pro Display',15),bg='#232323',fg='#249ADF')
        l85.place(relx=0.2,rely=0.3,anchor='w')

        l85=lb(f13,text='Phone number :',bd=0,font=('SF Pro Display',16),bg='#232323',fg='#249ADF')
        l85.place(relx=0.2,rely=0.4,anchor='w')

        l86=lb(f13,text='New password :',bd=0,font=('SF Pro Display',16),bg='#232323',fg='#249ADF')
        l86.place(relx=0.2,rely=0.5,anchor='w')

        l87=lb(f13,text='Confirm new password :',bd=0,font=('SF Pro Display',16),bg='#232323',fg='#249ADF')
        l87.place(relx=0.2,rely=0.6,anchor='w')

        l88=lb(f13,image=p33,bd=0)
        l89=lb(f13,image=p33,bd=0)
        l90=lb(f13,image=p33,bd=0)
        l91=lb(f13,image=p33,bd=0)
        l91.place(relx=0.45,rely=0.3,anchor='w')
        l88.place(relx=0.45,rely=0.4,anchor='w')
        l89.place(relx=0.45,rely=0.5,anchor='w')
        l90.place(relx=0.45,rely=0.6,anchor='w')
        
        tid=ent(f13,bd=0,bg='#F2F2F2',font=('SF Pro Display',16),width=10)
        tid.place(relx=0.475,rely=0.3,anchor='w')

        phno=ent(f13,bd=0,bg='#F2F2F2',font=('SF Pro Display',16),width=10) # ph
        phno.place(relx=0.475,rely=0.4,anchor='w')

        napass=ent(f13,bd=0,bg='#F2F2F2',font=('SF Pro Display',16),width=10) # new
        napass.place(relx=0.475,rely=0.5,anchor='w')

        cnapass=ent(f13,bd=0,bg='#F2F2F2',font=('SF Pro Display',16),width=10) # new confirmed
        cnapass.place(relx=0.475,rely=0.6,anchor='w')

        def nadmin_save():
            a=0
            c=0
            aget=[tid.get(),phno.get(),napass.get(),cnapass.get()]
            a1get=[tid.get(),phno.get(),napass.get()]
            for i in aget:
                if i=='':
                    c+=1
            if c!=0:
                msgb.showwarning('Entry error','Please fill all fields.')
            if c==0:
                if (tid.get().startswith('Taiit')==False) :
                    a+=1
                for k in tid.get()[5:]:
                    if k in list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'):
                        a+=1
                for j in phno.get():
                    if j.isdigit()==False:
                        a+=1
                if len(phno.get())!=10:
                    a+=1
                if a!=0:
                    msgb.showwarning('Entry error','Please check all fields and try again.')
                if a==0:
                    if napass.get()!=cnapass.get():
                        msgb.showwarning('Key error','Entered paswords do not match.\nPlease try again.')
                    if napass.get()==cnapass.get():
                        if tuple(a1get) in d12:
                            msgb.showwarning('Repeated entry','This record already exists.')
                        if tuple(a1get) not in d12 :
                            try:                        
                                dbcur.execute('insert into adminlogin values("{}","{}","{}")'.format(tid.get(),cnapass.get(),phno.get()))
                                dbcon.commit()
                                msgb.showinfo('Message','Account added successfully.')
                                adminhome()
                            except:
                                msgb.showwarning('Unexpected error','Please check all fields or try again later.')

                
        b43=bt(f13,image=p51,bd=0,font=('SF Pro Display',15),bg='#000000',fg='#249ADF',activebackground='#000000',command=nadmin_save)
        b43.place(relx=0.95,rely=0.0875,anchor='center') 
        ANIMATE(b43,p51)

        b44=bt(f13,image=p52,bd=0,font=('sf pro display',15),bg='#000000',fg='#CF3327',activebackground='#000000',command=adminhome)  
        b44.place(relx=0.85,rely=0.0875,anchor='center')  
        ANIMATE(b44,p52)
    

    def forgpass():#####################################################################  COMPLETED  #############################################################
        f1.place_forget()
        fram=fr(win,height=650,width=1150,bd=0,bg='#000000')
        fram.place(relx=0.5,rely=0.5,anchor='center')

        global f8
        f8=fr(fram,height=500,width=855,bd=0,bg='#000000')
        f8.place(relx=0.5,rely=0.535,anchor='center')

        l38=lb(f8,text='Forgot password',font=('SF Pro Display',38,'bold'),bd=0,bg='#000000', fg='#FFFFFF')
        l38.place(relx=0,rely=0.05,anchor='w')

        l39=lb(f8,image=p29,bd=0)
        l39.place(relx=0.5,rely=0.55,anchor='center') 

        l42=lb(f8,image=p33,bd=0)
        l42.place(relx = 0.525,rely=0.2,anchor = 'center') 

        global fid
        fid=ent(f8,bd = 0 ,font=('SF Pro Display',16),width=8,bg='#F2F2F2') 
        fid.place(relx = 0.525,rely=0.2,anchor = 'center') 

        l41=lb(f8,text='Enter ID :',bd = 0 ,font=('SF Pro Display',16),bg='#232323', fg='#FFFFFF')
        l41.place(relx = 0.375,rely = 0.2,anchor = 'center')

        def go():        
            dbcur.execute('select id from adminlogin')
            d2=dbcur.fetchall()  
            if fid.get()=='':
                msgb.showwarning('Empty entry','    Please enter ID.    ')
            if (fid.get(),) not in d2 and fid.get()!='':
                msgb.showwarning('Invalid entry','  Incorrect ID.  \nPlease try again')
            if (fid.get(),) in d2:            
                dbcur.execute('select * from adminlogin where id="{}"'.format(fid.get()))
                d3=dbcur.fetchall()[0]
                Pn='******'+d3[2][6:]
                t.sleep(0.5)        
                l40=lb(f8,text="We'll send an OTP the your registered mobile number ending with  {}.".format(Pn),
                font=('SF Pro Display',16),bd=0,bg='#232323', fg='#FFFFFF')
                l40.place(relx=0.5,rely=0.4,anchor='center')

                l43=lb(f8,image=p33,bd=0)
                l43.place(relx=0.525,rely=0.5,anchor='center')

                phone=ent(f8,bd = 0 ,font=('SF Pro Display',16),width=10,bg='#F2F2F2')
                phone.place(relx=0.525,rely=0.5,anchor='center')

                l44=lb(f8,text='Enter phone number :',bd=0,font=('SF Pro Display',16),bg='#232323', fg='#FFFFFF')
                l44.place(relx=0.31,rely=0.5,anchor='center')

                global scount
                scount=[]

                def send():            
                    phn=d3[2]
                    if phone.get().strip()==phn:
                        import Phone                       ### EXTERNAL INSTALL AND IMPORT ###    
                        try:
                            global onet
                            onet=randrange(635745,952675)
                            Phone.OTP(phn,onet)                 
                            msgb.showinfo('Forgot password','   OTP sent successfully.   ')
                            scount.append('clicked')
                        except:
                            msgb.showerror('Message Client error','Message could not be sent.\nPlease try again later.')    
                    else :
                        msgb.showwarning('Incorrect credentials','  Phone number not entered or invalid.  ') 

                b29=bt(f8,text='Send',bd=0,font=('SF Pro Display',16),bg='#232323',fg='#249ADF',activebackground='#232323',command=send)
                b29.place(relx=0.7,rely=0.55,anchor='center')
                
                l45=lb(f8,text='Enter One Time Password',bd=0,font=('SF Pro Display',16),bg='#232323',fg='#FFFFFF') 
                l45.place(relx=0.525,rely=0.65,anchor='center')

                l46=lb(f8,image=p33,bd=0)
                l46.place(relx=0.525,rely=0.75,anchor='center')

                otp=ent(f8,bd = 0 ,font=('SF Pro Display',16),width=6,bg='#F2F2F2')
                otp.place(relx=0.525,rely=0.75,anchor='center')

                def fverify():
                    if len(scount)==0:
                        msgb.showinfo('Message error','Please click on send to send OTP and then enter it to verify.')
                    if len(scount)!=0:    
                        if otp.get()=='':
                            msgb.showwarning('Invalid entry','Please enter OTP. \nif not recieved,enter registered mobile number and click on send')
                        if otp.get()==str(onet):
                            t.sleep(0.3)
                            global f9
                            f9=fr(f8,bd=0,height=500,width=855,bg='#000000')
                            f9.place(relx=0.5,rely=0.5,anchor='center')

                            l47=lb(f9,image=p29,bd=0)
                            l47.place(relx=0.5,rely=0.55,anchor='center')

                            l48=lb(f9,text='Set New password',font=('SF Pro Display',38,'bold'),bd=0,bg='#000000', fg='#FFFFFF')
                            l48.place(relx=0,rely=0.05,anchor='w')

                            l49=lb(f9,text='Enter new password :',font=('SF Pro Display',16),bd=0,bg='#232323', fg='#FFFFFF')
                            l49.place(relx=0.15,rely=0.2,anchor='w')

                            l50=lb(f9,image=p33,bd=0)
                            l50.place(relx=0.475,rely=0.2,anchor='center')

                            npass=ent(f9,bd = 0 ,font=('SF Pro Display',16),width=10,bg='#F2F2F2')
                            npass.place(relx=0.475,rely=0.2,anchor='center')

                            l51=lb(f9,text='Confirm password :',font=('SF Pro Display',16),bd=0,bg='#232323', fg='#FFFFFF')
                            l51.place(relx=0.15,rely=0.35,anchor='w')

                            l52=lb(f9,image=p33,bd=0)
                            l52.place(relx=0.475,rely=0.35,anchor='center')

                            cnpass=ent(f9,bd = 0 ,font=('SF Pro Display',16),width=10,bg='#F2F2F2')
                            cnpass.place(relx=0.475,rely=0.35,anchor='center')

                            def cancel2():
                                f9.place_forget()
                                f8.place_forget()
                                fram.place_forget()
                                f1.place(relx=0.5,rely=0.5,anchor = 'center')

                            b31=bt(f9,image=p52,font=('SF Pro Display',16),bd=0,bg='#000000',activebackground='#000000',fg='#CF3327',command=cancel2)
                            b31.place(relx=0.9,rely=0.08,anchor='center')
                            ANIMATE(b31,p52)

                            def save2():
                                try:
                                    if npass.get()=='' or cnpass.get()=='':
                                        msgb.showwarning('Operation unsuccessful','Please enter credentials in both fields')
                                    if npass.get()==cnpass.get() and npass.get()!='':
                                        dbcur.execute('update adminlogin set pass="{}" where id="{}"'.format(npass.get(),fid.get()))
                                        dbcon.commit()
                                        msgb.showinfo('Operation successful','Password changed successfully.\nPlease re-login for changes to take effect.')
                                        cancel2()
                                    if npass.get()!=cnpass.get() and npass.get()!='' and cnpass.get()!='':
                                        msgb.showwarning('Operation unsuccessful','Passswords do not match, please try again.')  
                                except:
                                    msgb.showinfo('Unexpected error','Please check all fields and try again.')

                            b32=bt(f9,text='Save',font=('SF Pro Display',16),bd=0,bg='#232323',activebackground='#232323',fg='#249ADF',command=save2)
                            b32.place(relx=0.55,rely=0.45,anchor='center')

                        if otp.get()!=str(onet) and otp.get()!='':
                            msgb.showwarning('Invalid entry','  Entered code is incorrect.  ')

                b30=bt(f8,text='Verify',font=('SF Pro Display',16),bd=0,fg='#249ADF',bg='#232323',activebackground='#232323',command=fverify)
                b30.place(relx=0.525,rely=0.825,anchor='center')
        
        def cancel1():
            fram.place_forget()
            f1.place(relx=0.5,rely=0.5,anchor = 'center')

        b27=bt(f8,text='Go',bd=0,font=('SF Pro Display',16),bg='#232323',fg='#249ADF',activebackground='#232323',command=go)
        b27.place(relx=0.6,rely=0.3,anchor='center')

        b28=bt(f8,image=p52,bd=0,font=('SF Pro Display',16),bg='#000000',fg='#CF3327',activebackground='#000000',command=cancel1)
        b28.place(relx=0.9,rely=0.08,anchor='center')
        ANIMATE(b28,p52)
        

    def passr():#####################################################################  COMPLETED  #############################################################    
        def apassreset():
            global l32
            l32=lb(f7,text='Current password :',bd=0,font=('SF Pro Display',16),bg='#232323',fg='#FFFFFF')
            l32.place(relx=0.2,rely=0.3,anchor='w')

            l33=lb(f7,text='New password :',bd=0,font=('SF Pro Display',16),bg='#232323',fg='#FFFFFF')
            l33.place(relx=0.2,rely=0.4,anchor='w')

            l34=lb(f7,text='Confirm new password :',bd=0,font=('SF Pro Display',16),bg='#232323',fg='#FFFFFF')
            l34.place(relx=0.2,rely=0.5,anchor='w')

            l35=lb(f7,image=p33,bd=0)
            l36=lb(f7,image=p33,bd=0)
            l37=lb(f7,image=p33,bd=0)
            l35.place(relx=0.45,rely=0.3,anchor='w')
            l36.place(relx=0.45,rely=0.4,anchor='w')
            l37.place(relx=0.45,rely=0.5,anchor='w')

            curpass=ent(f7,bd=0,bg='#F2F2F2',font=('SF Pro Display',16),width=10) # cur
            curpass.place(relx=0.475,rely=0.3,anchor='w')

            newpass=ent(f7,bd=0,bg='#F2F2F2',font=('SF Pro Display',16),width=10) # new
            newpass.place(relx=0.475,rely=0.4,anchor='w')

            cnewpass=ent(f7,bd=0,bg='#F2F2F2',font=('SF Pro Display',16),width=10) # new confirmed
            cnewpass.place(relx=0.475,rely=0.5,anchor='w')

            global b25
            b25=bt(f7,text= 'Forgot your Password ?',font = ('SF Pro Display',10,UNDERLINE),
            bd = 0,bg = '#232323',fg='#737373',activebackground = '#232323',command=forgpass)
            b25.place(relx=0.675,rely=0.3,anchor='w')
                
            def apass_save():
                dbcur.execute('select * from adminlogin where id="{}"'.format(aid.get()))
                d4=dbcur.fetchall()[0]
                try:
                    if curpass.get()=='':
                        msgb.showwarning('Empty entry',' Please enter current password. ')        
                    if curpass.get()!=d4[1] and curpass.get()!='':
                        msgb.showwarning('Incorrect password','Entered password was wrong.\nplease try again.')
                    if curpass.get()==d4[1]:
                        if newpass.get()=='':
                            msgb.showwarning('Empty entry','  Please enter new password.  ')    
                        if cnewpass.get()!=newpass.get() and newpass.get()!='':
                            msgb.showwarning('Incorrect entry',' New passwords do no match,\n please try again.')
                            newpass.delete(0,END)
                            cnewpass.delete(0,END)
                        if newpass.get()==cnewpass.get() and newpass.get()!='':
                            dbcur.execute('update adminlogin set pass="{}" where id="{}"'.format(cnewpass.get(),aid.get()))
                            dbcon.commit()
                            msgb.showinfo('Operation successful','Password changed successfully.\nPlease re-login for changes to take effect.')
                except:
                    msgb.showinfo('Unexpected error','Please check all fields and try again.')

            b26=bt(f7,text='Save',bd=0,font=('SF Pro Display',15),bg='#232323',fg='#249ADF',activebackground='#232323',command=apass_save)
            b26.place(relx=0.7,rely=0.6,anchor='center')

        def spassreset():
            b25.place_forget()
            l32.configure(text='Enter ID : ')

            l54=lb(f7,text='New password :',bd=0,font=('SF Pro Display',16),bg='#232323',fg='#FFFFFF')
            l54.place(relx=0.2,rely=0.4,anchor='w')

            l55=lb(f7,text='Confirm new password :',bd=0,font=('SF Pro Display',16),bg='#232323',fg='#FFFFFF')
            l55.place(relx=0.2,rely=0.5,anchor='w')

            l56=lb(f7,image=p33,bd=0)
            l57=lb(f7,image=p33,bd=0)
            l58=lb(f7,image=p33,bd=0)
            l56.place(relx=0.45,rely=0.3,anchor='w')
            l57.place(relx=0.45,rely=0.4,anchor='w')
            l58.place(relx=0.45,rely=0.5,anchor='w')

            Sid=ent(f7,bd=0,bg='#F2F2F2',font=('SF Pro Display',16),width=10) # current
            Sid.place(relx=0.475,rely=0.3,anchor='w')

            newspass=ent(f7,bd=0,bg='#F2F2F2',font=('SF Pro Display',16),width=10) # new
            newspass.place(relx=0.475,rely=0.4,anchor='w')

            cnewspass=ent(f7,bd=0,bg='#F2F2F2',font=('SF Pro Display',16),width=10) # new confirmed
            cnewspass.place(relx=0.475,rely=0.5,anchor='w')
                
            def spass_save():
                dbcur.execute('select id from slogin')
                d5=dbcur.fetchall()
                try:
                    if (Sid.get(),) in d5: 
                        if newspass.get()=='':
                            msgb.showwarning('Empty entry','  Please enter new password.  ')    
                        if cnewspass.get()!=newspass.get() and newspass.get()!='':
                            msgb.showwarning('Incorrect entry',' New passwords do no match,\n please try again.')
                            newspass.delete(0,END)
                            cnewspass.delete(0,END)
                        if newspass.get()==cnewspass.get() and newspass.get()!='':
                            dbcur.execute('update slogin set pass="{}" where id="{}"'.format(cnewspass.get(),Sid.get()))
                            dbcon.commit()
                            msgb.showinfo('Operation successful','Password changed successfully.')
                    else:
                        msgb.showwarning('Invalid ID','Incorrect ID, Please try again.')
                except:
                    msgb.showinfo('Unexpected error','Please check all fields and try again.')

            b26=bt(f7,text='Save',bd=0,font=('SF Pro Display',15),bg='#232323',fg='#249ADF',activebackground='#232323',command=spass_save)
            b26.place(relx=0.7,rely=0.6,anchor='center')       
        
        f4.place_forget()
        global f7
        f7=fr(f2,height=500,width=855,bd=0,bg='#000000') 
        f7.place(relx=0.5,rely=0.535,anchor='center')

        l30=lb(f7,image=p29,bd=0)
        l30.place(relx=0.5,rely=0.55,anchor='center')

        l31=lb(f7,text='Password reset',font=('SF Pro Display',38,'bold'),bd=0,bg='#000000', fg='#FFFFFF')
        l31.place(relx=0,rely=0.05,anchor='w')

        b23=bt(f7,image=p30,bd=0,bg='#232323',activebackground='#232323',command=apassreset)
        b23.place(relx=0.499,rely=0.175,anchor='e')
        ANIMATE(b23,p30)
        
        b24=bt(f7,image=p32,bd=0,bg='#232323',activebackground='#232323',command=spassreset)
        b24.place(relx=0.501,rely=0.177,anchor='w')
        ANIMATE(b24,p32)

        apassreset()       
        

    def sprofile():##########################################################   COMPLETED   ##################################################
        dbcur.execute('select sid from sprofile')
        global d1
        d1=dbcur.fetchall()
        if sid.get()=='':
            msgb.showwarning('ID error','  Please enter a Student ID  ')
        if (sid.get(),) not in d1 and sid.get()!='':
            msgb.showwarning('Invalid Student ID',' Please enter a valid student ID ')            
            sid.delete(0,END) 
        for i in d1:
            if sid.get()==i[0]:
                f4.place_forget()
                global f5
                f5=fr(f2,height=500,width=855,bd=0,bg='#000000') 
                f5.place(relx=0.5,rely=0.535,anchor='center')

                l6=lb(f5,text='Profile',font=('SF Pro Display',38,'bold'),bd=0,bg='#000000', fg='#FFFFFF')
                l6.place(relx=0,rely=0.05,anchor='w')

                dbcur.execute('select * from sprofile where sid="{}"'.format(sid.get()))
                d6=dbcur.fetchall()            
                rec=d6[0]

                l10=lb(f5,image=p25,bd=0)            
                l10.place(relx=0.5,rely=0.55,anchor='center')

                if rec[10] in ['male','Male','M','m']:
                    l13=lb(f5,image=p26,bd=0)
                    l13.place(relx=0.095,rely=0.375,anchor='center')
                if rec[10] in ['female','Female','F','f']:
                    l13=lb(f5,image=p27,bd=0)
                    l13.place(relx=0.095,rely=0.375,anchor='center')

                l14=lb(f5,text='{}'.format(rec[2]),bd=0,font=('SF Pro Display',16),bg='#232323',fg='#FFFFFF') # sname
                l14.place(relx=0.29,rely=0.29,anchor='w')   

                l15=lb(f5,text='{}'.format(rec[5]),bd=0,font=('SF Pro Display',16),bg='#232323',fg='#FFFFFF') # student ph
                l15.place(relx=0.29,rely=0.383,anchor='w') 

                l16=lb(f5,text='{}'.format(rec[9]),bd=0,font=('SF Pro Display',16),bg='#232323',fg='#FFFFFF') # year
                l16.place(relx=0.29,rely=0.475,anchor='w')

                l17=lb(f5,text='{}'.format(rec[1]),bd=0,font=('SF Pro Display',16),bg='#232323',fg='#FFFFFF') # admission number 
                l17.place(relx=0.6925,rely=0.29,anchor='w')

                l18=lb(f5,text='{}'.format(rec[8]),bd=0,font=('SF Pro Display',16),bg='#232323',fg='#FFFFFF') # course  
                l18.place(relx=0.6925,rely=0.383,anchor='w')

                l19=lb(f5,text='{}'.format(rec[0]),bd=0,font=('SF Pro Display',16),bg='#232323',fg='#FFFFFF') # id
                l19.place(relx=0.5425,rely=0.473,anchor='w')

                l20=lb(f5,text='{}'.format(rec[11]),bd=0,font=('SF Pro Display',16),bg='#232323',fg='#FFFFFF') # blood group
                l20.place(relx=0.825,rely=0.473,anchor='w')

                l21=lb(f5,text='{}'.format(rec[3]),bd=0,font=('SF Pro Display',16),bg='#232323',fg='#FFFFFF') # fname
                l21.place(relx=0.29,rely=0.688,anchor='w')

                l22=lb(f5,text='{}'.format(rec[6]),bd=0,font=('SF Pro Display',16),bg='#232323',fg='#FFFFFF') # father ph
                l22.place(relx=0.29,rely=0.782,anchor='w')

                l23=lb(f5,text='{}'.format(rec[4]),bd=0,font=('SF Pro Display',16),bg='#232323',fg='#FFFFFF') # mname
                l23.place(relx=0.78,rely=0.688,anchor='w')

                l24=lb(f5,text='{}'.format(rec[7]),bd=0,font=('SF Pro Display',16),bg='#232323',fg='#FFFFFF') # mother ph
                l24.place(relx=0.78,rely=0.782,anchor='w')

                l25=lb(f5,text='{}'.format(rec[10].capitalize()),bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') # gender 
                l25.place(relx=0.095,rely=0.515,anchor='center')          
                
                def profile_edit():
                    b17.place_forget()  
                    l13.place(relx=0.095,rely=0.345,anchor='center')

                    lb(f5,image = p33,bd=0).place(relx=0.29,rely=0.29,anchor='w')
                    sname_e=ent(f5,bd=0,bg='#F2F2F2',font=('SF Pro Display',14),width=13) # for student name
                    sname_e.place(relx=0.298,rely=0.29,anchor='w')
                    sname_e.insert(0,rec[2])

                    lb(f5,image = p33,bd=0).place(relx=0.29,rely=0.383,anchor='w')
                    sph_e=ent(f5,bd=0,bg='#F2F2F2',font=('SF Pro Display',14),width=13) # for student mobile
                    sph_e.place(relx=0.298,rely=0.383,anchor='w')
                    sph_e.insert(0,rec[5])

                    lb(f5,image = p33,bd=0).place(relx=0.29,rely=0.475,anchor='w')
                    y_e=ent(f5,bd=0,bg='#F2F2F2',font=('SF Pro Display',14),width=13) # for current year
                    y_e.place(relx=0.298,rely=0.475,anchor='w')
                    y_e.insert(0,rec[9])

                    
                    lb(f5,image = p33,bd=0).place(relx=0.6925,rely=0.29,anchor='w')
                    admn_e=ent(f5,bd=0,bg='#F2F2F2',font=('SF Pro Display',14),width=13) # for student admission
                    admn_e.place(relx=0.7005,rely=0.29,anchor='w')
                    admn_e.insert(0,rec[1])

                    l18.place_forget()
                    lb(f5,image = p33,bd=0).place(relx=0.6925,rely=0.383,anchor='w')
                    crs_e=ent(f5,bd=0,bg='#F2F2F2',font=('SF Pro Display',14),width=13) # for course
                    crs_e.place(relx=0.7005,rely=0.383,anchor='w')
                    crs_e.insert(0,rec[8])

                    lb(f5,image = p44,bd=0).place(relx=0.825,rely=0.473,anchor='w')
                    bld_e=ent(f5,bd=0,bg='#F2F2F2',font=('SF Pro Display',14),width=4) # for blood group
                    bld_e.place(relx=0.833,rely=0.473,anchor='w')
                    bld_e.insert(0,rec[11])
                    
                    l25.place_forget()
                    lb(f5,image = p44,bd=0).place(relx=0.095,rely=0.5,anchor='center')
                    gdr_e=ent(f5,bd=0,bg='#F2F2F2',font=('SF Pro Display',13),width=6) # for gender
                    gdr_e.place(relx=0.095,rely=0.5,anchor='center')
                    gdr_e.insert(0,rec[10])
                    
                    lb(f5,image = p33,bd=0).place(relx=0.29,rely=0.688,anchor='w')
                    fname_e=ent(f5,bd=0,bg='#F2F2F2',font=('SF Pro Display',14),width=13) # for father's name
                    fname_e.place(relx=0.298,rely=0.688,anchor='w')
                    fname_e.insert(0,rec[3])

                    lb(f5,image = p33,bd=0).place(relx=0.29,rely=0.782,anchor='w')
                    fph_e=ent(f5,bd=0,bg='#F2F2F2',font=('SF Pro Display',14),width=13) # father's number
                    fph_e.place(relx=0.298,rely=0.782,anchor='w')
                    fph_e.insert(0,rec[6])

                    lb(f5,image = p33,bd=0).place(relx=0.78,rely=0.688,anchor='w')
                    mname_e=ent(f5,bd=0,bg='#F2F2F2',font=('SF Pro Display',14),width=13) # for mother's name
                    mname_e.place(relx=0.788,rely=0.688,anchor='w')
                    mname_e.insert(0,rec[4])

                    lb(f5,image = p33,bd=0).place(relx=0.78,rely=0.782,anchor='w')
                    mph_e=ent(f5,bd=0,bg='#F2F2F2',font=('SF Pro Display',14),width=13) # mother's number
                    mph_e.place(relx=0.788,rely=0.782,anchor='w')
                    mph_e.insert(0,rec[7])

                    def profile_save():
                        a=0
                        b=0
                        c=0
                        d=0
                        r=0
                        ad=0
                        for ch in sname_e.get(): # sname checked.
                            if ch.isdigit()==True:
                                a+=1
                        for ch1 in fname_e.get(): # fname checked.
                            if ch1.isdigit()==True:
                                a+=1
                        for ch2 in mname_e.get(): # mname checked.
                            if ch2.isdigit()==True:
                                a+=1                
                        if a!=0:
                            msgb.showwarning('Invalid entry','Names cannot contain numbers, please try again.')
                            sname_e.delete(0,END)
                            fname_e.delete(0,END)
                            mname_e.delete(0,END)
                            sname_e.insert(0,rec[2])
                            fname_e.insert(0,rec[3])
                            mname_e.insert(0,rec[4])
                            r+=1
                            
                        for n in sph_e.get(): # sph cheked.
                            if n.isdigit()!=True:
                                b+=1 
                        for n1 in fph_e.get(): # fph cheked.
                            if n1.isdigit()!=True:
                                b+=1
                        for n2 in mph_e.get(): # mph checked.
                            if n2.isdigit()!=True:
                                b+=1                           
                        if len(sph_e.get())!=10 or len(fph_e.get())!=10 or len(mph_e.get())!=10 or b!=0:
                            msgb.showwarning('Invalid entry','Phone number is invalid, please try again.')
                            sph_e.delete(0,END)
                            fph_e.delete(0,END)
                            mph_e.delete(0,END)
                            sph_e.insert(0,rec[5])
                            fph_e.insert(0,rec[6])
                            mph_e.insert(0,rec[7])
                            r+=1
                            
                        l=['1st year','2nd year','3rd year','Final year'] # year checked.
                        if y_e.get() not in l:
                            msgb.showwarning('Invalid entry','    Please check year.    ')
                            y_e.delete(0,END)
                            r+=1     

                        for ad1 in admn_e.get()[1:]:
                            if ad1 in list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'):
                                ad+=1
                        if admn_e.get().startswith('S')==False or ad!=0:
                            c+=1
                        if c!=0: # admission number checked
                            msgb.showwarning('Invalid entry','Admission number is not valid, please try again.')
                            admn_e.delete(0,END)
                            admn_e.insert(0,rec[1])
                            r+=1

                        for w in crs_e.get(): # course checked.
                            if w.isdigit()==True:
                                d+=1  
                        if d!=0:   
                            msgb.showwarning('Invalid entry','Course is not valid, please try again.')
                            crs_e.delete(0,END)
                            crs_e.insert(0,rec[8])
                            r+=1
                        l2=['+A','+B','+O','-O','+AB','-AB','-A','-B'] # blood group checked.
                        if bld_e.get() not in l2:
                            msgb.showwarning('Invalid entry','Please check blood group and try again.')
                            bld_e.delete(0,END)
                            bld_e.insert(0,rec[11])
                            r+=1
                        if gdr_e.get() not in ['male','female','Male','Female']: # gender checked.
                            msgb.showwarning('Invalid entry','Please check gender and try again.')
                            gdr_e.delete(0,END)
                            gdr_e.insert(0,rec[10])  
                            r+=1              
                        else:
                            if r==0: 
                                try:                       
                                    dbcur.execute('update sprofile set '
                                    'sname="{}",sph="{}",pname="{}",fph="{}",mname="{}",mph="{}",year="{}",'
                                    'addm_no="{}",course="{}",blood_group="{}",gender="{}" where sid="{}"'.format(
                                        sname_e.get(),sph_e.get(),fname_e.get(),fph_e.get(),mname_e.get(), 
                                        mph_e.get(),y_e.get(),admn_e.get(),crs_e.get(),bld_e.get(),
                                        gdr_e.get(),rec[0])) 
                                    dbcon.commit()
                                    msgb.showinfo('Message','Operation successful.')
                                    sprofile()
                                except:
                                    msgb.showwarning('Unexpected error','Please try again.')    
    
                    b18=bt(f5,image=p51,bd=0,font=('SF Pro Display',15),bg='#000000',fg='#249ADF',activebackground='#000000',command=profile_save)
                    b18.place(relx=0.95,rely=0.1,anchor='center') 
                    ANIMATE(b18,p51)

                    b19=bt(f5,image=p52,bd=0,font=('sf pro display',15),bg='#000000',fg='#CF3327',activebackground='#000000',command=sprofile)  
                    b19.place(relx=0.85,rely=0.1,anchor='center')
                    ANIMATE(b19,p52)

                b17=bt(f5,image=p28,bd=0,bg='#000000',activebackground='#000000',command=profile_edit)  
                b17.place(relx=0.975,rely=0.09,anchor='center')  
                ANIMATE(b17,p28)  


    def marks(): ##########################################################   COMPLETED   ##################################################
        dbcur.execute('select sid from marks')
        global d13
        d13=dbcur.fetchall()
        if sid.get()=='':
            msgb.showwarning('ID error','  Please enter a Student ID  ')
        if (sid.get(),) not in d13 and sid.get()!='':
            msgb.showwarning('Invalid Student ID',' Please enter a valid student ID ')            
            sid.delete(0,END)
        if (sid.get(),) in d13:
            f4.place_forget()

            global f10
            f10=fr(f2,height=500,width=855,bd=0,bg='#000000') 
            f10.place(relx=0.5,rely=0.535,anchor='center')

            l59=lb(f10,text='Mark details',font=('SF Pro Display',38,'bold'),bd=0,bg='#000000', fg='#FFFFFF')
            l59.place(relx=0,rely=0.05,anchor='w')

            l60=lb(f10,image=p34,bd=0)
            l60.place(relx=0.5,rely=0.56,anchor='center')

            dbcur.execute('select * from marks where sid="{}"'.format(sid.get()))
            d10=dbcur.fetchall()            
            rec1=list(d10[0])
            for y in range(0,len(rec1)):
                if rec1[y]==None:
                    rec1[y]='NULL'                  
            
            if rec1[1]!='NULL':
                l61=lb(f10,text=rec1[1],bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') # mid sem 1
                l61.place(relx=0.53,rely=0.315,anchor='center')

                l62=lb(f10,text=(rec1[1]+'%'),bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
                l62.place(relx=0.82,rely=0.315,anchor='center')
            else:
                l77=lb(f10,text='N/A',bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') # mid sem 1
                l77.place(relx=0.53,rely=0.315,anchor='center')

                l78=lb(f10,text='N/A',bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
                l78.place(relx=0.82,rely=0.315,anchor='center')

            if rec1[2]!='NULL':
                l63=lb(f10,text=rec1[2],bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') # sem final 1 
                l63.place(relx=0.53,rely=0.375,anchor='center')

                l64=lb(f10,text=(rec1[2]+'%'),bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
                l64.place(relx=0.82,rely=0.375,anchor='center')
            else:
                l79=lb(f10,text='N/A',bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') # sem final 1 
                l79.place(relx=0.53,rely=0.375,anchor='center')

                l80=lb(f10,text='N/A',bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
                l80.place(relx=0.82,rely=0.375,anchor='center')
            
            if rec1[3]!='NULL':
                l65=lb(f10,text=rec1[3],bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') # midsem 2
                l65.place(relx=0.53,rely=0.465,anchor='center')

                l66=lb(f10,text=(rec1[3]+'%'),bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
                l66.place(relx=0.82,rely=0.465,anchor='center')
            else:
                l65=lb(f10,text='N/A',bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') # midsem 2
                l65.place(relx=0.53,rely=0.465,anchor='center')

                l66=lb(f10,text=('N/A'),bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
                l66.place(relx=0.82,rely=0.465,anchor='center')
        
            if rec1[4]!='NULL':
                l67=lb(f10,text=rec1[4],bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') # final 2
                l67.place(relx=0.53,rely=0.525,anchor='center')

                l68=lb(f10,text=(rec1[4]+'%'),bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
                l68.place(relx=0.82,rely=0.525,anchor='center')
            else:
                l67=lb(f10,text=('N/A'),bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') # final 2
                l67.place(relx=0.53,rely=0.525,anchor='center')

                l68=lb(f10,text=('N/A'),bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
                l68.place(relx=0.82,rely=0.525,anchor='center')      
            
            if rec1[5]!='NULL':
                l69=lb(f10,text=rec1[5],bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') # midsem 3
                l69.place(relx=0.53,rely=0.615,anchor='center')

                l70=lb(f10,text=(rec1[5]+'%'),bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
                l70.place(relx=0.82,rely=0.615,anchor='center')
            else:
                l69=lb(f10,text=('N/A'),bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') # midsem 3
                l69.place(relx=0.53,rely=0.615,anchor='center')

                l70=lb(f10,text=('N/A'),bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
                l70.place(relx=0.82,rely=0.615,anchor='center')

            if rec1[6]!='NULL':    
                l71=lb(f10,text=rec1[6],bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') # final 3 
                l71.place(relx=0.53,rely=0.675,anchor='center')

                l72=lb(f10,text=(rec1[6]+'%'),bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
                l72.place(relx=0.82,rely=0.675,anchor='center')
            else:
                l71=lb(f10,text='N/A',bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') # final 3 
                l71.place(relx=0.53,rely=0.675,anchor='center')

                l72=lb(f10,text='N/A',bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
                l72.place(relx=0.82,rely=0.675,anchor='center')

            if rec1[7]!='NULL':
                l73=lb(f10,text=rec1[7],bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') # midsem 4
                l73.place(relx=0.53,rely=0.765,anchor='center')

                l74=lb(f10,text=(rec1[7]+'%'),bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
                l74.place(relx=0.82,rely=0.765,anchor='center')
            else:
                l73=lb(f10,text='N/A',bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') # midsem 4
                l73.place(relx=0.53,rely=0.765,anchor='center')

                l74=lb(f10,text='N/A',bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
                l74.place(relx=0.82,rely=0.765,anchor='center')

            if rec1[8]!='NULL':
                l75=lb(f10,text=rec1[8],bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') # final 4
                l75.place(relx=0.53,rely=0.825,anchor='center')

                l76=lb(f10,text=(rec1[8]+'%'),bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
                l76.place(relx=0.82,rely=0.825,anchor='center')
            else:
                l75=lb(f10,text='N/A',bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') # final 4
                l75.place(relx=0.53,rely=0.825,anchor='center')

                l76=lb(f10,text='N/A',bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
                l76.place(relx=0.82,rely=0.825,anchor='center')

            def marks_edit():
                b33.place_forget()
                rec2=[]
                for i in rec1:
                    if i!='NULL':
                        rec2.append(i)
                    if i=='NULL':
                        rec2.append('N/A')   
                
                lb(f10,image=p44,bd=0).place(relx=0.53,rely=0.315,anchor='center')
                e1=ent(f10,bd=0,bg='#F2F2F2',font=('SF Pro Display',15),width=3)
                e1.place(relx=0.53,rely=0.315,anchor='center')
                e1.insert(0,rec2[1])

                lb(f10,image=p44,bd=0).place(relx=0.53,rely=0.375,anchor='center')
                e2=ent(f10,bd=0,bg='#F2F2F2',font=('SF Pro Display',15),width=3)
                e2.place(relx=0.53,rely=0.375,anchor='center')
                e2.insert(0,rec2[2]) 

                lb(f10,image=p44,bd=0).place(relx=0.53,rely=0.465,anchor='center')
                e3=ent(f10,bd=0,bg='#F2F2F2',font=('SF Pro Display',15),width=3)
                e3.place(relx=0.53,rely=0.465,anchor='center')
                e3.insert(0,rec2[3])

                lb(f10,image=p44,bd=0).place(relx=0.53,rely=0.525,anchor='center')
                e4=ent(f10,bd=0,bg='#F2F2F2',font=('SF Pro Display',15),width=3)
                e4.place(relx=0.53,rely=0.525,anchor='center')
                e4.insert(0,rec2[4])

                lb(f10,image=p44,bd=0).place(relx=0.53,rely=0.615,anchor='center')
                e5=ent(f10,bd=0,bg='#F2F2F2',font=('SF Pro Display',15),width=3)
                e5.place(relx=0.53,rely=0.615,anchor='center')
                e5.insert(0,rec2[5])

                lb(f10,image=p44,bd=0).place(relx=0.53,rely=0.675,anchor='center')
                e6=ent(f10,bd=0,bg='#F2F2F2',font=('SF Pro Display',15),width=3)
                e6.place(relx=0.53,rely=0.675,anchor='center')
                e6.insert(0,rec2[6])

                lb(f10,image=p44,bd=0).place(relx=0.53,rely=0.765,anchor='center')
                e7=ent(f10,bd=0,bg='#F2F2F2',font=('SF Pro Display',15),width=3)
                e7.place(relx=0.53,rely=0.765,anchor='center')
                e7.insert(0,rec2[7])

                lb(f10,image=p44,bd=0).place(relx=0.53,rely=0.825,anchor='center')
                e8=ent(f10,bd=0,bg='#F2F2F2',font=('SF Pro Display',15),width=3)
                e8.place(relx=0.53,rely=0.825,anchor='center')
                e8.insert(0,rec2[8])
                
                def marks_save():
                    mget=[e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get()]
                    w=0 
                    s=0                  
                    for b in range(0,len(mget)):
                        if mget[b]=='NULL':
                            msgb.showinfo("Entry error","NULL is an internal keyword.\nPlease enter 'N/A' instead")
                            s+=1
                            break
                    for d in range(0,len(mget)):
                        if mget[d]=='N/A':
                            mget[d]='NULL'                                        
                    lis1=['NULL']
                    for a in range(0,101):
                        lis1.append(str(a))                  
                    
                    for i in mget:
                        if i not in lis1:
                            w+=1
                    if w!=0:
                        msgb.showwarning('Entry error','Please check all entries,\nThere seems to be a mistake.')
                        marks()
                    if w==0 and s==0:
                        dbcur.execute('update marks set mid1="{}",final1="{}",'
                        'mid2="{}",final2="{}",mid3="{}",final3="{}",mid4="{}",final4="{}" '
                        'where sid="{}"'.format(mget[0],mget[1],mget[2],mget[3],mget[4],mget[5],
                        mget[6],mget[7],rec1[0]))
                        dbcon.commit()
                        msgb.showinfo('Operation sucessful','All records updated successfully.')
                        marks()
                            
                b34=bt(f10,image=p51,bd=0,font=('SF Pro Display',15),bg='#000000',fg='#249ADF',activebackground='#000000',command=marks_save)
                b34.place(relx=0.95,rely=0.0875,anchor='center')
                ANIMATE(b34,p51)

                b35=bt(f10,image=p52,bd=0,font=('sf pro display',15),bg='#000000',fg='#CF3327',activebackground='#000000',command=marks)  
                b35.place(relx=0.85,rely=0.0875,anchor='center')
                ANIMATE(b35,p52)

            b33=bt(f10,image=p28,bd=0,bg='#000000',activebackground='#000000',command=marks_edit)  
            b33.place(relx=0.95,rely=0.09,anchor='center')
            ANIMATE(b33,p28)


    def fee_details():##########################################################  COMPLETED  ####################################################################
        dbcur.execute('select sid from fees')
        global d13
        d13=dbcur.fetchall()
        if sid.get()=='':
            msgb.showwarning('ID error','  Please enter a Student ID  ')
        if (sid.get(),) not in d13 and sid.get()!='':
            msgb.showwarning('Invalid Student ID',' Please enter a valid student ID ')            
            sid.delete(0,END)
        if (sid.get(),) in d13:
            f4.place_forget()

            f11=fr(f2,height=500,width=855,bd=0,bg='#000000') 
            f11.place(relx=0.5,rely=0.535,anchor='center')

            l81=lb(f11,text='Fee details',font=('SF Pro Display',38,'bold'),bd=0,bg='#000000', fg='#FFFFFF')
            l81.place(relx=0,rely=0.05,anchor='w')

            l82=lb(f11,image=p29,bd=0)
            l82.place(relx=0.5,rely=0.55,anchor='center')

            dbcur.execute('select * from fees where sid="{}"'.format(sid.get()))
            global d14
            d14=list(dbcur.fetchall()[0])
            for j in range(0,len(d14)):
                if d14[j]==None or d14[j]=='NULL':
                    d14[j]='N/A'
            pp1=[p37,p38,p39]
            pp2=['All Clear!','No dues!','No Pending Fees!'] 
            im=choice(pp1)
            it=choice(pp2) 

            l98=lb(f11,image=im,bd=0)
            l99=lb(f11,text=it,font=('SF Pro Display',32,'bold'),bd=0,bg='#232323', fg='#FFFFFF')

            if d14[3]=='Paid' or d14[3]=='paid':                           
                l98.place(relx=0.5,rely=0.45,anchor='center')             
                l99.place(relx=0.5,rely=0.65,anchor='center')
            else:       
                l82.place(relx=0.5,rely=0.55,anchor='center')

                l92=lb(f11,text='Cycle  :',font=('SF Pro Display',16),bd=0,bg='#232323', fg='#249ADF')
                l92.place(relx=0.2,rely=0.25,anchor='w')

                l93=lb(f11,text='Amount  :',font=('SF Pro Display',16),bd=0,bg='#232323', fg='#249ADF')
                l93.place(relx=0.2,rely=0.35,anchor='w')

                l94=lb(f11,text='Status  :',font=('SF Pro Display',16),bd=0,bg='#232323', fg='#249ADF')
                l94.place(relx=0.2,rely=0.45,anchor='w')

                l100=lb(f11,text='Due date  :',font=('SF Pro Display',16),bd=0,bg='#232323', fg='#249ADF')
                l100.place(relx=0.2,rely=0.55,anchor='w')

                l95=lb(f11,text=d14[1],font=('SF Pro Display',16),bd=0,bg='#232323', fg='#FFFFFF')
                l95.place(relx=0.35,rely=0.25,anchor='w')

                if d14[2]!='N/A':
                    l96=lb(f11,text=('Rs. '+d14[2]+'/-'),font=('SF Pro Display',16),bd=0,bg='#232323', fg='#FFFFFF')
                    l96.place(relx=0.35,rely=0.35,anchor='w')
                else:
                    l96=lb(f11,text=d14[2],font=('SF Pro Display',16),bd=0,bg='#232323', fg='#FFFFFF')
                    l96.place(relx=0.35,rely=0.35,anchor='w')

                l97=lb(f11,text=d14[3],font=('SF Pro Display',16),bd=0,bg='#232323', fg='#FFFFFF')
                l97.place(relx=0.35,rely=0.45,anchor='w')

                l101=lb(f11,text=d14[4],font=('SF Pro Display',16),bd=0,bg='#232323', fg='#FFFFFF')
                l101.place(relx=0.35,rely=0.55,anchor='w')    
            
            def fee_edit():

                b36.place_forget()
                l98.place_forget()
                l99.place_forget()
                l95.place_forget()

                l82.place(relx=0.5,rely=0.55,anchor='center')   

                la1=lb(f11,text='Cycle  :',font=('SF Pro Display',16),bd=0,bg='#232323', fg='#249ADF')
                la1.place(relx=0.2,rely=0.25,anchor='w')

                la2=lb(f11,text='Amount  :',font=('SF Pro Display',16),bd=0,bg='#232323', fg='#249ADF')
                la2.place(relx=0.2,rely=0.35,anchor='w')

                la3=lb(f11,text='Status  :',font=('SF Pro Display',16),bd=0,bg='#232323', fg='#249ADF')
                la3.place(relx=0.2,rely=0.45,anchor='w')

                la8=lb(f11,text='Due date  :',font=('SF Pro Display',16),bd=0,bg='#232323', fg='#249ADF')
                la8.place(relx=0.2,rely=0.55,anchor='w')

                la4=lb(f11,image=p33,bd=0)
                la5=lb(f11,image=p33,bd=0)
                la6=lb(f11,image=p33,bd=0)
                la7=lb(f11,image=p33,bd=0)
                la4.place(relx=0.45,rely=0.25,anchor='center')
                la5.place(relx=0.45,rely=0.35,anchor='center')
                la6.place(relx=0.45,rely=0.45,anchor='center')
                la7.place(relx=0.45,rely=0.55,anchor='center')

                cy=ent(f11,bd=0,font=('SF Pro Display',15),width=10,bg='#F2F2F2')
                cy.place(relx=0.45,rely=0.25,anchor='center')
                cy.insert(0,d14[1]) 

                amt=ent(f11,bd=0,font=('SF Pro Display',15),width=10,bg='#F2F2F2')
                amt.place(relx=0.45,rely=0.35,anchor='center')
                amt.insert(0,d14[2])

                st=ent(f11,bd=0,font=('SF Pro Display',15),width=10,bg='#F2F2F2')
                st.place(relx=0.45,rely=0.45,anchor='center')
                st.insert(0,d14[3])

                dd=ent(f11,bd=0,font=('SF Pro Display',15),width=10,bg='#F2F2F2')
                dd.place(relx=0.45,rely=0.55,anchor='center')
                dd.insert(0,d14[4])

                tx1=('* The cycle can be any time period, it may be represented as semesters or even dates.\n'
                    '* You can only edit the record of the most recent or due payment only.\n'
                    '* Payments can be done only through depositing check, DD, NEFT, RTGS or by online alternatives\n'
                    'such as PayTM, our online portal, Net banking, etc.\n'
                    '* Funds once transferred can in no way be refunded, instead it may be adjusted in future transactions.\n')
                m2=msg(f11,text=tx1,bd=0,bg='#232323',fg='#FFFFFF',font=('SF Pro Display',11),width=800)                
                m2.place(relx=0.5,rely=0.8,anchor='center')
                
                def fee_save():                    
                    fc=0
                    err=0
                    n=0
                    fget=[cy.get(),amt.get(),st.get(),dd.get()]
                    for i in fget:
                        if i=='':
                            fc+=1
                    if fc!=0:
                        msgb.showwarning('Entry error','Please fill all fields and try again.')
                    if fc==0:
                        for h in amt.get():
                            if h.isalpha()==True:
                                n+=1
                        if n!=0 or int(fget[1]) not in range(1,1000000):
                            msgb.showwarning('Message','Please enter valid amount.')
                            err+=1
                        if fget[2] not in ['Pending','Paid','paid','pending']:
                            msgb.showwarning('Message','Please check status, you can only enter Paid or Pending.')
                            err+=1
                        if err==0:
                            try:
                                dbcur.execute('update fees set cycle="{}",amount="{}",status="{}",'
                                'due_date="{}" where sid="{}"'.format(fget[0],fget[1],fget[2],fget[3],sid.get()))
                                dbcon.commit()
                                msgb.showinfo('Message','Operation succesfull.')
                                fee_details()
                            except:
                                msgb.showwarning('Unexpected error','Please check all entries and try again or later.')

                b37=bt(f11,image=p51,bd=0,font=('SF Pro Display',15),bg='#000000',fg='#249ADF',activebackground='#000000',command=fee_save)
                b37.place(relx=0.95,rely=0.0875,anchor='center') 
                ANIMATE(b37,p51)

                b38=bt(f11,image=p52,bd=0,font=('sf pro display',15),bg='#000000',fg='#CF3327',activebackground='#000000',command=fee_details)  
                b38.place(relx=0.85,rely=0.0875,anchor='center')
                ANIMATE(b38,p52)

            b36=bt(f11,image=p28,bd=0,bg='#000000',activebackground='#000000',command=fee_edit)  
            b36.place(relx=0.95,rely=0.09,anchor='center')
            ANIMATE(b36,p28)


    def events(): #################################################### COMPLETED ###############################################################
        f4.place_forget()

        f14=fr(f2,height=500,width=855,bd=0,bg='#000000') 
        f14.place(relx=0.5,rely=0.535,anchor='center')

        la9=lb(f14,text='Events',font=('SF Pro Display',38,'bold'),bd=0,bg='#000000', fg='#FFFFFF') 
        la9.place(relx=0,rely=0.05,anchor='w')

        lb1=lb(f14,image=p40,bd=0)
        lb1.place(relx=0.5,rely=0.55,anchor='center')

        dbcur.execute('select * from events')
        d15=dbcur.fetchall()
        
        ### EVENTS ###

        lm1=msg(f14,text=d15[0][1].strip(),bd=0,bg='#404040',fg='#FFFFFF',width=525,font=('SF Pro Display',10))
        lm1.place(relx=0.085,rely=0.335,anchor='w',height=55)

        lm2=msg(f14,text=d15[1][1].strip(),bd=0,bg='#404040',fg='#FFFFFF',width=525,font=('SF Pro Display',10))
        lm2.place(relx=0.085,rely=0.471,anchor='w',height=55)

        lm3=msg(f14,text=d15[2][1].strip(),bd=0,bg='#404040',fg='#FFFFFF',width=525,font=('SF Pro Display',10))
        lm3.place(relx=0.085,rely=0.607,anchor='w',height=55)

        lm4=msg(f14,text=d15[3][1].strip(),bd=0,bg='#404040',fg='#FFFFFF',width=525,font=('SF Pro Display',10))
        lm4.place(relx=0.085,rely=0.745,anchor='w',height=55)

        lm5=msg(f14,text=d15[4][1].strip(),bd=0,bg='#404040',fg='#FFFFFF',width=525,font=('SF Pro Display',10))
        lm5.place(relx=0.085,rely=0.883,anchor='w',height=55)

        ### DATES ###

        lb2=lb(f14,text=d15[0][2],bd=0,bg='#404040',fg='#FFFFFF',font=('SF Pro Display',10))
        lb2.place(relx=0.775,rely=0.335,anchor='w')

        lb3=lb(f14,text=d15[1][2],bd=0,bg='#404040',fg='#FFFFFF',font=('SF Pro Display',10))
        lb3.place(relx=0.775,rely=0.471,anchor='w')

        lb4=lb(f14,text=d15[2][2],bd=0,bg='#404040',fg='#FFFFFF',font=('SF Pro Display',10))
        lb4.place(relx=0.775,rely=0.607,anchor='w')

        lb5=lb(f14,text=d15[3][2],bd=0,bg='#404040',fg='#FFFFFF',font=('SF Pro Display',10))
        lb5.place(relx=0.775,rely=0.745,anchor='w')

        lb6=lb(f14,text=d15[4][2],bd=0,bg='#404040',fg='#FFFFFF',font=('SF Pro Display',10))
        lb6.place(relx=0.775,rely=0.883,anchor='w')

        def events_edit():
            b45.place_forget()
            
            ### EVENTS ###

            ta1=tx(f14,bd=0,bg='#404040',fg='#FFFFFF',font=('SF Pro Display',10),height=3)
            ta1.place(relx=0.085,rely=0.335,anchor='w',width=525)
            ta1.insert(1.0,d15[0][1].strip())

            ta2=tx(f14,bd=0,bg='#404040',fg='#FFFFFF',font=('SF Pro Display',10),height=3)
            ta2.place(relx=0.085,rely=0.471,anchor='w',width=525)
            ta2.insert(1.0,d15[1][1].strip())

            ta3=tx(f14,bd=0,bg='#404040',fg='#FFFFFF',font=('SF Pro Display',10),height=3)
            ta3.place(relx=0.085,rely=0.607,anchor='w',width=525)
            ta3.insert(1.0,d15[2][1].strip())

            ta4=tx(f14,bd=0,bg='#404040',fg='#FFFFFF',font=('SF Pro Display',10),height=3)
            ta4.place(relx=0.085,rely=0.745,anchor='w',width=525)
            ta4.insert(1.0,d15[3][1].strip())

            ta5=tx(f14,bd=0,bg='#404040',fg='#FFFFFF',font=('SF Pro Display',10),height=3)
            ta5.place(relx=0.085,rely=0.883,anchor='w',width=525)
            ta5.insert(1.0,d15[4][1].strip()) 
            
            ### DATES ###
            
            lb(f14,image = p45,bd=0).place(relx=0.7565,rely=0.335,anchor='w')
            tb1=ent(f14,bd=0,bg='#F2F2F2',font=('SF Pro Display',10),width=10)
            tb1.place(relx=0.775,rely=0.335,anchor='w')
            tb1.insert(0,d15[0][2])

            lb(f14,image = p45,bd=0).place(relx=0.7565,rely=0.471,anchor='w')
            tb2=ent(f14,bd=0,bg='#F2F2F2',font=('SF Pro Display',10),width=10)
            tb2.place(relx=0.775,rely=0.471,anchor='w')
            tb2.insert(0,d15[1][2])

            lb(f14,image = p45,bd=0).place(relx=0.7565,rely=0.607,anchor='w')
            tb3=ent(f14,bd=0,bg='#F2F2F2',font=('SF Pro Display',10),width=10)
            tb3.place(relx=0.775,rely=0.607,anchor='w')
            tb3.insert(0,d15[2][2])

            lb(f14,image = p45,bd=0).place(relx=0.7565,rely=0.745,anchor='w')
            tb4=ent(f14,bd=0,bg='#F2F2F2',font=('SF Pro Display',10),width=10)
            tb4.place(relx=0.775,rely=0.745,anchor='w')
            tb4.insert(0,d15[3][2])
            
            lb(f14,image = p45,bd=0).place(relx=0.7565,rely=0.883,anchor='w')
            tb5=ent(f14,bd=0,bg='#F2F2F2',font=('SF Pro Display',10),width=10)
            tb5.place(relx=0.775,rely=0.883,anchor='w')
            tb5.insert(0,d15[4][2])            

            def events_save():
                a=0
                b=0
                c=0
                eget=[ta1.get(1.0,END),ta2.get(1.0,END),ta3.get(1.0,END),ta4.get(1.0,END),ta5.get(1.0,END)]
                e1get=[tb1.get(),tb2.get(),tb3.get(),tb4.get(),tb5.get()]
                l1=['E01','E02','E03','E04','E05']
                for i in eget:
                    if i.strip()=='':
                        a+=1
                for k in e1get:
                    if k=='':
                        b+=1
                if a!=0 :
                    msgb.showwarning('Invalid entry','Please fill all descriptions and try again.')
                
                for h in e1get:
                    for p in h:
                        if p in list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'):
                            c+=1
                if b!=0 or c!=0:
                    msgb.showwarning('Invalid entry','Please check all the dates and try again.\nMake sure they are valid and relevant.')
                else:
                    if a==0 and b==0 and c==0:
                        try:
                            for p in range(0,5):                            
                                dbcur.execute('update events set event="{}",date="{}" where Eid="{}"'.format(eget[p],e1get[p],l1[p]))
                                dbcon.commit()
                            msgb.showinfo('Message','Operation succesful.')
                            events()
                        except:
                            msgb.showwarning('Unexpected error','Please check all entries and try again or later.')

            b46=bt(f14,image=p51,bd=0,font=('SF Pro Display',15),bg='#000000',fg='#249ADF',activebackground='#000000',command=events_save)
            b46.place(relx=0.95,rely=0.0865,anchor='center')
            ANIMATE(b46,p51)

            b47=bt(f14,image=p52,bd=0,font=('sf pro display',15),bg='#000000',fg='#CF3327',activebackground='#000000',command=events)  
            b47.place(relx=0.85,rely=0.0865,anchor='center')
            ANIMATE(b47,p52)

        b45=bt(f14,image=p28,bd=0,bg='#000000',activebackground='#000000',command=events_edit)  
        b45.place(relx=0.95,rely=0.08,anchor='center')
        ANIMATE(b45,p28)


    def attendance():######################################################  COMPLETED  ##########################################################
        dbcur.execute('select sid from attendance')
        global d16
        d16=dbcur.fetchall()
        if sid.get()=='':
            msgb.showwarning('ID error','  Please enter a Student ID  ')
        if (sid.get(),) not in d16 and sid.get()!='':
            msgb.showwarning('Invalid Student ID',' Please enter a valid student ID ')            
            sid.delete(0,END)
        if (sid.get(),) in d16:
            f4.place_forget()

            f15=fr(f2,height=500,width=855,bd=0,bg='#000000') 
            f15.place(relx=0.5,rely=0.535,anchor='center')

            lb7=lb(f15,text='Attendance',font=('SF Pro Display',38,'bold'),bd=0,bg='#000000', fg='#FFFFFF')
            lb7.place(relx=0,rely=0.05,anchor='w')

            lb8=lb(f15,image=p29,bd=0)
            lb8.place(relx=0.5,rely=0.55,anchor='center')

            dbcur.execute('select * from attendance where sid="{}"'.format(sid.get()))
            global d17
            d17=dbcur.fetchall()[0]
            
            lb9=lb(f15,text='Number of days present  :',font=('SF Pro Display',16),bd=0,bg='#232323', fg='#FFFFFF')
            lb9.place(relx=0.2,rely=0.2,anchor='w')

            lc1=lb(f15,text='Total number of days  :',font=('SF Pro Display',16),bd=0,bg='#232323', fg='#FFFFFF')
            lc1.place(relx=0.2,rely=0.275,anchor='w')

            lc2=lb(f15,text=d17[1],font=('SF Pro Display',16),bd=0,bg='#232323', fg='#249ADF')
            lc2.place(relx=0.55,rely=0.2,anchor='w')

            lc4=lb(f15,text='180',font=('SF Pro Display',16),bd=0,bg='#232323', fg='#FFFFFF')
            lc4.place(relx=0.55,rely=0.275,anchor='w')

            lc5=lb(f15,text='Status  :',font=('SF Pro Display',16),bd=0,bg='#232323', fg='#FFFFFF')
            lc5.place(relx=0.2,rely=0.35,anchor='w')

            lc6=lb(f15,text='N/A',font=('SF Pro Display',16),bd=0,bg='#232323',fg='#FFFFFF')
            lc6.place(relx=0.55,rely=0.35,anchor='w')

            if d17[1]!='NULL' and d17[1]!=None:
                if int(d17[1])<=180 and int(d17[1])>=163:
                    lc6.configure(text='Good',fg='#C9E265')
                if int(d17[1])<=162 and int(d17[1])>=135:  
                    lc6.configure(text='Adequate',fg='#8C52FF') 
                if int(d17[1])<=134 and int(d17[1])>=108:  
                    lc6.configure(text='Low',fg='#FF914D')
                if int(d17[1])<=107:  
                    lc6.configure(text='Critically low',fg='#FF5757')
                
                ## GRAPH ##

                c1=cv(f15,width=230,height=230,bd=0,bg='#232323',highlightbackground='#232323')
                arc=20,20,230,230
                pr=int(d17[1])
                ab=180-(pr)

                c1.create_arc(arc,start=-60,extent="{}".format(-ab),fill='#FF5757',outline='#FF5757') # absent right
                c1.create_arc(arc,start=0,extent="{}".format(pr),fill='#8C52FF',outline='#8C52FF') # present right
                c1.create_arc(arc,start="{}".format(pr),extent=120,fill='#C9E265',outline='#C9E265') # holidays (festivals + weekends)
                c1.create_arc(arc,start=0,extent=-60,fill='#FF914D',outline='#FF914D') # permitted leaves
                c1.place(relx=0.35,rely=0.65,anchor='center')

                lc7=lb(f15,image=p41,bd=0)
                lc7.place(relx=0.68,rely=0.66,anchor='center')

            def att_edit():

                lb(f15,image = p44,bd=0).place(relx=0.55,rely=0.2,anchor='w')
                at=ent(f15,bd=0,bg='#F2F2F2',font=('SF Pro Display',14),width=3)
                at.place(relx=0.558,rely=0.2,anchor='w')
                at.insert(0,d17[1])      

                b48.place_forget()
                def att_save():
                    a=0 
                    for i in at.get():
                        if i=='':
                            a+=1
                    if at.get()=='':
                        msgb.showwarning('Invalid entry','Please enter number of days present correctly and try again.')
                    if at.get()!='' and a!=0:
                        msgb.showwarning('Invalid error','Please enter a valid numeric value for number of days present.')
                    else:                        
                        if a==0 and at.get()!='':
                            try:
                                dbcur.execute('update attendance set present="{}" where sid="{}"'.format(at.get(),sid.get()))
                                dbcon.commit()
                                msgb.showinfo('Message','Operation successful.')
                                attendance()
                            except:
                                msgb.showwarning('Unexpected error','Please check all entries and try again or later.')   

                b49=bt(f15,image=p51,bd=0,font=('SF Pro Display',15),bg='#000000',fg='#249ADF',activebackground='#000000',command=att_save)
                b49.place(relx=0.95,rely=0.0875,anchor='center') 
                ANIMATE(b49,p51)

                b50=bt(f15,image=p52,bd=0,font=('sf pro display',15),bg='#000000',fg='#CF3327',activebackground='#000000',command=attendance)  
                b50.place(relx=0.85,rely=0.0875,anchor='center')
                ANIMATE(b50,p52)

            b48=bt(f15,image=p28,bd=0,bg='#000000',activebackground='#000000',command=att_edit)  
            b48.place(relx=0.95,rely=0.09,anchor='center')
            ANIMATE(b48,p28)


    def projects():######################################################  COMPLETED  #########################################################
        dbcur.execute('select sid from attendance')
        global d18
        d18=dbcur.fetchall()
        if sid.get()=='':
            msgb.showwarning('ID error','  Please enter a Student ID  ')
        if (sid.get(),) not in d18 and sid.get()!='':
            msgb.showwarning('Invalid Student ID',' Please enter a valid student ID ')            
            sid.delete(0,END)
        if (sid.get(),) in d18:
            f4.place_forget()
            f16=fr(f2,height=500,width=855,bd=0,bg='#000000') 
            f16.place(relx=0.5,rely=0.535,anchor='center')

            lc8=lb(f16,text='Projects',font=('SF Pro Display',38,'bold'),bd=0,bg='#000000', fg='#FFFFFF')
            lc8.place(relx=0,rely=0.05,anchor='w')

            lc9=lb(f16,image=p42,bd=0)
            lc9.place(relx=0.5,rely=0.56,anchor='center')

            dbcur.execute('select t1,t2,t3,t4,t5 from projects where sid="{}"'.format(sid.get()))
            d19=dbcur.fetchall()[0]
            proj=[]
            date1=[]
            for g in d19:
                y=g.split(',')
                proj.append(y[0])
                date1.append(y[1])
            for d in range(len(proj)):
                if proj[d]=='NULL' or proj[d]==None:
                    proj[d]='N/A'
            for f in range(len(date1)):
                if date1[f]=='NULL' or date1[f]==None:
                    date1[f]='N/A'

            ## PROJECT ##

            lm6=msg(f16,text=proj[0].strip(),bd=0,bg='#404040',fg='#FFFFFF',width=525,font=('SF Pro Display',16))
            lm6.place(relx=0.35,rely=0.348,anchor='center',height=55)

            lm7=msg(f16,text=proj[1].strip(),bd=0,bg='#404040',fg='#FFFFFF',width=525,font=('SF Pro Display',16))
            lm7.place(relx=0.35,rely=0.484,anchor='center',height=55)

            lm8=msg(f16,text=proj[2].strip(),bd=0,bg='#404040',fg='#FFFFFF',width=525,font=('SF Pro Display',16))
            lm8.place(relx=0.35,rely=0.62,anchor='center',height=55)

            lm9=msg(f16,text=proj[3].strip(),bd=0,bg='#404040',fg='#FFFFFF',width=525,font=('SF Pro Display',16))
            lm9.place(relx=0.35,rely=0.758,anchor='center',height=55)

            ln1=msg(f16,text=proj[4].strip(),bd=0,bg='#404040',fg='#FFFFFF',width=525,font=('SF Pro Display',16))
            ln1.place(relx=0.35,rely=0.896,anchor='center',height=55) 
            
            ## DATE ##

            ld0=lb(f16,text=date1[0],bd=0,bg='#404040',fg='#249ADF',font=('SF Pro Display',16))
            ld0.place(relx=0.785,rely=0.348,anchor='center')

            ld1=lb(f16,text=date1[1],bd=0,bg='#404040',fg='#249ADF',font=('SF Pro Display',16))
            ld1.place(relx=0.785,rely=0.484,anchor='center')

            ld2=lb(f16,text=date1[2],bd=0,bg='#404040',fg='#249ADF',font=('SF Pro Display',16))
            ld2.place(relx=0.785,rely=0.62,anchor='center')

            ld3=lb(f16,text=date1[3],bd=0,bg='#404040',fg='#249ADF',font=('SF Pro Display',16))
            ld3.place(relx=0.785,rely=0.758,anchor='center')

            ld4=lb(f16,text=date1[4],bd=0,bg='#404040',fg='#249ADF',font=('SF Pro Display',16))
            ld4.place(relx=0.785,rely=0.896,anchor='center')

            if date1[0]!='N/A':
                if str_date(date1[0])<date.today():
                    ld0.configure(fg='#FF5757')
                if str_date(date1[0])==date.today():
                    ld0.configure(fg='#E48F2A')
            if date1[1]!='N/A' :
                if str_date(date1[1])<date.today():
                    ld1.configure(fg='#FF5757')
                if str_date(date1[1])==date.today():
                    ld1.configure(fg='#E48F2A')
            if date1[2]!='N/A':
                if str_date(date1[2])<date.today():
                    ld2.configure(fg='#FF5757')
                if str_date(date1[2])==date.today():
                    ld2.configure(fg='#E48F2A')
            if date1[3]!='N/A':
                if str_date(date1[3])<date.today():
                    ld3.configure(fg='#FF5757')
                if str_date(date1[3])==date.today():
                    ld3.configure(fg='#E48F2A')
            if date1[4]!='N/A':
                if str_date(date1[4])<date.today():
                    ld4.configure(fg='#FF5757')
                if str_date(date1[4])==date.today():
                    ld4.configure(fg='#E48F2A')

            def projects_edit():
                b51.place_forget()

                ta6=tx(f16,bd=0,bg='#404040',fg='#FFFFFF',font=('SF Pro Display',16),height=2)
                ta6.place(relx=0.35,rely=0.348,anchor='center',width=450)
                ta6.insert(1.0,proj[0].strip())

                ta7=tx(f16,bd=0,bg='#404040',fg='#FFFFFF',font=('SF Pro Display',16),height=2)
                ta7.place(relx=0.35,rely=0.484,anchor='center',width=450)
                ta7.insert(1.0,proj[1].strip())

                ta8=tx(f16,bd=0,bg='#404040',fg='#FFFFFF',font=('SF Pro Display',16),height=2)
                ta8.place(relx=0.35,rely=0.62,anchor='center',width=450)
                ta8.insert(1.0,proj[2].strip())

                ta9=tx(f16,bd=0,bg='#404040',fg='#FFFFFF',font=('SF Pro Display',16),height=2)
                ta9.place(relx=0.35,rely=0.758,anchor='center',width=450)
                ta9.insert(1.0,proj[3].strip())

                ta10=tx(f16,bd=0,bg='#404040',fg='#FFFFFF',font=('SF Pro Display',16),height=2)
                ta10.place(relx=0.35,rely=0.896,anchor='center',width=450)
                ta10.insert(1.0,proj[4].strip()) 

                lb(f16,image = p46,bd=0).place(relx=0.785,rely=0.348,anchor='center')
                tb6=ent(f16,bd=0,bg='#F2F2F2',font=('SF Pro Display',16),width=10)
                tb6.place(relx=0.785,rely=0.348,anchor='center')
                tb6.insert(0,date1[0])

                lb(f16,image = p46,bd=0).place(relx=0.785,rely=0.484,anchor='center')
                tb7=ent(f16,bd=0,bg='#F2F2F2',font=('SF Pro Display',16),width=10)
                tb7.place(relx=0.785,rely=0.484,anchor='center')
                tb7.insert(0,date1[1])

                lb(f16,image = p46,bd=0).place(relx=0.785,rely=0.62,anchor='center')
                tb8=ent(f16,bd=0,bg='#F2F2F2',font=('SF Pro Display',16),width=10)
                tb8.place(relx=0.785,rely=0.62,anchor='center')
                tb8.insert(0,date1[2])

                lb(f16,image = p46,bd=0).place(relx=0.785,rely=0.758,anchor='center')
                tb9=ent(f16,bd=0,bg='#F2F2F2',font=('SF Pro Display',16),width=10)
                tb9.place(relx=0.785,rely=0.758,anchor='center')
                tb9.insert(0,date1[3])
                
                lb(f16,image = p46,bd=0).place(relx=0.785,rely=0.896,anchor='center')
                tc1=ent(f16,bd=0,bg='#F2F2F2',font=('SF Pro Display',16),width=10)
                tc1.place(relx=0.785,rely=0.896,anchor='center')
                tc1.insert(0,date1[4])

                def projects_save():
                    a=0
                    b=0
                    c=0
                    pro=[ta6.get(1.0,END).strip(),ta7.get(1.0,END).strip(),ta8.get(1.0,END).strip(),ta9.get(1.0,END).strip(),ta10.get(1.0,END).strip()]
                    dates=[tb6.get().strip(),tb7.get().strip(),tb8.get().strip(),tb9.get().strip(),tc1.get().strip()]
                    for h in pro:
                        if h=='':
                            a+=1
                    for i in dates :
                        if i=='':
                            a+=1
                        if i!='N/A':
                            for j in i:    
                                if j in list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'):
                                    b+=1
                    if a!=0:
                        msgb.showwarning('Invalid entry','Please fill all fields and try again.\n'
                        'If you want to leave an empty record\njust pass N/A in both its parameters.')
                    if b!=0:
                        msgb.showwarning('Invalid entry','Please enter a valid date.')
                    for u in range(5):
                        if pro[u].strip()=='N/A':
                            if dates[u]!='N/A':
                                c+=1
                        elif dates[u]=='N/A':
                            if pro[u].strip()!='N/A':
                                c+=1
                    if c!=0:
                        msgb.showwarning('Invalid entry','Please fill both parameters as N/A, not one.')
                    else:
                        if a==0 and b==0:
                            try:
                                q0=pro[0]+','+dates[0]
                                q1=pro[1]+','+dates[1]
                                q2=pro[2]+','+dates[2]
                                q3=pro[3]+','+dates[3]
                                q4=pro[4]+','+dates[4]
                                dbcur.execute('update projects set t1="{}",t2="{}",t3="{}",t4="{}",t5="{}" where sid="{}"'.format(
                                    q0,q1,q2,q3,q4,sid.get()))
                                msgb.showinfo('Message','Operation successful.')
                                dbcon.commit()
                                projects()
                            except TypeError:                        
                                msgb.showwarning('Unexpected error','Please check all entries and try again or later.')

                b52=bt(f16,image=p51,bd=0,font=('SF Pro Display',15),bg='#000000',fg='#249ADF',activebackground='#000000',command=projects_save)
                b52.place(relx=0.95,rely=0.0875,anchor='center') 
                ANIMATE(b52,p51)

                b53=bt(f16,image=p52,bd=0,font=('sf pro display',15),bg='#000000',fg='#CF3327',activebackground='#000000',command=projects)  
                b53.place(relx=0.85,rely=0.0875,anchor='center')
                ANIMATE(b53,p52)

            b51=bt(f16,image=p28,bd=0,bg='#000000',activebackground='#000000',command=projects_edit)  
            b51.place(relx=0.95,rely=0.09,anchor='center')
            ANIMATE(b51,p28)


    def assignments(): ################################################  COMPLETED  #############################################################
        dbcur.execute('select sid from attendance')
        global d18
        d18=dbcur.fetchall()
        if sid.get()=='':
            msgb.showwarning('ID error','  Please enter a Student ID  ')
        if (sid.get(),) not in d18 and sid.get()!='':
            msgb.showwarning('Invalid Student ID',' Please enter a valid student ID ')            
            sid.delete(0,END)
        if (sid.get(),) in d18:
            f4.place_forget()

            f17=fr(f2,height=500,width=855,bd=0,bg='#000000') 
            f17.place(relx=0.5,rely=0.535,anchor='center')

            ld5=lb(f17,text='Assignments',font=('SF Pro Display',38,'bold'),bd=0,bg='#000000', fg='#FFFFFF')
            ld5.place(relx=0,rely=0.05,anchor='w')

            ld6=lb(f17,image=p43,bd=0)
            ld6.place(relx=0.5,rely=0.55,anchor='center')

            dbcur.execute('select a1,a2,a3,a4,a5 from assignments where sid="{}"'.format(sid.get()))
            d19=dbcur.fetchall()[0]
            assi=[]
            adate=[]
            sdate=[]
            for i in d19:
                y=i.split(',')                
                assi.append(y[0])
                adate.append(y[1])
                sdate.append(y[2])
            for j in range(len(assi)):
                if assi[j]=='NULL' or assi[j]==None:
                    assi[j]='N/A'
            for k in range(len(adate)):
                if adate[k]=='NULL' or adate[k]==None:
                    adate[k]='N/A'
            for m in range(len(sdate)):
                if sdate[m]=='NULL' or sdate[m]==None:
                    sdate[m]='N/A'
            
            ### ASSIGNNMENT ####
            
            ln2=msg(f17,text=assi[0].strip(),bd=0,bg='#404040',fg='#FFFFFF',width=525,font=('SF Pro Display',16))
            ln2.place(relx=0.29,rely=0.34,anchor='center',height=55) 

            ln3=msg(f17,text=assi[1].strip(),bd=0,bg='#404040',fg='#FFFFFF',width=525,font=('SF Pro Display',16))
            ln3.place(relx=0.29,rely=0.473,anchor='center',height=55)

            ln4=msg(f17,text=assi[2].strip(),bd=0,bg='#404040',fg='#FFFFFF',width=525,font=('SF Pro Display',16))
            ln4.place(relx=0.29,rely=0.612,anchor='center',height=55)

            ln5=msg(f17,text=assi[3].strip(),bd=0,bg='#404040',fg='#FFFFFF',width=525,font=('SF Pro Display',16))
            ln5.place(relx=0.29,rely=0.75,anchor='center',height=55)

            ln6=msg(f17,text=assi[4].strip(),bd=0,bg='#404040',fg='#FFFFFF',width=525,font=('SF Pro Display',16))
            ln6.place(relx=0.29,rely=0.89,anchor='center',height=55)

            ### DATE OF ASSIGNMENT ###

            ld5=lb(f17,text=adate[0],bd=0,bg='#404040',fg='#FFFFFF',font=('SF Pro Display',16))
            ld5.place(relx=0.6275,rely=0.34,anchor='center')

            ld6=lb(f17,text=adate[1],bd=0,bg='#404040',fg='#FFFFFF',font=('SF Pro Display',16))
            ld6.place(relx=0.6275,rely=0.473,anchor='center')

            ld7=lb(f17,text=adate[2],bd=0,bg='#404040',fg='#FFFFFF',font=('SF Pro Display',16))
            ld7.place(relx=0.6275,rely=0.612,anchor='center')

            ld8=lb(f17,text=adate[3],bd=0,bg='#404040',fg='#FFFFFF',font=('SF Pro Display',16))
            ld8.place(relx=0.6275,rely=0.75,anchor='center')

            ld9=lb(f17,text=adate[4],bd=0,bg='#404040',fg='#FFFFFF',font=('SF Pro Display',16))
            ld9.place(relx=0.6275,rely=0.89,anchor='center')

            ### DATE OF SUBMISSION ###

            lf1=lb(f17,text=sdate[0],bd=0,bg='#404040',fg='#FFFFFF',font=('SF Pro Display',16))
            lf1.place(relx=0.8365,rely=0.34,anchor='center')

            lf2=lb(f17,text=sdate[1],bd=0,bg='#404040',fg='#FFFFFF',font=('SF Pro Display',16))
            lf2.place(relx=0.8365,rely=0.473,anchor='center')

            lf3=lb(f17,text=sdate[2],bd=0,bg='#404040',fg='#FFFFFF',font=('SF Pro Display',16))
            lf3.place(relx=0.8365,rely=0.612,anchor='center')

            lf4=lb(f17,text=sdate[3],bd=0,bg='#404040',fg='#FFFFFF',font=('SF Pro Display',16))
            lf4.place(relx=0.8365,rely=0.75,anchor='center')

            lf5=lb(f17,text=sdate[4],bd=0,bg='#404040',fg='#FFFFFF',font=('SF Pro Display',16))
            lf5.place(relx=0.8365,rely=0.89,anchor='center')

            if sdate[0]!='N/A':
                if str_date(sdate[0])<date.today():
                    lf1.configure(fg='#FF5757')
                if str_date(sdate[0])==date.today():
                    lf1.configure(fg='#E48F2A')
            if sdate[1]!='N/A' :
                if str_date(sdate[1])<date.today():
                    lf2.configure(fg='#FF5757')
                if str_date(sdate[1])==date.today():
                    lf2.configure(fg='#E48F2A')
            if sdate[2]!='N/A':
                if str_date(sdate[2])<date.today():
                    lf3.configure(fg='#FF5757')
                if str_date(sdate[2])==date.today():
                    lf3.configure(fg='#E48F2A')        
            if sdate[3]!='N/A':
                if str_date(sdate[3])<date.today():
                    lf4.configure(fg='#FF5757')
                if str_date(sdate[3])==date.today():
                    lf4.configure(fg='#E48F2A')
            if sdate[4]!='N/A':
                if str_date(sdate[4])<date.today():
                    lf5.configure(fg='#FF5757')
                if str_date(sdate[4])==date.today():
                    lf5.configure(fg='#E48F2A')
            
            def assignment_edit():

                b54.place_forget()

                a1=tx(f17,bd=0,bg='#404040',fg='#FFFFFF',font=('SF Pro Display',16),height=2)
                a1.place(relx=0.29,rely=0.34,anchor='center',width=350)
                a1.insert(1.0,assi[0].strip())

                a2=tx(f17,bd=0,bg='#404040',fg='#FFFFFF',font=('SF Pro Display',16),height=2)
                a2.place(relx=0.29,rely=0.473,anchor='center',width=350)
                a2.insert(1.0,assi[1].strip())

                a3=tx(f17,bd=0,bg='#404040',fg='#FFFFFF',font=('SF Pro Display',16),height=2)
                a3.place(relx=0.29,rely=0.612,anchor='center',width=350)
                a3.insert(1.0,assi[2].strip())

                a4=tx(f17,bd=0,bg='#404040',fg='#FFFFFF',font=('SF Pro Display',16),height=2)
                a4.place(relx=0.29,rely=0.75,anchor='center',width=350)
                a4.insert(1.0,assi[3].strip())

                a5=tx(f17,bd=0,bg='#404040',fg='#FFFFFF',font=('SF Pro Display',16),height=2)
                a5.place(relx=0.29,rely=0.89,anchor='center',width=350)
                a5.insert(1.0,assi[4].strip()) 

                #### A-DATE ####

                lb(f17,image=p46,bd=0).place(relx=0.6275,rely=0.34,anchor='center')
                a6=ent(f17,bd=0,bg='#F2F2F2',font=('SF Pro Display',16),width=10)
                a6.place(relx=0.6275,rely=0.34,anchor='center')
                a6.insert(0,adate[0])

                lb(f17,image=p46,bd=0).place(relx=0.6275,rely=0.473,anchor='center')
                a7=ent(f17,bd=0,bg='#F2F2F2',font=('SF Pro Display',16),width=10)
                a7.place(relx=0.6275,rely=0.473,anchor='center')
                a7.insert(0,adate[1])

                lb(f17,image=p46,bd=0).place(relx=0.6275,rely=0.612,anchor='center')
                a8=ent(f17,bd=0,bg='#F2F2F2',font=('SF Pro Display',16),width=10)
                a8.place(relx=0.6275,rely=0.612,anchor='center')
                a8.insert(0,adate[2])

                lb(f17,image=p46,bd=0).place(relx=0.6275,rely=0.75,anchor='center')
                a9=ent(f17,bd=0,bg='#F2F2F2',font=('SF Pro Display',16),width=10)
                a9.place(relx=0.6275,rely=0.75,anchor='center')
                a9.insert(0,adate[3])
                
                lb(f17,image=p46,bd=0).place(relx=0.6275,rely=0.89,anchor='center')
                c1=ent(f17,bd=0,bg='#F2F2F2',font=('SF Pro Display',16),width=10)
                c1.place(relx=0.6275,rely=0.89,anchor='center')
                c1.insert(0,adate[4])

                #### S-DATE ####

                lb(f17,image=p46,bd=0).place(relx=0.8365,rely=0.34,anchor='center')
                c2=ent(f17,bd=0,bg='#F2F2F2',font=('SF Pro Display',16),width=10)
                c2.place(relx=0.8365,rely=0.34,anchor='center')
                c2.insert(0,sdate[0])

                lb(f17,image=p46,bd=0).place(relx=0.8365,rely=0.473,anchor='center')
                c3=ent(f17,bd=0,bg='#F2F2F2',font=('SF Pro Display',16),width=10)
                c3.place(relx=0.8365,rely=0.473,anchor='center')
                c3.insert(0,sdate[1])

                lb(f17,image=p46,bd=0).place(relx=0.8365,rely=0.612,anchor='center')
                c4=ent(f17,bd=0,bg='#F2F2F2',font=('SF Pro Display',16),width=10)
                c4.place(relx=0.8365,rely=0.612,anchor='center')
                c4.insert(0,sdate[2])

                lb(f17,image=p46,bd=0).place(relx=0.8365,rely=0.75,anchor='center')
                c5=ent(f17,bd=0,bg='#F2F2F2',font=('SF Pro Display',16),width=10)
                c5.place(relx=0.8365,rely=0.75,anchor='center')
                c5.insert(0,sdate[3])
                
                lb(f17,image=p46,bd=0).place(relx=0.8365,rely=0.89,anchor='center')
                c6=ent(f17,bd=0,bg='#F2F2F2',font=('SF Pro Display',16),width=10)
                c6.place(relx=0.8365,rely=0.89,anchor='center')
                c6.insert(0,sdate[4])

                def assignment_save():
                    a1get=[a1.get(1.0,END).strip(),a2.get(1.0,END).strip(),a3.get(1.0,END).strip(),a4.get(1.0,END).strip(),a5.get(1.0,END).strip()]
                    adget=[a6.get().strip(),a7.get().strip(),a8.get().strip(),a9.get().strip(),c1.get().strip()]
                    sget= [c2.get().strip(),c3.get().strip(),c4.get().strip(),c5.get().strip(),c6.get().strip()]
                    g=0
                    z=0
                    p=0
                    for x in range(5):
                        if a1get[x]=='' or adget[x]=='' or sget[x]=='' :
                            g+=1
                        if a1get[x]=='N/A':
                            if adget[x]!='N/A':
                                p+=1
                            if sget[x]!='N/A':
                                p+=1
                        elif a1get[x]!='N/A':
                            if adget[x]=='N/A':
                                p+=1
                            if sget[x]=='N/A':
                                p+=1
                        elif a1get[x]!='N/A' and adget[x]!='N/A' and sget[x]!='N/A':
                            for v in adget[x] : 
                                if v in list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'):
                                    z+=1
                            for c in sget[x]:
                                if c in list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'):
                                    z+=1

                    if g!=0:
                        msgb.showwarning('Invalid entry','Please fill all fields and try again ')
                    if z!=0 and g==0:
                        msgb.showwarning('Invalid entry','Please enter a valid date.\n\n'
                        'To leave an empty record, enter N/A in all 3 parameters.')
                    if p!=0 and g==0:
                        msgb.showwarning('Invalid entry','Please enter N/A in all 3 parameters if you want to leave it empty.')
                    else:
                        if z==0 and g==0 and p==0:
                            try:
                                q5=a1get[0]+','+adget[0]+','+sget[0]
                                q6=a1get[1]+','+adget[1]+','+sget[1]
                                q7=a1get[2]+','+adget[2]+','+sget[2]
                                q8=a1get[3]+','+adget[3]+','+sget[3]
                                q9=a1get[4]+','+adget[4]+','+sget[4]

                                dbcur.execute('update assignments set a1="{}",a2="{}",a3="{}",a4="{}",a5="{}" where sid="{}"'.format(
                                    q5,q6,q7,q8,q9,sid.get()))
                                dbcon.commit()
                                msgb.showinfo('Message','Operation successful.')
                                assignments()
                            except:
                                msgb.showwarning('Unexpected error','Please check all entries and try again or later.')                    

                b55=bt(f17,image=p51,bd=0,font=('SF Pro Display',15),bg='#000000',fg='#249ADF',activebackground='#000000',command=assignment_save)
                b55.place(relx=0.95,rely=0.0875,anchor='center') 
                ANIMATE(b55,p51)

                b56=bt(f17,image=p52,bd=0,font=('sf pro display',15),bg='#000000',fg='#CF3327',activebackground='#000000',command=assignments)  
                b56.place(relx=0.85,rely=0.0875,anchor='center')
                ANIMATE(b56,p52)

            b54=bt(f17,image=p28,bd=0,bg='#000000',activebackground='#000000',command=assignment_edit)  
            b54.place(relx=0.95,rely=0.085,anchor='center')
            ANIMATE(b54,p28)
        

    def about():####################################################################    COMPLETED    ###############################################
        f4.place_forget()
        global f6    
        f6=fr(f2,height=500,width=855,bd=0,bg='#000000') 
        f6.place(relx=0.5,rely=0.535,anchor='center')

        l27=lb(f6,image=p29,bd=0)
        l27.place(relx=0.5,rely=0.55,anchor='center')

        dbcur.execute('select * from about')
        d7=(dbcur.fetchall())[0][0]  

        m1=msg(f6,text=d7.strip(),bd=0,bg='#232323',fg='#FFFFFF',font=('SF Pro Display',12))
        m1.place(relx=0.5,rely=0.55,anchor='center',width=750,height=400)

        l26=lb(f6,text='About',font=('SF Pro Display',38,'bold'),bd=0,bg='#000000',fg='#FFFFFF')
        l26.place(relx=0,rely=0.05,anchor='w')

        def about_edit():
            m1.place_forget()
            b20.place_forget()

            t1=tx(f6,bd=0,bg='#232323',fg='#FFFFFF',font=('SF Pro Display',12),padx=80,pady=10)
            t1.place(relx=0.5,rely=0.55,anchor='center',width=750,height=400)
            t1.insert(1.0,d7)

            def abt_save():
                if t1.get(1.0,END).strip()=='':
                    msgb.showwarning('Invalid entry',' Entry is empty, Please try again. ')
                    about()
                else:
                    try:
                        dbcur.execute('update about set text="{}"'.format(t1.get(1.0,END)))
                        dbcon.commit()
                        about()
                    except:
                        msgb.showinfo('Unexpected error','Please check the entry and try again.')

            b21=bt(f6,image=p51,bd=0,font=('SF Pro Display',15),bg='#000000',fg='#249ADF',activebackground='#000000',command=abt_save)
            b21.place(relx=0.95,rely=0.0875,anchor='center') 
            ANIMATE(b21,p51)

            b22=bt(f6,image=p52,bd=0,font=('sf pro display',15),bg='#000000',fg='#CF3327',activebackground='#000000',command=about)  
            b22.place(relx=0.85,rely=0.0875,anchor='center')  
            ANIMATE(b22,p52)

        b20=bt(f6,image=p28,bd=0,bg='#000000',activebackground='#000000',command=about_edit)  
        b20.place(relx=0.95,rely=0.09,anchor='center')    
        ANIMATE(b20,p28)



                                            
                                            ###############################################################
#############################################################         STUDENT SIDE        ###########################################################
                                            ###############################################################


    def studenthome():#####################################################################  COMPLETED  #############################################################
        f1.place_forget()

        global f2
        f2=fr(win,bd=0,height=650,width=1150,bg='#000000')#bigger one
        f2.place(relx=0.5,rely=0.5,anchor='center') 

        global f3
        f3=fr(win,bd=0,height=100,width=1150,bg='#232323')#smaller one OVER F2
        f3.place(relx=0.5,rely=0,anchor='center')       

        l28=lb(f3,text=DATE,bd=0,font=('SF Pro Display',13),bg='#232323',fg='#FFFFFF') 
        l28.place(relx=0.715,rely=0.755,anchor='center')

        l29=lb(f2,bd=0,bg='#000000',fg='#FFFFFF',font=('SF Pro Display',22,'bold'))
        l29.place(relx=0.5,rely=0.105,anchor='center')

        #####################  GREETING ACCORDING TO TIME ####################

        if curtime>=time(0,00,00) and curtime<time(11,59,59):
            l29.configure(text='Good morning !')
        if curtime>=time(12,00,00) and curtime<time(17,59,59):
            l29.configure(text='Good afternoon !')
        if curtime>=time(18,00,00) and curtime<time(23,59,59):
            l29.configure(text='Good evening !')       
        
        l5=lb(f3,image = p9,bd=0)
        l5.place(relx=0.05,rely=0.75,anchor = 'center')

        b6=bt(f3,image=p10,bd=0,bg='#232323',activebackground = '#232323',command = main)
        b6.place(relx=0.95,rely=0.75,anchor = 'center')
        ANIMATE(b6,p10)

        global f4
        f4=fr(f2,height=520,width=875,bd=0,bg='#000000') # OVER F2 BELOW F3
        f4.place(relx=0.5,rely=0.535,anchor='center')

        b7=bt(f4,image=p11,bd=0,bg='#000000',activebackground='#000000',command=sprofile1) # profile
        b7.place(relx=0.1385,rely=0.236,anchor='center')
        ANIMATE(b7,p11)

        b8=bt(f4,image=p12,bd=0,bg='#000000',activebackground='#000000',command=assignments1) #assignments
        b8.place(relx=0.466,rely=0.688,anchor='center')
        ANIMATE(b8,p12)
        
        b9=bt(f4,image=p14,bd=0,bg='#000000',activebackground='#000000',command=projects1) # projects
        b9.place(relx=0.392,rely=0.182,anchor='center')
        ANIMATE(b9,p14)

        b10=bt(f4,image=p18,bd=0,bg='#000000',activebackground='#000000',command=marks1) # marks
        b10.place(relx=0.7515,rely=0.182,anchor='center')
        ANIMATE(b10,p18)

        b11=bt(f4,image=p16,bd=0,bg='#000000',activebackground='#000000',command=attendance1) # attendance
        b11.place(relx=0.13855,rely=0.62,anchor='center')
        ANIMATE(b11,p16)

        b12=bt(f4,image=p15,bd=0,bg='#000000',activebackground='#000000',command=events1) # events
        b12.place(relx=0.13855,rely=0.8825,anchor='center')
        ANIMATE(b12,p15)

        b13=bt(f4,image=p19,bd=0,bg='#000000',activebackground='#000000',command=passr1) # passreset
        b13.place(relx=0.738,rely=0.52,anchor='center')
        ANIMATE(b13,p19)

        b14=bt(f4,image=p17,bd=0,bg='#000000',activebackground='#000000',command=about1) # about
        b14.place(relx=0.912,rely=0.52,anchor='center')
        ANIMATE(b14,p17)
        
        b15=bt(f4,image=p13,bd=0,bg='#000000',activebackground='#000000',command=fee_details1) # fee
        b15.place(relx=0.8263,rely=0.828,anchor='center')
        ANIMATE(b15,p13)

        b16=bt(f3,image=p20,bd=0,bg='#232323',activebackground ='#232323',command=studenthome) # studenthome button
        b16.place(relx=0.5,rely=0.75,anchor='center')
        ANIMATE(b16,p20)

        dbcur.execute('select sname from sprofile where sid="{}" '.format(stid.get()))
        gr=dbcur.fetchall()
        msgl=['Hi !','Hey !','Bonjour !']
        greeting=choice(msgl)+'  '+(gr[0][0].split())[0]

        l12=lb(f3,text=greeting,font=('SF Pro Display',18),bd=0,bg='#232323',fg='#FFFFFF')
        l12.place(relx=0.275,rely=0.75,anchor='center')
        

    def passr1():#####################################################################  COMPLETE  #############################################################    
        def spassreset1():
            l32=lb(f7,text='Current password : ',bd=0,font=('SF Pro Display',16),bg='#232323',fg='#FFFFFF')
            l32.place(relx=0.2,rely=0.3,anchor='w')            

            l54=lb(f7,text='New password :',bd=0,font=('SF Pro Display',16),bg='#232323',fg='#FFFFFF')
            l54.place(relx=0.2,rely=0.4,anchor='w')

            l55=lb(f7,text='Confirm new password :',bd=0,font=('SF Pro Display',16),bg='#232323',fg='#FFFFFF')
            l55.place(relx=0.2,rely=0.5,anchor='w')

            l56=lb(f7,image=p33,bd=0)
            l57=lb(f7,image=p33,bd=0)
            l58=lb(f7,image=p33,bd=0)
            l56.place(relx=0.45,rely=0.3,anchor='w')
            l57.place(relx=0.45,rely=0.4,anchor='w')
            l58.place(relx=0.45,rely=0.5,anchor='w')

            Curpass=ent(f7,bd=0,bg='#F2F2F2',font=('SF Pro Display',16),width=10) # current
            Curpass.place(relx=0.475,rely=0.3,anchor='w')

            newspass=ent(f7,bd=0,bg='#F2F2F2',font=('SF Pro Display',16),width=10) # new
            newspass.place(relx=0.475,rely=0.4,anchor='w')

            cnewspass=ent(f7,bd=0,bg='#F2F2F2',font=('SF Pro Display',16),width=10) # new confirmed
            cnewspass.place(relx=0.475,rely=0.5,anchor='w')
                
            def spass_save():
                dbcur.execute('select pass from slogin where id="{}"'.format(stid.get()))
                d5=dbcur.fetchall()
                try:
                    if (Curpass.get(),) in d5: 
                        if newspass.get()=='':
                            msgb.showwarning('Empty entry','  Please enter new password.  ')    
                        if cnewspass.get()!=newspass.get() and newspass.get()!='':
                            msgb.showwarning('Incorrect entry',' New passwords do no match,\n please try again.')
                            newspass.delete(0,END)
                            cnewspass.delete(0,END)
                        if newspass.get()==cnewspass.get() and newspass.get()!='':
                            dbcur.execute('update slogin set pass="{}" where id="{}"'.format(cnewspass.get(),stid.get()))
                            dbcon.commit()
                            msgb.showinfo('Operation successful','Password changed successfully.')
                            studenthome()
                    else:
                        msgb.showwarning('Invalid ID','Current password is incorrect, Please try again.')
                except:
                    msgb.showinfo('Unexpected error','Please check all fields and try again.')

            b26=bt(f7,text='Save',bd=0,font=('SF Pro Display',15),bg='#232323',fg='#249ADF',activebackground='#232323',command=spass_save)
            b26.place(relx=0.7,rely=0.6,anchor='center')       
        
        f4.place_forget()
        global f7
        f7=fr(f2,height=500,width=855,bd=0,bg='#000000') 
        f7.place(relx=0.5,rely=0.535,anchor='center')

        l30=lb(f7,image=p29,bd=0)
        l30.place(relx=0.5,rely=0.55,anchor='center')

        l31=lb(f7,text='Password reset',font=('SF Pro Display',38,'bold'),bd=0,bg='#000000', fg='#FFFFFF')
        l31.place(relx=0,rely=0.05,anchor='w')
        
        spassreset1()       
        

    def sprofile1():##########################################################   COMPLETE   ##################################################
                        
        f4.place_forget()
        global f5
        f5=fr(f2,height=500,width=855,bd=0,bg='#000000') 
        f5.place(relx=0.5,rely=0.535,anchor='center')

        l6=lb(f5,text='Profile',font=('SF Pro Display',38,'bold'),bd=0,bg='#000000', fg='#FFFFFF')
        l6.place(relx=0,rely=0.05,anchor='w')

        dbcur.execute('select * from sprofile where sid="{}"'.format(stid.get()))
        d6=dbcur.fetchall()            
        rec=d6[0]

        l10=lb(f5,image=p25,bd=0)            
        l10.place(relx=0.5,rely=0.55,anchor='center')

        if rec[10] in ['male','Male','M','m']:
            l13=lb(f5,image=p26,bd=0)
            l13.place(relx=0.095,rely=0.375,anchor='center')
        if rec[10] in ['female','Female','F','f']:
            l13=lb(f5,image=p27,bd=0)
            l13.place(relx=0.095,rely=0.375,anchor='center')

        l14=lb(f5,text='{}'.format(rec[2]),bd=0,font=('SF Pro Display',16),bg='#232323',fg='#FFFFFF') # sname
        l14.place(relx=0.29,rely=0.29,anchor='w')   

        l15=lb(f5,text='{}'.format(rec[5]),bd=0,font=('SF Pro Display',16),bg='#232323',fg='#FFFFFF') # student ph
        l15.place(relx=0.29,rely=0.383,anchor='w') 

        l16=lb(f5,text='{}'.format(rec[9]),bd=0,font=('SF Pro Display',16),bg='#232323',fg='#FFFFFF') # year
        l16.place(relx=0.29,rely=0.475,anchor='w')

        l17=lb(f5,text='{}'.format(rec[1]),bd=0,font=('SF Pro Display',16),bg='#232323',fg='#FFFFFF') # admission number 
        l17.place(relx=0.6925,rely=0.29,anchor='w')

        l18=lb(f5,text='{}'.format(rec[8]),bd=0,font=('SF Pro Display',16),bg='#232323',fg='#FFFFFF') # course  
        l18.place(relx=0.6925,rely=0.383,anchor='w')

        l19=lb(f5,text='{}'.format(rec[0]),bd=0,font=('SF Pro Display',16),bg='#232323',fg='#FFFFFF') # id
        l19.place(relx=0.5425,rely=0.473,anchor='w')

        l20=lb(f5,text='{}'.format(rec[11]),bd=0,font=('SF Pro Display',16),bg='#232323',fg='#FFFFFF') # blood group
        l20.place(relx=0.825,rely=0.473,anchor='w')

        l21=lb(f5,text='{}'.format(rec[3]),bd=0,font=('SF Pro Display',16),bg='#232323',fg='#FFFFFF') # fname
        l21.place(relx=0.29,rely=0.688,anchor='w')

        l22=lb(f5,text='{}'.format(rec[6]),bd=0,font=('SF Pro Display',16),bg='#232323',fg='#FFFFFF') # father ph
        l22.place(relx=0.29,rely=0.782,anchor='w')

        l23=lb(f5,text='{}'.format(rec[4]),bd=0,font=('SF Pro Display',16),bg='#232323',fg='#FFFFFF') # mname
        l23.place(relx=0.78,rely=0.688,anchor='w')

        l24=lb(f5,text='{}'.format(rec[7]),bd=0,font=('SF Pro Display',16),bg='#232323',fg='#FFFFFF') # mother ph
        l24.place(relx=0.78,rely=0.782,anchor='w')

        l25=lb(f5,text='{}'.format(rec[10].capitalize()),bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') # gender 
        l25.place(relx=0.095,rely=0.515,anchor='center')  


    def marks1(): ##########################################################   COMPLETE   ##################################################
        f4.place_forget()

        global f10
        f10=fr(f2,height=500,width=855,bd=0,bg='#000000') 
        f10.place(relx=0.5,rely=0.535,anchor='center')

        l59=lb(f10,text='Mark details',font=('SF Pro Display',38,'bold'),bd=0,bg='#000000', fg='#FFFFFF')
        l59.place(relx=0,rely=0.05,anchor='w')

        l60=lb(f10,image=p34,bd=0)
        l60.place(relx=0.5,rely=0.56,anchor='center')

        dbcur.execute('select * from marks where sid="{}"'.format(stid.get()))
        d10=dbcur.fetchall()            
        rec1=list(d10[0])
        for y in range(0,len(rec1)):
            if rec1[y]==None:
                rec1[y]='NULL'                  
        
        if rec1[1]!='NULL':
            l61=lb(f10,text=rec1[1],bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') # mid sem 1
            l61.place(relx=0.53,rely=0.315,anchor='center')

            l62=lb(f10,text=(rec1[1]+'%'),bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
            l62.place(relx=0.82,rely=0.315,anchor='center')
        else:
            l77=lb(f10,text='N/A',bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') # mid sem 1
            l77.place(relx=0.53,rely=0.315,anchor='center')

            l78=lb(f10,text='N/A',bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
            l78.place(relx=0.82,rely=0.315,anchor='center')

        if rec1[2]!='NULL':
            l63=lb(f10,text=rec1[2],bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') # sem final 1 
            l63.place(relx=0.53,rely=0.375,anchor='center')

            l64=lb(f10,text=(rec1[2]+'%'),bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
            l64.place(relx=0.82,rely=0.375,anchor='center')
        else:
            l79=lb(f10,text='N/A',bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') # sem final 1 
            l79.place(relx=0.53,rely=0.375,anchor='center')

            l80=lb(f10,text='N/A',bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
            l80.place(relx=0.82,rely=0.375,anchor='center')
        
        if rec1[3]!='NULL':
            l65=lb(f10,text=rec1[3],bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') # midsem 2
            l65.place(relx=0.53,rely=0.465,anchor='center')

            l66=lb(f10,text=(rec1[3]+'%'),bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
            l66.place(relx=0.82,rely=0.465,anchor='center')
        else:
            l65=lb(f10,text='N/A',bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') # midsem 2
            l65.place(relx=0.53,rely=0.465,anchor='center')

            l66=lb(f10,text=('N/A'),bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
            l66.place(relx=0.82,rely=0.465,anchor='center')
    
        if rec1[4]!='NULL':
            l67=lb(f10,text=rec1[4],bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') # final 2
            l67.place(relx=0.53,rely=0.525,anchor='center')

            l68=lb(f10,text=(rec1[4]+'%'),bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
            l68.place(relx=0.82,rely=0.525,anchor='center')
        else:
            l67=lb(f10,text=('N/A'),bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') # final 2
            l67.place(relx=0.53,rely=0.525,anchor='center')

            l68=lb(f10,text=('N/A'),bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
            l68.place(relx=0.82,rely=0.525,anchor='center')      
        
        if rec1[5]!='NULL':
            l69=lb(f10,text=rec1[5],bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') # midsem 3
            l69.place(relx=0.53,rely=0.615,anchor='center')

            l70=lb(f10,text=(rec1[5]+'%'),bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
            l70.place(relx=0.82,rely=0.615,anchor='center')
        else:
            l69=lb(f10,text=('N/A'),bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') # midsem 3
            l69.place(relx=0.53,rely=0.615,anchor='center')

            l70=lb(f10,text=('N/A'),bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
            l70.place(relx=0.82,rely=0.615,anchor='center')

        if rec1[6]!='NULL':    
            l71=lb(f10,text=rec1[6],bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') # final 3 
            l71.place(relx=0.53,rely=0.675,anchor='center')

            l72=lb(f10,text=(rec1[6]+'%'),bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
            l72.place(relx=0.82,rely=0.675,anchor='center')
        else:
            l71=lb(f10,text='N/A',bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') # final 3 
            l71.place(relx=0.53,rely=0.675,anchor='center')

            l72=lb(f10,text='N/A',bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
            l72.place(relx=0.82,rely=0.675,anchor='center')

        if rec1[7]!='NULL':
            l73=lb(f10,text=rec1[7],bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') # midsem 4
            l73.place(relx=0.53,rely=0.765,anchor='center')

            l74=lb(f10,text=(rec1[7]+'%'),bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
            l74.place(relx=0.82,rely=0.765,anchor='center')
        else:
            l73=lb(f10,text='N/A',bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') # midsem 4
            l73.place(relx=0.53,rely=0.765,anchor='center')

            l74=lb(f10,text='N/A',bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
            l74.place(relx=0.82,rely=0.765,anchor='center')

        if rec1[8]!='NULL':
            l75=lb(f10,text=rec1[8],bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') # final 4
            l75.place(relx=0.53,rely=0.825,anchor='center')

            l76=lb(f10,text=(rec1[8]+'%'),bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
            l76.place(relx=0.82,rely=0.825,anchor='center')
        else:
            l75=lb(f10,text='N/A',bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') # final 4
            l75.place(relx=0.53,rely=0.825,anchor='center')

            l76=lb(f10,text='N/A',bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
            l76.place(relx=0.82,rely=0.825,anchor='center')


    def fee_details1():##########################################################  COMPLETED  ####################################################################
        
        f4.place_forget()

        f11=fr(f2,height=500,width=855,bd=0,bg='#000000') 
        f11.place(relx=0.5,rely=0.535,anchor='center')

        l81=lb(f11,text='Fee details',font=('SF Pro Display',38,'bold'),bd=0,bg='#000000', fg='#FFFFFF')
        l81.place(relx=0,rely=0.05,anchor='w')

        l82=lb(f11,image=p29,bd=0)
        l82.place(relx=0.5,rely=0.55,anchor='center')

        dbcur.execute('select * from fees where sid="{}"'.format(stid.get()))
        global d14
        d14=list(dbcur.fetchall()[0])
        for j in range(0,len(d14)):
            if d14[j]==None or d14[j]=='NULL':
                d14[j]='N/A'
        pp1=[p37,p38,p39]
        pp2=['All Clear!','No dues!','No Pending Fees!'] 
        im=choice(pp1)
        it=choice(pp2) 

        l98=lb(f11,image=im,bd=0)
        l99=lb(f11,text=it,font=('SF Pro Display',32,'bold'),bd=0,bg='#232323', fg='#FFFFFF')

        if d14[3]=='Paid' or d14[3]=='paid':                           
            l98.place(relx=0.5,rely=0.45,anchor='center')             
            l99.place(relx=0.5,rely=0.65,anchor='center')
        else:       
            l82.place(relx=0.5,rely=0.55,anchor='center')

            l92=lb(f11,text='Cycle  :',font=('SF Pro Display',16),bd=0,bg='#232323', fg='#249ADF')
            l92.place(relx=0.2,rely=0.25,anchor='w')

            l93=lb(f11,text='Amount  :',font=('SF Pro Display',16),bd=0,bg='#232323', fg='#249ADF')
            l93.place(relx=0.2,rely=0.35,anchor='w')

            l94=lb(f11,text='Status  :',font=('SF Pro Display',16),bd=0,bg='#232323', fg='#249ADF')
            l94.place(relx=0.2,rely=0.45,anchor='w')

            l100=lb(f11,text='Due date  :',font=('SF Pro Display',16),bd=0,bg='#232323', fg='#249ADF')
            l100.place(relx=0.2,rely=0.55,anchor='w')

            l95=lb(f11,text=d14[1],font=('SF Pro Display',16),bd=0,bg='#232323', fg='#FFFFFF')
            l95.place(relx=0.35,rely=0.25,anchor='w')

            if d14[2]!='N/A':
                l96=lb(f11,text=('Rs. '+d14[2]+'/-'),font=('SF Pro Display',16),bd=0,bg='#232323', fg='#FFFFFF')
                l96.place(relx=0.35,rely=0.35,anchor='w')
            else:
                l96=lb(f11,text=d14[2],font=('SF Pro Display',16),bd=0,bg='#232323', fg='#FFFFFF')
                l96.place(relx=0.35,rely=0.35,anchor='w')

            l97=lb(f11,text=d14[3],font=('SF Pro Display',16),bd=0,bg='#232323', fg='#FFFFFF')
            l97.place(relx=0.35,rely=0.45,anchor='w')

            l101=lb(f11,text=d14[4],font=('SF Pro Display',16),bd=0,bg='#232323', fg='#FFFFFF')
            l101.place(relx=0.35,rely=0.55,anchor='w')  

            tx1=('* The cycle can be any time period, it may be represented as semesters or even dates.\n'
                    '* You can only review the record of the most recent or due payment only.\n'
                    '* Payments can be done only through depositing check, DD, NEFT, RTGS or by online alternatives\n'
                    'such as PayTM, our online portal, Net banking, etc.\n'
                    '* Funds once transferred can in no way be refunded, instead it may be adjusted in future transactions.\n')
            m2=msg(f11,text=tx1,bd=0,bg='#232323',fg='#FFFFFF',font=('SF Pro Display',11),width=800)                
            m2.place(relx=0.5,rely=0.8,anchor='center')   
            
           
    def events1(): #################################################### COMPLETED ###############################################################
        f4.place_forget()

        f14=fr(f2,height=500,width=855,bd=0,bg='#000000') 
        f14.place(relx=0.5,rely=0.535,anchor='center')

        la9=lb(f14,text='Events',font=('SF Pro Display',38,'bold'),bd=0,bg='#000000', fg='#FFFFFF') 
        la9.place(relx=0,rely=0.05,anchor='w')

        lb1=lb(f14,image=p40,bd=0)
        lb1.place(relx=0.5,rely=0.55,anchor='center')

        dbcur.execute('select * from events')
        d15=dbcur.fetchall()
        
        ### EVENTS ###

        lm1=msg(f14,text=d15[0][1].strip(),bd=0,bg='#404040',fg='#FFFFFF',width=525,font=('SF Pro Display',10))
        lm1.place(relx=0.085,rely=0.335,anchor='w',height=55)

        lm2=msg(f14,text=d15[1][1].strip(),bd=0,bg='#404040',fg='#FFFFFF',width=525,font=('SF Pro Display',10))
        lm2.place(relx=0.085,rely=0.471,anchor='w',height=55)

        lm3=msg(f14,text=d15[2][1].strip(),bd=0,bg='#404040',fg='#FFFFFF',width=525,font=('SF Pro Display',10))
        lm3.place(relx=0.085,rely=0.607,anchor='w',height=55)

        lm4=msg(f14,text=d15[3][1].strip(),bd=0,bg='#404040',fg='#FFFFFF',width=525,font=('SF Pro Display',10))
        lm4.place(relx=0.085,rely=0.745,anchor='w',height=55)

        lm5=msg(f14,text=d15[4][1].strip(),bd=0,bg='#404040',fg='#FFFFFF',width=525,font=('SF Pro Display',10))
        lm5.place(relx=0.085,rely=0.883,anchor='w',height=55)

        ### DATES ###

        lb2=lb(f14,text=d15[0][2],bd=0,bg='#404040',fg='#FFFFFF',font=('SF Pro Display',10))
        lb2.place(relx=0.775,rely=0.335,anchor='w')

        lb3=lb(f14,text=d15[1][2],bd=0,bg='#404040',fg='#FFFFFF',font=('SF Pro Display',10))
        lb3.place(relx=0.775,rely=0.471,anchor='w')

        lb4=lb(f14,text=d15[2][2],bd=0,bg='#404040',fg='#FFFFFF',font=('SF Pro Display',10))
        lb4.place(relx=0.775,rely=0.607,anchor='w')

        lb5=lb(f14,text=d15[3][2],bd=0,bg='#404040',fg='#FFFFFF',font=('SF Pro Display',10))
        lb5.place(relx=0.775,rely=0.745,anchor='w')

        lb6=lb(f14,text=d15[4][2],bd=0,bg='#404040',fg='#FFFFFF',font=('SF Pro Display',10))
        lb6.place(relx=0.775,rely=0.883,anchor='w')


    def attendance1():######################################################  COMPLETED  ##########################################################
        
        f4.place_forget()

        f15=fr(f2,height=500,width=855,bd=0,bg='#000000') 
        f15.place(relx=0.5,rely=0.535,anchor='center')

        lb7=lb(f15,text='Attendance',font=('SF Pro Display',38,'bold'),bd=0,bg='#000000', fg='#FFFFFF')
        lb7.place(relx=0,rely=0.05,anchor='w')

        lb8=lb(f15,image=p29,bd=0)
        lb8.place(relx=0.5,rely=0.55,anchor='center')

        dbcur.execute('select * from attendance where sid="{}"'.format(stid.get()))
        global d17
        d17=dbcur.fetchall()[0]
        
        lb9=lb(f15,text='Number of days present  :',font=('SF Pro Display',16),bd=0,bg='#232323', fg='#FFFFFF')
        lb9.place(relx=0.2,rely=0.2,anchor='w')

        lc1=lb(f15,text='Total number of days  :',font=('SF Pro Display',16),bd=0,bg='#232323', fg='#FFFFFF')
        lc1.place(relx=0.2,rely=0.275,anchor='w')

        lc2=lb(f15,text=d17[1],font=('SF Pro Display',16),bd=0,bg='#232323', fg='#249ADF')
        lc2.place(relx=0.55,rely=0.2,anchor='w')

        lc4=lb(f15,text='180',font=('SF Pro Display',16),bd=0,bg='#232323', fg='#FFFFFF')
        lc4.place(relx=0.55,rely=0.275,anchor='w')

        lc5=lb(f15,text='Status  :',font=('SF Pro Display',16),bd=0,bg='#232323', fg='#FFFFFF')
        lc5.place(relx=0.2,rely=0.35,anchor='w')

        lc6=lb(f15,text='N/A',font=('SF Pro Display',16),bd=0,bg='#232323',fg='#FFFFFF')
        lc6.place(relx=0.55,rely=0.35,anchor='w')

        if d17[1]!='NULL' and d17[1]!=None:
            if int(d17[1])<=180 and int(d17[1])>=163:
                lc6.configure(text='Good',fg='#C9E265')
            if int(d17[1])<=162 and int(d17[1])>=135:  
                lc6.configure(text='Adequate',fg='#8C52FF') 
            if int(d17[1])<=134 and int(d17[1])>=108:  
                lc6.configure(text='Low',fg='#FF914D')
            if int(d17[1])<=107:  
                lc6.configure(text='Critically low',fg='#FF5757')
            
            ## GRAPH ##

            c1=cv(f15,width=230,height=230,bd=0,bg='#232323',highlightbackground='#232323')
            arc=20,20,230,230
            pr=int(d17[1])
            ab=180-(pr)

            c1.create_arc(arc,start=-60,extent="{}".format(-ab),fill='#FF5757',outline='#FF5757') # absent right
            c1.create_arc(arc,start=0,extent="{}".format(pr),fill='#8C52FF',outline='#8C52FF') # present right
            c1.create_arc(arc,start="{}".format(pr),extent=120,fill='#C9E265',outline='#C9E265') # holidays (festivals + weekends)
            c1.create_arc(arc,start=0,extent=-60,fill='#FF914D',outline='#FF914D') # permitted leaves
            c1.place(relx=0.35,rely=0.65,anchor='center')

            lc7=lb(f15,image=p41,bd=0)
            lc7.place(relx=0.68,rely=0.66,anchor='center')


    def projects1():######################################################  COMPLETED  #########################################################
        
        f4.place_forget()
        f16=fr(f2,height=500,width=855,bd=0,bg='#000000') 
        f16.place(relx=0.5,rely=0.535,anchor='center')

        lc8=lb(f16,text='Projects',font=('SF Pro Display',38,'bold'),bd=0,bg='#000000', fg='#FFFFFF')
        lc8.place(relx=0,rely=0.05,anchor='w')

        lc9=lb(f16,image=p42,bd=0)
        lc9.place(relx=0.5,rely=0.56,anchor='center')

        dbcur.execute('select t1,t2,t3,t4,t5 from projects where sid="{}"'.format(stid.get()))
        d19=dbcur.fetchall()[0]
        proj=[]
        date1=[]
        for g in d19:
            y=g.split(',')
            proj.append(y[0])
            date1.append(y[1])
        for d in range(len(proj)):
            if proj[d]=='NULL' or proj[d]==None:
                proj[d]='N/A'
        for f in range(len(date1)):
            if date1[f]=='NULL' or date1[f]==None:
                date1[f]='N/A'

        ## PROJECT ##

        lm6=msg(f16,text=proj[0].strip(),bd=0,bg='#404040',fg='#FFFFFF',width=525,font=('SF Pro Display',16))
        lm6.place(relx=0.35,rely=0.348,anchor='center',height=55)

        lm7=msg(f16,text=proj[1].strip(),bd=0,bg='#404040',fg='#FFFFFF',width=525,font=('SF Pro Display',16))
        lm7.place(relx=0.35,rely=0.484,anchor='center',height=55)

        lm8=msg(f16,text=proj[2].strip(),bd=0,bg='#404040',fg='#FFFFFF',width=525,font=('SF Pro Display',16))
        lm8.place(relx=0.35,rely=0.62,anchor='center',height=55)

        lm9=msg(f16,text=proj[3].strip(),bd=0,bg='#404040',fg='#FFFFFF',width=525,font=('SF Pro Display',16))
        lm9.place(relx=0.35,rely=0.758,anchor='center',height=55)

        ln1=msg(f16,text=proj[4].strip(),bd=0,bg='#404040',fg='#FFFFFF',width=525,font=('SF Pro Display',16))
        ln1.place(relx=0.35,rely=0.896,anchor='center',height=55) 
        
        ## DATE ##

        ld0=lb(f16,text=date1[0],bd=0,bg='#404040',fg='#249ADF',font=('SF Pro Display',16))
        ld0.place(relx=0.785,rely=0.348,anchor='center')

        ld1=lb(f16,text=date1[1],bd=0,bg='#404040',fg='#249ADF',font=('SF Pro Display',16))
        ld1.place(relx=0.785,rely=0.484,anchor='center')

        ld2=lb(f16,text=date1[2],bd=0,bg='#404040',fg='#249ADF',font=('SF Pro Display',16))
        ld2.place(relx=0.785,rely=0.62,anchor='center')

        ld3=lb(f16,text=date1[3],bd=0,bg='#404040',fg='#249ADF',font=('SF Pro Display',16))
        ld3.place(relx=0.785,rely=0.758,anchor='center')

        ld4=lb(f16,text=date1[4],bd=0,bg='#404040',fg='#249ADF',font=('SF Pro Display',16))
        ld4.place(relx=0.785,rely=0.896,anchor='center')

        if date1[0]!='N/A':
            if str_date(date1[0])<date.today():
                ld0.configure(fg='#FF5757')
            if str_date(date1[0])==date.today():
                ld0.configure(fg='#E48F2A')
        if date1[1]!='N/A' :
            if str_date(date1[1])<date.today():
                ld1.configure(fg='#FF5757')
            if str_date(date1[1])==date.today():
                ld1.configure(fg='#E48F2A')
        if date1[2]!='N/A':
            if str_date(date1[2])<date.today():
                ld2.configure(fg='#FF5757')
            if str_date(date1[2])==date.today():
                ld2.configure(fg='#E48F2A')
        if date1[3]!='N/A':
            if str_date(date1[3])<date.today():
                ld3.configure(fg='#FF5757')
            if str_date(date1[3])==date.today():
                ld3.configure(fg='#E48F2A')
        if date1[4]!='N/A':
            if str_date(date1[4])<date.today():
                ld4.configure(fg='#FF5757')
            if str_date(date1[4])==date.today():
                ld4.configure(fg='#E48F2A')


    def assignments1(): ################################################  COMPLETED  #############################################################

        f4.place_forget()

        f17=fr(f2,height=500,width=855,bd=0,bg='#000000') 
        f17.place(relx=0.5,rely=0.535,anchor='center')

        ld5=lb(f17,text='Assignments',font=('SF Pro Display',38,'bold'),bd=0,bg='#000000', fg='#FFFFFF')
        ld5.place(relx=0,rely=0.05,anchor='w')

        ld6=lb(f17,image=p43,bd=0)
        ld6.place(relx=0.5,rely=0.55,anchor='center')

        dbcur.execute('select a1,a2,a3,a4,a5 from assignments where sid="{}"'.format(stid.get()))
        d19=dbcur.fetchall()[0]
        assi=[]
        adate=[]
        sdate=[]
        for i in d19:
            y=i.split(',')                
            assi.append(y[0])
            adate.append(y[1])
            sdate.append(y[2])
        for j in range(len(assi)):
            if assi[j]=='NULL' or assi[j]==None:
                assi[j]='N/A'
        for k in range(len(adate)):
            if adate[k]=='NULL' or adate[k]==None:
                adate[k]='N/A'
        for m in range(len(sdate)):
            if sdate[m]=='NULL' or sdate[m]==None:
                sdate[m]='N/A'
        
        ### ASSIGNNMENT ####
        
        ln2=msg(f17,text=assi[0].strip(),bd=0,bg='#404040',fg='#FFFFFF',width=525,font=('SF Pro Display',16))
        ln2.place(relx=0.29,rely=0.34,anchor='center',height=55) 

        ln3=msg(f17,text=assi[1].strip(),bd=0,bg='#404040',fg='#FFFFFF',width=525,font=('SF Pro Display',16))
        ln3.place(relx=0.29,rely=0.473,anchor='center',height=55)

        ln4=msg(f17,text=assi[2].strip(),bd=0,bg='#404040',fg='#FFFFFF',width=525,font=('SF Pro Display',16))
        ln4.place(relx=0.29,rely=0.612,anchor='center',height=55)

        ln5=msg(f17,text=assi[3].strip(),bd=0,bg='#404040',fg='#FFFFFF',width=525,font=('SF Pro Display',16))
        ln5.place(relx=0.29,rely=0.75,anchor='center',height=55)

        ln6=msg(f17,text=assi[4].strip(),bd=0,bg='#404040',fg='#FFFFFF',width=525,font=('SF Pro Display',16))
        ln6.place(relx=0.29,rely=0.89,anchor='center',height=55)

        ### DATE OF ASSIGNMENT ###

        ld5=lb(f17,text=adate[0],bd=0,bg='#404040',fg='#FFFFFF',font=('SF Pro Display',16))
        ld5.place(relx=0.6275,rely=0.34,anchor='center')

        ld6=lb(f17,text=adate[1],bd=0,bg='#404040',fg='#FFFFFF',font=('SF Pro Display',16))
        ld6.place(relx=0.6275,rely=0.473,anchor='center')

        ld7=lb(f17,text=adate[2],bd=0,bg='#404040',fg='#FFFFFF',font=('SF Pro Display',16))
        ld7.place(relx=0.6275,rely=0.612,anchor='center')

        ld8=lb(f17,text=adate[3],bd=0,bg='#404040',fg='#FFFFFF',font=('SF Pro Display',16))
        ld8.place(relx=0.6275,rely=0.75,anchor='center')

        ld9=lb(f17,text=adate[4],bd=0,bg='#404040',fg='#FFFFFF',font=('SF Pro Display',16))
        ld9.place(relx=0.6275,rely=0.89,anchor='center')

        ### DATE OF SUBMISSION ###

        lf1=lb(f17,text=sdate[0],bd=0,bg='#404040',fg='#FFFFFF',font=('SF Pro Display',16))
        lf1.place(relx=0.8365,rely=0.34,anchor='center')

        lf2=lb(f17,text=sdate[1],bd=0,bg='#404040',fg='#FFFFFF',font=('SF Pro Display',16))
        lf2.place(relx=0.8365,rely=0.473,anchor='center')

        lf3=lb(f17,text=sdate[2],bd=0,bg='#404040',fg='#FFFFFF',font=('SF Pro Display',16))
        lf3.place(relx=0.8365,rely=0.612,anchor='center')

        lf4=lb(f17,text=sdate[3],bd=0,bg='#404040',fg='#FFFFFF',font=('SF Pro Display',16))
        lf4.place(relx=0.8365,rely=0.75,anchor='center')

        lf5=lb(f17,text=sdate[4],bd=0,bg='#404040',fg='#FFFFFF',font=('SF Pro Display',16))
        lf5.place(relx=0.8365,rely=0.89,anchor='center')

        if sdate[0]!='N/A':
            if str_date(sdate[0])<date.today():
                lf1.configure(fg='#FF5757')
            if str_date(sdate[0])==date.today():
                lf1.configure(fg='#E48F2A')
        if sdate[1]!='N/A' :
            if str_date(sdate[1])<date.today():
                lf2.configure(fg='#FF5757')
            if str_date(sdate[1])==date.today():
                lf2.configure(fg='#E48F2A')
        if sdate[2]!='N/A':
            if str_date(sdate[2])<date.today():
                lf3.configure(fg='#FF5757')
            if str_date(sdate[2])==date.today():
                lf3.configure(fg='#E48F2A')        
        if sdate[3]!='N/A':
            if str_date(sdate[3])<date.today():
                lf4.configure(fg='#FF5757')
            if str_date(sdate[3])==date.today():
                lf4.configure(fg='#E48F2A')
        if sdate[4]!='N/A':
            if str_date(sdate[4])<date.today():
                lf5.configure(fg='#FF5757')
            if str_date(sdate[4])==date.today():
                lf5.configure(fg='#E48F2A')


    def about1():####################################################################    COMPLETE    ###############################################
        f4.place_forget()
        global f6    
        f6=fr(f2,height=500,width=855,bd=0,bg='#000000') 
        f6.place(relx=0.5,rely=0.535,anchor='center')

        l27=lb(f6,image=p29,bd=0)
        l27.place(relx=0.5,rely=0.55,anchor='center')

        dbcur.execute('select * from about')
        d7=(dbcur.fetchall())[0][0]  

        m1=msg(f6,text=d7.strip(),bd=0,bg='#232323',fg='#FFFFFF',font=('SF Pro Display',12))
        m1.place(relx=0.5,rely=0.55,anchor='center',width=750,height=400)

        l26=lb(f6,text='About',font=('SF Pro Display',38,'bold'),bd=0,bg='#000000',fg='#FFFFFF')
        l26.place(relx=0,rely=0.05,anchor='w')
                 
                                            
    def adlogin():######################################################################### COMPLETE #####################################################################
        adminbt.place_forget()
        studentbt.place_forget()

        l7=lb(f1,image=p21,bd=0)
        l7.place(relx=0.75,rely=0.61,anchor='center')
            
        l3 = lb(f1,text = 'ID',bg = '#232323' , fg = '#FFFFFF',font = ('SF Pro Display',15))
        l3.place(relx = 0.64 , rely = 0.54,anchor = 'center')
            
        l4 = lb(f1,text = 'Password',bg = '#232323' , fg = '#FFFFFF',font = ('SF Pro Display',15))
        l4.place(relx = 0.64 , rely = 0.6 , anchor = 'center')

        l8=lb(f1,image=p23,bd=0)
        l8.place(relx=0.8,rely=0.54,anchor='center')

        l9=lb(f1,image=p23,bd=0)
        l9.place(relx=0.8,rely=0.6,anchor='center')
        
        global aid
        aid= ent(f1,bd = 0 ,font=('SF Pro Display',12)) 
        aid.place(relx = 0.8,rely = 0.54,anchor = 'center')

        key = ent(f1,bd = 0  , show = '*' ,font=('SF Pro Display',12)) 
        key.place(relx = 0.8,rely = 0.6,anchor = 'center') 

        def adverify():
            dbcur.execute('select id from adminlogin')
            global d8
            d8=dbcur.fetchall()  
            if aid.get()=='' or key.get()=='' :
                msgb.showwarning('Invalid entry','   Please fill both fields.   ')
                key.delete(0,END)
                
            if (aid.get(),) not in d8 and (aid.get()!='' and key.get()!=''):#((id.get().startswith('Taiit')==False or len(id.get())<=5) 
                msgb.showwarning('Invalid entry','      Invalid ID      ')
                aid.delete(0,END)
                key.delete(0,END)
                                        
            for i in d8:                                             
                if aid.get()==i[0]:
                    dbcur.execute('select pass from adminlogin where id="{}"'.format(aid.get()))
                    d9=dbcur.fetchall()          
                    if key.get()==d9[0][0]:
                        adminhome() 
                    elif key.get()!=d9[0][0] and key.get()!='' :
                        msgb.showwarning('Invalid entry','There was an error, Incorrect ID and Password combination.')
                        key.delete(0,END)  

        b3=bt(f1,image=p7,bd = 0, bg='#232323',activebackground='#232323',command=adverify)
        b3.place(relx = 0.85,rely=0.69,anchor='center')
        ANIMATE(b3,p7)

        b4=bt(f1,text= 'Forgot your Password ?',font = ('SF Pro Display',10,UNDERLINE),
        bd = 0,bg = '#232323',fg='#737373',activebackground = '#232323',command=forgpass)
        b4.place(relx=0.83,rely=0.643,anchor='center')

        b5=bt(f1,image=p8,bd=0,bg='#000000',activebackground='#000000',command=main)
        b5.place(relx=0.03,rely=0.05,anchor='center')
        ANIMATE(b5,p8)
    
    
    def stlogin():
        adminbt.place_forget()
        studentbt.place_forget()

        l7=lb(f1,image=p21,bd=0)
        l7.place(relx=0.75,rely=0.61,anchor='center')
            
        l3 = lb(f1,text = 'ID',bg = '#232323' , fg = '#FFFFFF',font = ('SF Pro Display',15))
        l3.place(relx = 0.64 , rely = 0.54,anchor = 'center')
            
        l4 = lb(f1,text = 'Password',bg = '#232323' , fg = '#FFFFFF',font = ('SF Pro Display',15))
        l4.place(relx = 0.64 , rely = 0.6 , anchor = 'center')

        l8=lb(f1,image=p23,bd=0)
        l8.place(relx=0.8,rely=0.54,anchor='center')

        l9=lb(f1,image=p23,bd=0)
        l9.place(relx=0.8,rely=0.6,anchor='center')
        
        global stid
        stid= ent(f1,bd = 0 ,font=('SF Pro Display',12)) 
        stid.place(relx = 0.8,rely = 0.54,anchor = 'center')

        skey = ent(f1,bd = 0  , show = '*' ,font=('SF Pro Display',12)) 
        skey.place(relx = 0.8,rely = 0.6,anchor = 'center') 

        def stverify():
            dbcur.execute('select id from slogin')
            global d8
            d8=dbcur.fetchall()  
            if stid.get()=='' or skey.get()=='' :
                msgb.showwarning('Invalid entry','   Please fill both fields.   ')
                skey.delete(0,END)
                
            if (stid.get(),) not in d8 and (stid.get()!='' and skey.get()!=''): 
                msgb.showwarning('Invalid entry','      Invalid ID      ')
                stid.delete(0,END)
                skey.delete(0,END)
                                        
            for i in d8:                                             
                if stid.get()==i[0]:
                    dbcur.execute('select pass from slogin where id="{}"'.format(stid.get()))
                    d9=dbcur.fetchall()          
                    if skey.get()==d9[0][0]:
                        studenthome() 
                    elif skey.get()!=d9[0][0] and skey.get()!='' :
                        msgb.showwarning('Invalid entry','There was an error, Incorrect ID and Password combination.')
                        skey.delete(0,END) 
        def forgpassmsg():
            lb(f1,text='To reset your account password, Please contact the Administrator.',
            bg = '#000000', fg = '#FFFFFF',font = ('SF Pro Display',12)).place(relx=0.75,rely=0.85,anchor='center')

        b3=bt(f1,image=p7,bd = 0, bg='#232323',activebackground='#232323',command=stverify)
        b3.place(relx = 0.85,rely=0.69,anchor='center')
        ANIMATE(b3,p7)

        b4=bt(f1,text= 'Forgot your Password ?',font = ('SF Pro Display',10,UNDERLINE),
        bd = 0,bg = '#232323',fg='#737373',activebackground = '#232323',command=forgpassmsg)
        b4.place(relx=0.83,rely=0.643,anchor='center')

        b5=bt(f1,image=p8,bd=0,bg='#000000',activebackground='#000000',command=main)
        b5.place(relx=0.03,rely=0.05,anchor='center')
        ANIMATE(b5,p8)


    def main():####################################################################  COMPLETE  ########################################################################
        
        # main frame

        global f1
        f1=fr(win,height=650,width=1150,bd=0 ,bg='#000000')
        f1.place(relx=0.5,rely=0.5,anchor = 'center')
        
        # universitrely logo
        
        l=lb(f1,image=p1,bd=0,bg = '#000000')
        l.place(relx=0.25,rely=0.5,anchor='center')
        
        # sign in prompt

        l1=lb(f1,text='Please Sign In.',bg = '#000000',fg = '#FFFFFF',font = ('SF Pro Display',38,'bold'))
        l1.place(relx=0.75,rely=0.35,anchor='center')

        # login button 1
        
        global adminbt
        adminbt=bt(f1,image = p2,bd = 0,bg = '#000000', activebackground = '#000000',command =adlogin)
        adminbt.place(relx=0.75,rely=0.55,anchor='center')
        
        # login button 2

        global studentbt
        studentbt=bt(f1,image = p2,bd = 0,bg = '#FFFFFF', activebackground = '#000000',command =stlogin)
        studentbt.place(relx=0.75,rely=0.65,anchor='center')

        def hovereffect():                         
            def switch1(a):
                adminbt.configure(image=p3)
                adminbt.image=p3
            def reverse1(a):
                adminbt.configure(image=p2)
                adminbt.image=p2
            def switch2(a):
                studentbt.configure(image=p3)
                studentbt.image=p3
            def reverse2(a):
                studentbt.configure(image=p2)
                studentbt.image=p2

            adminbt.bind('<Enter>',switch1)
            adminbt.bind('<Leave>',reverse1)
            studentbt.bind('<Enter>',switch2)
            studentbt.bind('<Leave>',reverse2)
        hovereffect()               
                
        # division bar    
        
        l2=lb(f1,image = p6,bd = 0,bg = "#000000")
        l2.place(relx = 0.5 , rely = 0.55 , anchor = 'center')

        win.mainloop()

    try: 
        dbcon=db.connect(host='localhost',user='root',password='mysql',database='proj_vidul')
        if dbcon.is_connected()==True:
            dbcur=dbcon.cursor()
    except:
        msgb.showwarning(
            'Database Error','There was some problem with the associated database, Please try again later')
    else:
        main()        
except :
    msgb.showwarning('Unexpected error',"There was an unexpected error, we're trying to solve it. Please close the app and start it again.")




















































