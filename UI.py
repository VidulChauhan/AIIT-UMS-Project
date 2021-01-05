try:
    import mysql.connector as db
    from tkinter import *
    from tkinter import messagebox
    from random import *
    from datetime import *
    from twilio.rest import Client
    import time as t
    import os
    ph=PhotoImage
    lb=Label
    bt=Button
    fr=Frame
    ent=Entry
    msgb=messagebox   
    tx=Text       
    msg=Message
    dt=datetime
    day=dt.now().strftime('%A')
    month=dt.now().strftime('%B')
    DD=str(dt.now().day)
    YY=str(dt.now().year)
    DATE=day+', '+DD+' '+month+' '+YY
    curtime=dt.now().time()

    #root window 
    win=Tk()
    win.geometry('1150x650')
    win.title('All India Institute of Technology')
    win.configure(bg='#000000')
    win.resizable(False,False)


    #title bar icon change
    p=ph(file  = 'titlelogo.png')#title icon 
    p1=ph(file = 'main.png')#main screen logo
    p2=ph(file = 'loginbutton1.png') #login button
    p3=ph(file = 'loginbutton2.png')
    p6=ph(file = 'divbar.png')
    p7=ph(file = 'gobutton.png') 
    p8=ph(file = 'backbutton.png')
    p9=ph(file = 'aiit.png')
    p10=ph(file = 'signout.png')
    p11=ph(file = 'profile2.png')
    p12=ph(file = 'assignments2.png')
    p13=ph(file = 'fee2.png')
    p14=ph(file = 'projects2.png')
    p15=ph(file = 'events2.png')
    p16=ph(file = 'attendance2.png')
    p17=ph(file = 'about2.png')
    p18=ph(file = 'marks2.png')
    p19=ph(file = 'passreset2.png')
    p20=ph(file = 'hb.png')
    p21=ph(file = 'loginbg2.png')
    p22=ph(file = 'abtlogo.png')
    p23=ph(file = 'entrybar.png')
    p24=ph(file = 'sidbar.png')
    p25=ph(file = 'profilebg.png')
    p26=ph(file = 'boyicon.png')
    p27=ph(file = 'girlicon.png')
    p28=ph(file = 'editbutton.png')
    p29=ph(file = 'abtbg.png')
    p30=ph(file = 'apassr.png')
    p32=ph(file = 'spassr.png')#1st
    p33=ph(file = 'txbar bg.png')
    p34=ph(file = 'marksbg.png')
    p35=ph(file = '+admin.png')
    p36=ph(file = '+student.png')


    win.iconphoto(None,p)#title bar image

    def home():#####################################################################  COMPLETE  #############################################################
        f1.place_forget()
        global f2
        f2=fr(win,bd=0,height=650,width=1150,bg='#000000')#bigger one
        f2.place(relx=0.5,rely=0.5,anchor='center') 
        global f3
        f3=fr(win,bd=0,height=100,width=1150,bg='#232323')#smaller one
        f3.place(relx=0.5,rely=0,anchor='center')
        l28=lb(f3,text=DATE,bd=0,font=('SF Pro Display',13),bg='#232323',fg='#FFFFFF') 
        l28.place(relx=0.715,rely=0.755,anchor='center')
        l29=lb(f2,bd=0,bg='#000000',fg='#FFFFFF',font=('SF Pro Display',22,'bold'))
        l29.place(relx=0.5,rely=0.11,anchor='center')
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
        global f4
        f4=fr(f2,height=500,width=855,bd=0,bg='#000000') 
        f4.place(relx=0.5,rely=0.535,anchor='center')
        b7=bt(f4,image=p11,bd=0,bg='#000000',activebackground='#000000',command=sprofile)#profile
        b7.place(relx=0.1385,rely=0.236,anchor='center')
        b8=bt(f4,image=p12,bd=0,bg='#000000',activebackground='#000000',command=assignments)#assignments
        b8.place(relx=0.466,rely=0.688,anchor='center')
        b9=bt(f4,image=p14,bd=0,bg='#000000',activebackground='#000000',command=projects)#projects
        b9.place(relx=0.392,rely=0.182,anchor='center')
        b10=bt(f4,image=p18,bd=0,bg='#000000',activebackground='#000000',command=marks)#marks
        b10.place(relx=0.7515,rely=0.182,anchor='center')
        b11=bt(f4,image=p16,bd=0,bg='#000000',activebackground='#000000',command=attendance)#attendance
        b11.place(relx=0.13855,rely=0.62,anchor='center')
        b12=bt(f4,image=p15,bd=0,bg='#000000',activebackground='#000000',command=events)#events
        b12.place(relx=0.13855,rely=0.8825,anchor='center')
        b13=bt(f4,image=p19,bd=0,bg='#000000',activebackground='#000000',command=passr)#passreset
        b13.place(relx=0.738,rely=0.52,anchor='center')
        b14=bt(f4,image=p17,bd=0,bg='#000000',activebackground='#000000',command=about)#about
        b14.place(relx=0.912,rely=0.52,anchor='center')
        b15=bt(f4,image=p13,bd=0,bg='#000000',activebackground='#000000',command=fee_details)#fee
        b15.place(relx=0.8263,rely=0.828,anchor='center')
        b16=bt(f3,image=p20,bd=0,bg='#232323',activebackground ='#232323',command=home)# home button
        b16.place(relx=0.5,rely=0.75,anchor='center')
        b39=bt(f2,image=p35,bd=0,bg='#000000',activebackground='#000000',command=addadmin)
        b39.place(relx=0.01,rely=0.115,anchor='w')
        b40=bt(f2,image=p36,bd=0,bg='#000000',activebackground='#000000',command=addstudent)
        b40.place(relx=0.01,rely=0.175,anchor='w')
        l11=lb(f3,image=p24,bd=0)
        l11.place(relx=0.35,rely=0.75,anchor='center')
        l12=lb(f3,text='Student ID ',font=('SF Pro Display',13),bd=0,bg='#232323',fg='#FFFFFF')
        l12.place(relx=0.275,rely=0.75,anchor='center')
        global sid
        sid=ent(f3,bd=0,font=('SF Pro Display',13),width=6)# sid for profile
        sid.place(relx=0.35,rely=0.75,anchor='center')
        
    
    def addstudent():  #############################  ISKA DBCUR.EXECUTE ME EK DO AUR ADD HONGE VO DEKHLIYO  ###################################
        f4.place_forget()
        global f12
        f12=fr(f2,height=500,width=855,bd=0,bg='#000000') 
        f12.place(relx=0.5,rely=0.535,anchor='center')
        l6=lb(f12,text='Add Student account',font=('SF Pro Display',38,'bold'),bd=0,bg='#000000', fg='#FFFFFF')
        l6.place(relx=0,rely=0.05,anchor='w')           
        l83=lb(f12,image=p25,bd=0)            
        l83.place(relx=0.5,rely=0.55,anchor='center')
    
        s1=ent(f12,bd=0,font=('SF Pro Display',14),width=14)# for student name
        s1.place(relx=0.29,rely=0.29,anchor='w')
        
        s2=ent(f12,bd=0,font=('SF Pro Display',14),width=14)#for student mobile
        s2.place(relx=0.29,rely=0.383,anchor='w')
        
        s3=ent(f12,bd=0,font=('SF Pro Display',14),width=14)# for current year
        s3.place(relx=0.29,rely=0.475,anchor='w')
        
        s4=ent(f12,bd=0,font=('SF Pro Display',14),width=16)# for student admission
        s4.place(relx=0.6925,rely=0.29,anchor='w')
        
        s5=ent(f12,bd=0,font=('SF Pro Display',14),width=16) # for course
        s5.place(relx=0.6925,rely=0.383,anchor='w')
        
        s6=ent(f12,bd=0,font=('SF Pro Display',14),width=4)# for blood group
        s6.place(relx=0.825,rely=0.473,anchor='w')

        s7=ent(f12,bd=0,font=('SF Pro Display',13),width=6)#for gender
        s7.place(relx=0.095,rely=0.515,anchor='center')
        s7.insert(0,'M/F')

        s8=ent(f12,bd=0,font=('SF Pro Display',14),width=14)# for father's name
        s8.place(relx=0.29,rely=0.688,anchor='w')
        
        s9=ent(f12,bd=0,font=('SF Pro Display',14),width=14)#father's number
        s9.place(relx=0.29,rely=0.782,anchor='w')
        
        s10=ent(f12,bd=0,font=('SF Pro Display',14),width=14)# for mother's name
        s10.place(relx=0.78,rely=0.688,anchor='w')

        s11=ent(f12,bd=0,font=('SF Pro Display',14),width=14)#mother's number
        s11.place(relx=0.78,rely=0.782,anchor='w')
        
        s12=ent(f12,bd=0,font=('SF Pro Display',14),width=8)
        s12.place(relx=0.5425,rely=0.473,anchor='w')

        def nstudent_save():            
            a=0 #for names
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
            for c in s1.get():#sname checked.
                if c.isdigit()==True:
                    a+=1
            for c1 in s8.get():#fname checked.
                if c1.isdigit()==True:
                    a+=1
            for c2 in s10.get():#mname checked.
                if c2.isdigit()==True:
                    a+=1                  
            for no in s2.get():#sph cheked.
                if no.isdigit()!=True:
                    b+=1 
            for no1 in s9.get():#fph cheked.
                if no1.isdigit()!=True:
                    b+=1
            for no2 in s11.get():#mph checked.
                if no2.isdigit()!=True:
                    b+=1              
            for w1 in s5.get(): #course checked.
                if w1.isdigit()==True:
                    d+=1
            for i1 in s12.get()[5:]:
                if i1 in list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'):
                    s+=1
            for a1 in s4.get()[1:]:
                if a1 in list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'):
                    ad+=1

            if sg!=0:
                msgb.showwarning('Invalid entry','Please enter data in all fileds before saving.')                
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
                if s4.get().startswith('S')==False or ad!=0:    #admission number checked                
                    msgb.showwarning('Invalid entry',"Admission number is not valid,\nIt can only begin with a 'S'\nPlease try again.")
                    e+=1                
                if d!=0:   
                    msgb.showwarning('Invalid entry','Course is not valid, please try again.')   
                    e+=1             
                if s6.get() not in l2: #blood group checked.
                    msgb.showwarning('Invalid entry','Please check blood group and try again.') 
                    e+=1               
                if s7.get() not in ['male','female','Male','Female','M','F','m','f']:   #gender checked.
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
                            dbcon.commit()
                            msgb.showinfo('Message','Account added successfully.')
                            msgb.showinfo('Message','Since this will be a new account, therefore all other data branches such as password,assignments,attendance,etc are also not set-up.\n'
                                        'For now, all information regarding acedemics including credentials has been set to NULL.\n'
                                        'You can change this in the future. ')
                            home()
                        except:
                            msgb.showwarning('Unexpected error','Please check all fields or try again later.')
        b41=bt(f12,text='Save',bd=0,font=('SF Pro Display',15),bg='#000000',fg='#FFFFFF',activebackground='#000000',command=nstudent_save)
        b41.place(relx=0.95,rely=0.1,anchor='center') 
        b42=bt(f12,text='Cancel',bd=0,font=('sf pro display',15),bg='#000000',fg='#FFFFFF',activebackground='#000000',command=home)  
        b42.place(relx=0.85,rely=0.1,anchor='center')

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

        l85=lb(f13,text='ID',bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
        l85.place(relx=0.2,rely=0.3,anchor='w')
        l85=lb(f13,text='Phone number :',bd=0,font=('SF Pro Display',16),bg='#232323',fg='#FFFFFF')
        l85.place(relx=0.2,rely=0.4,anchor='w')
        l86=lb(f13,text='New password :',bd=0,font=('SF Pro Display',16),bg='#232323',fg='#FFFFFF')
        l86.place(relx=0.2,rely=0.5,anchor='w')
        l87=lb(f13,text='Confirm new password :',bd=0,font=('SF Pro Display',16),bg='#232323',fg='#FFFFFF')
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
        phno=ent(f13,bd=0,bg='#F2F2F2',font=('SF Pro Display',16),width=10) #ph
        phno.place(relx=0.475,rely=0.4,anchor='w')
        napass=ent(f13,bd=0,bg='#F2F2F2',font=('SF Pro Display',16),width=10) #new
        napass.place(relx=0.475,rely=0.5,anchor='w')
        cnapass=ent(f13,bd=0,bg='#F2F2F2',font=('SF Pro Display',16),width=10) #new confirmed
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
                                home()
                            except:
                                msgb.showwarning('Unexpected error','Please check all fields or try again later.')

                
        b43=bt(f13,text='Save',bd=0,font=('SF Pro Display',15),bg='#000000',fg='#FFFFFF',activebackground='#000000',command=nadmin_save)
        b43.place(relx=0.95,rely=0.0875,anchor='center') 
        b44=bt(f13,text='Cancel',bd=0,font=('sf pro display',15),bg='#000000',fg='#FFFFFF',activebackground='#000000',command=home)  
        b44.place(relx=0.85,rely=0.0875,anchor='center')  
    
    def forgpass():#####################################################################  COMPLETE  #############################################################
        f1.place_forget()
        global f8
        f8=fr(win,height=500,width=855,bd=0,bg='#000000')
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
                l40=lb(f8,text="We'll send an OTP the your registered mobile number ending with  {} .".format(Pn),
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
                        try:
                                                
                            mid='AC941df350e2684f45d0e175d4faf8e132'
                            auth='c5a3cae2b44f3417b71750f66b3a0f39'
                            cl=Client(mid,auth)
                            global onet
                            onet=randrange(635745,952675)
                            sms=cl.messages.create(from_='+17656256436',
                            body='Hi Administrator, {} is the following code to reset your password. DO NOT share this with anyone'.format(onet),
                            to="{}".format('+91'+phn))
                            msgb.showinfo('Forgot password','   OTP sent successfully.   ')
                            scount.append('clicked')
                            print(sms.mid)
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
                            t.sleep(0.5)
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
                                f1.place(relx=0.5,rely=0.5,anchor = 'center')
                            b31=bt(f9,text='Cancel',font=('SF Pro Display',16),bd=0,bg='#000000',activebackground='#000000',fg='#FFFFFF',command=cancel2)
                            b31.place(relx=0.9,rely=0.08,anchor='center')
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
                b30=bt(f8,text='Verify',font=('SF Pro Display',16),bd=0,bg='#232323',activebackground='#232323',fg='#FFFFFF',command=fverify)
                b30.place(relx=0.525,rely=0.825,anchor='center')
        
        def cancel1():
            f8.place_forget()
            f1.place(relx=0.5,rely=0.5,anchor = 'center')

        b27=bt(f8,text='Go',bd=0,font=('SF Pro Display',16),bg='#232323',fg='#249ADF',activebackground='#232323',command=go)
        b27.place(relx=0.6,rely=0.3,anchor='center')
        b28=bt(f8,text='Cancel',bd=0,font=('SF Pro Display',16),bg='#000000',fg='#FFFFFF',activebackground='#000000',command=cancel1)
        b28.place(relx=0.9,rely=0.08,anchor='center')
        
    def passr():#####################################################################  COMPLETE  #############################################################    
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
            curpass=ent(f7,bd=0,bg='#F2F2F2',font=('SF Pro Display',16),width=10)#cur
            curpass.place(relx=0.475,rely=0.3,anchor='w')
            newpass=ent(f7,bd=0,bg='#F2F2F2',font=('SF Pro Display',16),width=10)#new
            newpass.place(relx=0.475,rely=0.4,anchor='w')
            cnewpass=ent(f7,bd=0,bg='#F2F2F2',font=('SF Pro Display',16),width=10)#new confirmed
            cnewpass.place(relx=0.475,rely=0.5,anchor='w')
            global b25
            b25=bt(f7,text= 'Forgot your Password ?',font = ('SF Pro Display',10,UNDERLINE),
            bd = 0,bg = '#232323',fg='#737373',activebackground = '#232323',command=forgpass)
            b25.place(relx=0.675,rely=0.3,anchor='w')
                
            def apass_save():
                dbcur.execute('select * from adminlogin where id="{}"'.format(id.get()))
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
                            dbcur.execute('update adminlogin set pass="{}" where id="{}"'.format(cnewpass.get(),id.get()))
                            dbcon.commit()
                            msgb.showinfo('Operation successful','Password changed successfully.\nPlease re-login for changes to take effect.')
                except:
                    msgb.showinfo('Unexpected error','Please check all fields and try again.')
            b26=bt(f7,text='Save',bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF',activebackground='#232323',command=apass_save)
            b26.place(relx=0.7,rely=0.6,anchor='center')

        def spassreset():
            l32.place_forget()
            b25.place_forget()
            l53=lb(f7,text='Enter ID :',bd=0,font=('SF Pro Display',16),bg='#232323',fg='#FFFFFF')
            l53.place(relx=0.2,rely=0.3,anchor='w')
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
            Sid=ent(f7,bd=0,bg='#F2F2F2',font=('SF Pro Display',16),width=10)#cur
            Sid.place(relx=0.475,rely=0.3,anchor='w')
            newspass=ent(f7,bd=0,bg='#F2F2F2',font=('SF Pro Display',16),width=10)#new
            newspass.place(relx=0.475,rely=0.4,anchor='w')
            cnewspass=ent(f7,bd=0,bg='#F2F2F2',font=('SF Pro Display',16),width=10)#new confirmed
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
            b26=bt(f7,text='Save',bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF',activebackground='#232323',command=spass_save)
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
        b24=bt(f7,image=p32,bd=0,bg='#232323',activebackground='#232323',command=spassreset)
        b24.place(relx=0.501,rely=0.177,anchor='w')
        apassreset()       

        
    def sprofile():##########################################################   COMPLETE   ##################################################
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
                #global rec
                rec=d6[0]
                l10=lb(f5,image=p25,bd=0)            
                l10.place(relx=0.5,rely=0.55,anchor='center')
                if rec[10] in ['male','Male','M','m']:
                    l13=lb(f5,image=p26,bd=0)
                    l13.place(relx=0.095,rely=0.375,anchor='center')
                if rec[10] in ['female','Female','F','f']:
                    l13=lb(f5,image=p27,bd=0)
                    l13.place(relx=0.095,rely=0.375,anchor='center')
                l14=lb(f5,text='{}'.format(rec[2]),bd=0,font=('SF Pro Display',16),bg='#232323',fg='#FFFFFF')# sname
                l14.place(relx=0.29,rely=0.29,anchor='w')   
                l15=lb(f5,text='{}'.format(rec[5]),bd=0,font=('SF Pro Display',16),bg='#232323',fg='#FFFFFF')# student ph
                l15.place(relx=0.29,rely=0.383,anchor='w') 
                l16=lb(f5,text='{}'.format(rec[9]),bd=0,font=('SF Pro Display',16),bg='#232323',fg='#FFFFFF')# year
                l16.place(relx=0.29,rely=0.475,anchor='w')
                l17=lb(f5,text='{}'.format(rec[1]),bd=0,font=('SF Pro Display',16),bg='#232323',fg='#FFFFFF')# admission number 
                l17.place(relx=0.6925,rely=0.29,anchor='w')
                l18=lb(f5,text='{}'.format(rec[8]),bd=0,font=('SF Pro Display',16),bg='#232323',fg='#FFFFFF')# course  
                l18.place(relx=0.6925,rely=0.383,anchor='w')
                l19=lb(f5,text='{}'.format(rec[0]),bd=0,font=('SF Pro Display',16),bg='#232323',fg='#FFFFFF')# id
                l19.place(relx=0.5425,rely=0.473,anchor='w')
                l20=lb(f5,text='{}'.format(rec[11]),bd=0,font=('SF Pro Display',16),bg='#232323',fg='#FFFFFF')# blood group
                l20.place(relx=0.825,rely=0.473,anchor='w')
                l21=lb(f5,text='{}'.format(rec[3]),bd=0,font=('SF Pro Display',16),bg='#232323',fg='#FFFFFF')# fname
                l21.place(relx=0.29,rely=0.688,anchor='w')
                l22=lb(f5,text='{}'.format(rec[6]),bd=0,font=('SF Pro Display',16),bg='#232323',fg='#FFFFFF')# father ph
                l22.place(relx=0.29,rely=0.782,anchor='w')
                l23=lb(f5,text='{}'.format(rec[4]),bd=0,font=('SF Pro Display',16),bg='#232323',fg='#FFFFFF')# mname
                l23.place(relx=0.78,rely=0.688,anchor='w')
                l24=lb(f5,text='{}'.format(rec[7]),bd=0,font=('SF Pro Display',16),bg='#232323',fg='#FFFFFF')# mother ph
                l24.place(relx=0.78,rely=0.782,anchor='w')
                l25=lb(f5,text='{}'.format(rec[10].capitalize()),bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') #gender 
                l25.place(relx=0.095,rely=0.515,anchor='center')          
                
                def profile_edit():
                    b17.place_forget()                    
                    sname_e=ent(f5,bd=0,font=('SF Pro Display',14),width=14)# for student name
                    sname_e.place(relx=0.29,rely=0.29,anchor='w')
                    sname_e.insert(0,rec[2])
                    sph_e=ent(f5,bd=0,font=('SF Pro Display',14),width=14)#for student mobile
                    sph_e.place(relx=0.29,rely=0.383,anchor='w')
                    sph_e.insert(0,rec[5])
                    y_e=ent(f5,bd=0,font=('SF Pro Display',14),width=14)# for current year
                    y_e.place(relx=0.29,rely=0.475,anchor='w')
                    y_e.insert(0,rec[9])
                    admn_e=ent(f5,bd=0,font=('SF Pro Display',14),width=16)# for student admission
                    admn_e.place(relx=0.6925,rely=0.29,anchor='w')
                    admn_e.insert(0,rec[1])
                    crs_e=ent(f5,bd=0,font=('SF Pro Display',14),width=16) # for course
                    crs_e.place(relx=0.6925,rely=0.383,anchor='w')
                    crs_e.insert(0,rec[8])
                    bld_e=ent(f5,bd=0,font=('SF Pro Display',14),width=4)# for blood group
                    bld_e.place(relx=0.825,rely=0.473,anchor='w')
                    bld_e.insert(0,rec[11])
                    gdr_e=ent(f5,bd=0,font=('SF Pro Display',13),width=6)#for gender
                    gdr_e.place(relx=0.095,rely=0.515,anchor='center')
                    gdr_e.insert(0,rec[10])
                    fname_e=ent(f5,bd=0,font=('SF Pro Display',14),width=14)# for father's name
                    fname_e.place(relx=0.29,rely=0.688,anchor='w')
                    fname_e.insert(0,rec[3])
                    fph_e=ent(f5,bd=0,font=('SF Pro Display',14),width=14)#father's number
                    fph_e.place(relx=0.29,rely=0.782,anchor='w')
                    fph_e.insert(0,rec[6])
                    mname_e=ent(f5,bd=0,font=('SF Pro Display',14),width=14)# for mother's name
                    mname_e.place(relx=0.78,rely=0.688,anchor='w')
                    mname_e.insert(0,rec[4])
                    mph_e=ent(f5,bd=0,font=('SF Pro Display',14),width=14)#mother's number
                    mph_e.place(relx=0.78,rely=0.782,anchor='w')
                    mph_e.insert(0,rec[7])

                    def profile_save():
                        a=0 #for names
                        b=0
                        c=0
                        d=0
                        r=0
                        ad=0
                        for ch in sname_e.get():#sname checked.
                            if ch.isdigit()==True:
                                a+=1
                        for ch1 in fname_e.get():#fname checked.
                            if ch1.isdigit()==True:
                                a+=1
                        for ch2 in mname_e.get():#mname checked.
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
                            
                        for n in sph_e.get():#sph cheked.
                            if n.isdigit()!=True:
                                b+=1 
                        for n1 in fph_e.get():#fph cheked.
                            if n1.isdigit()!=True:
                                b+=1
                        for n2 in mph_e.get():#mph checked.
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
                            
                        l=['1st year','2nd year','3rd year','Final year']#year checked.
                        if y_e.get() not in l:
                            msgb.showwarning('Invalid entry','    Please check year.    ')
                            y_e.delete(0,END)
                            r+=1     

                        for ad1 in admn_e.get()[1:]:
                            if ad1 in list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'):
                                ad+=1
                        if admn_e.get().startswith('S')==False or ad!=0:
                            c+=1
                        if c!=0:    
                            #admission number checked
                            msgb.showwarning('Invalid entry','Admission number is not valid, please try again.')
                            admn_e.delete(0,END)
                            admn_e.insert(0,rec[1])
                            r+=1

                        for w in crs_e.get():#course checked.
                            if w.isdigit()==True:
                                d+=1  
                        if d!=0:   
                            msgb.showwarning('Invalid entry','Course is not valid, please try again.')
                            crs_e.delete(0,END)
                            crs_e.insert(0,rec[8])
                            r+=1
                        l2=['+A','+B','+O','-O','+AB','-AB','-A','-B'] #blood group checked.
                        if bld_e.get() not in l2:
                            msgb.showwarning('Invalid entry','Please check blood group and try again.')
                            bld_e.delete(0,END)
                            bld_e.insert(0,rec[11])
                            r+=1
                        if gdr_e.get() not in ['male','female','Male','Female']:#gender checked.
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
    
                    b18=bt(f5,text='Save',bd=0,font=('SF Pro Display',15),bg='#000000',fg='#FFFFFF',activebackground='#000000',command=profile_save)
                    b18.place(relx=0.95,rely=0.1,anchor='center') 
                    b19=bt(f5,text='Cancel',bd=0,font=('sf pro display',15),bg='#000000',fg='#FFFFFF',activebackground='#000000',command=sprofile)  
                    b19.place(relx=0.85,rely=0.1,anchor='center')
                b17=bt(f5,image=p28,bd=0,bg='#000000',activebackground='#000000',command=profile_edit)  
                b17.place(relx=0.95,rely=0.09,anchor='center')    

    def marks(): ##########################################################   COMPLETE   ##################################################
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
                l61=lb(f10,text=rec1[1],bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') #mid sem 1
                l61.place(relx=0.53,rely=0.315,anchor='center')
                l62=lb(f10,text=(rec1[1]+'%'),bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
                l62.place(relx=0.82,rely=0.315,anchor='center')
            else:
                l77=lb(f10,text='N/A',bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') #mid sem 1
                l77.place(relx=0.53,rely=0.315,anchor='center')
                l78=lb(f10,text='N/A',bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
                l78.place(relx=0.82,rely=0.315,anchor='center')

            if rec1[2]!='NULL':
                l63=lb(f10,text=rec1[2],bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') #sem final 1 
                l63.place(relx=0.53,rely=0.375,anchor='center')
                l64=lb(f10,text=(rec1[2]+'%'),bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
                l64.place(relx=0.82,rely=0.375,anchor='center')
            else:
                l79=lb(f10,text='N/A',bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') #sem final 1 
                l79.place(relx=0.53,rely=0.375,anchor='center')
                l80=lb(f10,text='N/A',bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
                l80.place(relx=0.82,rely=0.375,anchor='center')
            
            if rec1[3]!='NULL':
                l65=lb(f10,text=rec1[3],bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') #midsem 2
                l65.place(relx=0.53,rely=0.465,anchor='center')
                l66=lb(f10,text=(rec1[3]+'%'),bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
                l66.place(relx=0.82,rely=0.465,anchor='center')
            else:
                l65=lb(f10,text='N/A',bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') #midsem 2
                l65.place(relx=0.53,rely=0.465,anchor='center')
                l66=lb(f10,text=('N/A'),bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
                l66.place(relx=0.82,rely=0.465,anchor='center')
        
            if rec1[4]!='NULL':
                l67=lb(f10,text=rec1[4],bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') #final 2
                l67.place(relx=0.53,rely=0.525,anchor='center')
                l68=lb(f10,text=(rec1[4]+'%'),bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
                l68.place(relx=0.82,rely=0.525,anchor='center')
            else:
                l67=lb(f10,text=('N/A'),bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') #final 2
                l67.place(relx=0.53,rely=0.525,anchor='center')
                l68=lb(f10,text=('N/A'),bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
                l68.place(relx=0.82,rely=0.525,anchor='center')      
            
            if rec1[5]!='NULL':
                l69=lb(f10,text=rec1[5],bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') #midsem 3
                l69.place(relx=0.53,rely=0.615,anchor='center')
                l70=lb(f10,text=(rec1[5]+'%'),bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
                l70.place(relx=0.82,rely=0.615,anchor='center')
            else:
                l69=lb(f10,text=('N/A'),bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') #midsem 3
                l69.place(relx=0.53,rely=0.615,anchor='center')
                l70=lb(f10,text=('N/A'),bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
                l70.place(relx=0.82,rely=0.615,anchor='center')

            if rec1[6]!='NULL':    
                l71=lb(f10,text=rec1[6],bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') #final 3 
                l71.place(relx=0.53,rely=0.675,anchor='center')
                l72=lb(f10,text=(rec1[6]+'%'),bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
                l72.place(relx=0.82,rely=0.675,anchor='center')
            else:
                l71=lb(f10,text='N/A',bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') #final 3 
                l71.place(relx=0.53,rely=0.675,anchor='center')
                l72=lb(f10,text='N/A',bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
                l72.place(relx=0.82,rely=0.675,anchor='center')

            if rec1[7]!='NULL':
                l73=lb(f10,text=rec1[7],bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') #midsem 4
                l73.place(relx=0.53,rely=0.765,anchor='center')
                l74=lb(f10,text=(rec1[7]+'%'),bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
                l74.place(relx=0.82,rely=0.765,anchor='center')
            else:
                l73=lb(f10,text='N/A',bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') #midsem 4
                l73.place(relx=0.53,rely=0.765,anchor='center')
                l74=lb(f10,text='N/A',bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
                l74.place(relx=0.82,rely=0.765,anchor='center')

            if rec1[8]!='NULL':
                l75=lb(f10,text=rec1[8],bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') #final 4
                l75.place(relx=0.53,rely=0.825,anchor='center')
                l76=lb(f10,text=(rec1[8]+'%'),bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF')
                l76.place(relx=0.82,rely=0.825,anchor='center')
            else:
                l75=lb(f10,text='N/A',bd=0,font=('SF Pro Display',15),bg='#232323',fg='#FFFFFF') #final 4
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
                e1=ent(f10,bd=0,font=('SF Pro Display',15),width=3)
                e1.place(relx=0.53,rely=0.315,anchor='center')
                e1.insert(0,rec2[1])

                e2=ent(f10,bd=0,font=('SF Pro Display',15),width=3)
                e2.place(relx=0.53,rely=0.375,anchor='center')
                e2.insert(0,rec2[2]) 

                e3=ent(f10,bd=0,font=('SF Pro Display',15),width=3)
                e3.place(relx=0.53,rely=0.465,anchor='center')
                e3.insert(0,rec2[3])

                e4=ent(f10,bd=0,font=('SF Pro Display',15),width=3)
                e4.place(relx=0.53,rely=0.525,anchor='center')
                e4.insert(0,rec2[4])

                e5=ent(f10,bd=0,font=('SF Pro Display',15),width=3)
                e5.place(relx=0.53,rely=0.615,anchor='center')
                e5.insert(0,rec2[5])

                e6=ent(f10,bd=0,font=('SF Pro Display',15),width=3)
                e6.place(relx=0.53,rely=0.675,anchor='center')
                e6.insert(0,rec2[6])

                e7=ent(f10,bd=0,font=('SF Pro Display',15),width=3)
                e7.place(relx=0.53,rely=0.765,anchor='center')
                e7.insert(0,rec2[7])

                e8=ent(f10,bd=0,font=('SF Pro Display',15),width=3)
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
                            
                b34=bt(f10,text='Save',bd=0,font=('SF Pro Display',15),bg='#000000',fg='#FFFFFF',activebackground='#000000',command=marks_save)
                b34.place(relx=0.95,rely=0.0875,anchor='center') 
                b35=bt(f10,text='Cancel',bd=0,font=('sf pro display',15),bg='#000000',fg='#FFFFFF',activebackground='#000000',command=marks)  
                b35.place(relx=0.85,rely=0.0875,anchor='center')
            b33=bt(f10,image=p28,bd=0,bg='#000000',activebackground='#000000',command=marks_edit)  
            b33.place(relx=0.95,rely=0.09,anchor='center')

    def fee_details():
        dbcur.execute('select sid from fee')
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
            l81=lb(f11,text='Fee details',font=('SF Pro Display',38,'bold'),bd=0,bg='#000000', fg='#FFFFFF')#isse dekhliyo iska variabke aadha hai 
            l81.place(relx=0,rely=0.05,anchor='w')#ise bhi
            l82=lb(f11,image=p29,bd=0)# ise bhi
            l82.place(relx=0.5,rely=0.55,anchor='center')# aur ise bhi
            def fee_edit():
                print('ruk')
                b36.place_forget()
                def fee_save():
                    print('wait more')
                b37=bt(f11,text='Save',bd=0,font=('SF Pro Display',15),bg='#000000',fg='#FFFFFF',activebackground='#000000',command=fee_save)
                b37.place(relx=0.95,rely=0.0875,anchor='center') 
                b38=bt(f11,text='Cancel',bd=0,font=('sf pro display',15),bg='#000000',fg='#FFFFFF',activebackground='#000000',command=fee_details)  
                b38.place(relx=0.85,rely=0.0875,anchor='center')
            b36=bt(f11,image=p28,bd=0,bg='#000000',activebackground='#000000',command=fee_edit)  
            b36.place(relx=0.95,rely=0.09,anchor='center')




    def events():
        print('under development')
        f4.place_forget()
        f11=fr(f2,height=500,width=855,bd=0,bg='#000000') 
        f11.place(relx=0.5,rely=0.535,anchor='center')
        l=lb(f11,text='Events',font=('SF Pro Display',38,'bold'),bd=0,bg='#000000', fg='#FFFFFF')#isse dekhliyo iska variabke aadha hai 
        l.place(relx=0,rely=0.05,anchor='w')#ise bhi
        l=lb(f11,image=p29,bd=0)# ise bhi
        l.place(relx=0.5,rely=0.55,anchor='center')# aur ise bhi
        def events_edit():
            print('ruk')
            b36.place_forget()
            def events_save():
                print('wait more')
            b37=bt(f11,text='Save',bd=0,font=('SF Pro Display',15),bg='#000000',fg='#FFFFFF',activebackground='#000000',command=events_save)
            b37.place(relx=0.95,rely=0.0875,anchor='center') 
            b38=bt(f11,text='Cancel',bd=0,font=('sf pro display',15),bg='#000000',fg='#FFFFFF',activebackground='#000000',command=events)  
            b38.place(relx=0.85,rely=0.0875,anchor='center')
        b36=bt(f11,image=p28,bd=0,bg='#000000',activebackground='#000000',command=events_edit)  
        b36.place(relx=0.95,rely=0.09,anchor='center')




    def attendance():
        print('under development')
        f4.place_forget()
        f11=fr(f2,height=500,width=855,bd=0,bg='#000000') 
        f11.place(relx=0.5,rely=0.535,anchor='center')
        l=lb(f11,text='Attendance',font=('SF Pro Display',38,'bold'),bd=0,bg='#000000', fg='#FFFFFF')#isse dekhliyo iska variabke aadha hai 
        l.place(relx=0,rely=0.05,anchor='w')#ise bhi
        l=lb(f11,image=p29,bd=0)# ise bhi
        l.place(relx=0.5,rely=0.55,anchor='center')# aur ise bhi
        def attendance_edit():
            print('ruk')
            b36.place_forget()
            def attendance_save():
                print('wait more')
            b37=bt(f11,text='Save',bd=0,font=('SF Pro Display',15),bg='#000000',fg='#FFFFFF',activebackground='#000000',command=attendance_save)
            b37.place(relx=0.95,rely=0.0875,anchor='center') 
            b38=bt(f11,text='Cancel',bd=0,font=('sf pro display',15),bg='#000000',fg='#FFFFFF',activebackground='#000000',command=attendance)  
            b38.place(relx=0.85,rely=0.0875,anchor='center')
        b36=bt(f11,image=p28,bd=0,bg='#000000',activebackground='#000000',command=attendance_edit)  
        b36.place(relx=0.95,rely=0.09,anchor='center')




    def projects():
        print('under development')
        f4.place_forget()
        f11=fr(f2,height=500,width=855,bd=0,bg='#000000') 
        f11.place(relx=0.5,rely=0.535,anchor='center')
        l=lb(f11,text='Projects',font=('SF Pro Display',38,'bold'),bd=0,bg='#000000', fg='#FFFFFF')#isse dekhliyo iska variabke aadha hai 
        l.place(relx=0,rely=0.05,anchor='w')#ise bhi
        l=lb(f11,image=p29,bd=0)# ise bhi
        l.place(relx=0.5,rely=0.55,anchor='center')# aur ise bhi
        def projects_edit():
            print('ruk')
            b36.place_forget()
            def projects_save():
                print('wait more')
            b37=bt(f11,text='Save',bd=0,font=('SF Pro Display',15),bg='#000000',fg='#FFFFFF',activebackground='#000000',command=projects_save)
            b37.place(relx=0.95,rely=0.0875,anchor='center') 
            b38=bt(f11,text='Cancel',bd=0,font=('sf pro display',15),bg='#000000',fg='#FFFFFF',activebackground='#000000',command=projects)  
            b38.place(relx=0.85,rely=0.0875,anchor='center')
        b36=bt(f11,image=p28,bd=0,bg='#000000',activebackground='#000000',command=projects_edit)  
        b36.place(relx=0.95,rely=0.09,anchor='center')




    def assignments():        
        print('under development')
        f4.place_forget()
        f11=fr(f2,height=500,width=855,bd=0,bg='#000000') 
        f11.place(relx=0.5,rely=0.535,anchor='center')
        l=lb(f11,text='Assignments',font=('SF Pro Display',38,'bold'),bd=0,bg='#000000', fg='#FFFFFF')#isse dekhliyo iska variabke aadha hai 
        l.place(relx=0,rely=0.05,anchor='w')#ise bhi
        l=lb(f11,image=p29,bd=0)# ise bhi
        l.place(relx=0.5,rely=0.55,anchor='center')# aur ise bhi
        def assignment_edit():
            print('ruk')
            b36.place_forget()
            def assignment_save():
                print('wait more')
            b37=bt(f11,text='Save',bd=0,font=('SF Pro Display',15),bg='#000000',fg='#FFFFFF',activebackground='#000000',command=assignment_save)
            b37.place(relx=0.95,rely=0.0875,anchor='center') 
            b38=bt(f11,text='Cancel',bd=0,font=('sf pro display',15),bg='#000000',fg='#FFFFFF',activebackground='#000000',command=assignments)  
            b38.place(relx=0.85,rely=0.0875,anchor='center')
        b36=bt(f11,image=p28,bd=0,bg='#000000',activebackground='#000000',command=assignment_edit)  
        b36.place(relx=0.95,rely=0.09,anchor='center')



        
    def about():####################################################################    COMPLETE    ###############################################
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
                        #dbcon.commit()
                        about()
                    except:
                        msgb.showinfo('Unexpected error','Please check the entry and try again.')
            b21=bt(f6,text='Save',bd=0,font=('SF Pro Display',15),bg='#000000',fg='#FFFFFF',activebackground='#000000',command=abt_save)
            b21.place(relx=0.95,rely=0.0875,anchor='center') 
            b22=bt(f6,text='Cancel',bd=0,font=('sf pro display',15),bg='#000000',fg='#FFFFFF',activebackground='#000000',command=about)  
            b22.place(relx=0.85,rely=0.0875,anchor='center')                 
        b20=bt(f6,image=p28,bd=0,bg='#000000',activebackground='#000000',command=about_edit)  
        b20.place(relx=0.95,rely=0.09,anchor='center')        


        
        
        
        
    def login():######################################################################### COMPLETE #####################################################################
        b1.place_forget()

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
        
        global id
        id= ent(f1,bd = 0 ,font=('SF Pro Display',12)) 
        id.place(relx = 0.8,rely = 0.54,anchor = 'center')

        key = ent(f1,bd = 0  , show = '*' ,font=('SF Pro Display',12)) 
        key.place(relx = 0.8,rely = 0.6,anchor = 'center') 

        def verify():
            dbcur.execute('select id from adminlogin')
            global d8
            d8=dbcur.fetchall()  
            if id.get()=='' or key.get()=='' :
                msgb.showwarning('Invalid entry','   Please fill both fields.   ')
                key.delete(0,END)
                
            if (id.get(),) not in d8 and (id.get()!='' and key.get()!=''):#((id.get().startswith('Taiit')==False or len(id.get())<=5) 
                msgb.showwarning('Invalid entry','      Invalid ID      ')
                id.delete(0,END)
                key.delete(0,END)
                                        
            for i in d8:                                             
                if id.get()==i[0]:
                    dbcur.execute('select pass from adminlogin where id="{}"'.format(id.get()))
                    d9=dbcur.fetchall()          
                    if key.get()==d9[0][0]:
                        home() 
                    elif key.get()!=d9[0][0] and key.get()!='' :
                        #id.delete()
                        #key.delete()
                        msgb.showwarning('Invalid entry','There was an error, Incorrect ID and Password combination.')
                        key.delete(0,END)         
                            
            
        b3=bt(f1,image=p7,bd = 0, bg='#232323',
        activebackground='#232323',command=verify)
        b3.place(relx = 0.85,rely=0.69,anchor='center')

        b4=bt(f1,text= 'Forgot your Password ?',font = ('SF Pro Display',10,UNDERLINE),
        bd = 0,bg = '#232323',fg='#737373',activebackground = '#232323',command=forgpass)
        b4.place(relx=0.83,rely=0.643,anchor='center')

        b5=bt(f1,image=p8,bd=0,bg='#000000',activebackground='#000000',command=main)
        b5.place(relx=0.03,rely=0.05,anchor='center')
    
    def main():####################################################################  COMPLETE  ########################################################################
        #main window
        global f1
        f1=fr(win,height=650,width=1150,bd=0 ,bg='#000000')
        f1.place(relx=0.5,rely=0.5,anchor = 'center')
        
        #universitrely logo
        
        l=lb(f1,image=p1,bd=0,bg = '#000000')
        l.place(relx=0.25,rely=0.5,anchor='center')
        
        #sign in prompt
        l1=lb(f1,text='Please Sign In.',bg = '#000000',fg = '#FFFFFF',font = ('SF Pro Display',38,'bold'))
        l1.place(relx=0.75,rely=0.35,anchor='center')

        #login button 1
        
        global b1
        b1=bt(f1,image = p2,bd = 0,bg = '#000000', activebackground = '#000000',command =home)
        b1.place(relx=0.75,rely=0.55,anchor='center')


        def sbutton():                         
            def switch(a):
                b1.configure(image=p3)
                b1.image=p3
            def reverse(a):
                b1.configure(image=p2)
                b1.image=p2
                
            b1.bind('<Enter>',switch)
            b1.bind('<Leave>',reverse)
        sbutton()               
                
            
        # division bar    
        
        l2=lb(f1,image = p6,bd = 0,bg = "#000000")
        l2.place(relx = 0.5 , rely = 0.55 , anchor = 'center')

        win.mainloop()

    try:   # step 1 where it starts
        dbcon=db.connect(host='localhost',user='root',password='mysql',database='proj_vidul')
        if dbcon.is_connected()==True:
            dbcur=dbcon.cursor()
    except:
        msgb.showwarning(
            'Database Error','There was some problem with the associated database, Please try again later')
    else:
        main()
except:
    msgb.showwarning('Unexpected error',"There was an unexpected error, we're trying to solve it. Please close the app and start it again.")
  




























































