from tkinter import * 
import time
win=Tk()
win.geometry('800x550')
win.configure(bg="#FFFFFF")
wn=win.title('Gyan Bharati School management system ')
#l1=tki.Label(win,text='The new IPhone 12 Pro max',bg="#FFFFFF",font=("SF Pro Display",38))
#l2=tki.Label(win,text='All for one,one for all.',bg="#FFFFFF",font=("SF Pro Display",38))
#l1.grid(column=0,row=0)
#l2.grid(column=0,row=25)
def l_d():
    #l1.configure(text='clicked')
    win.configure(bg='#000000')
    bt.configure(image=pic2,bd=0,bg="#000000",activebackground="#000000")
    #bt.grid(column=1,row=0)
    #bt.pack(side="bottom")
    l.configure(fg='#FFFFFF',bg='#000000')
    bt.configure(command=d_l)
    #l.grid(column=5,row=4)
def d_l():
    win.configure(bg='#FFFFFF')
    bt.configure(image=pic,bd=0,bg='#FFFFFF',activebackground='#FFFFFF')
    l.configure(fg='#000000',bg='#FFFFFF')
    bt.configure(command=l_d)
    
pic=PhotoImage( file = "swoff.png")
pic2=PhotoImage( file = "swon.png")
bt=Button(win,bd=0,bg="#FFFFFF",activebackground="#FFFFFF",image=pic,command=l_d)
bt.grid(column=1,row=0)
#bt.pack(side="bottom")
l=Label(win,text='Dark mode',bg='#FFFFFF',fg='#000000',font=('SF Pro Display',9))
l.grid(column=0,row=0)
        
a=input("press any key to close : ")

    

