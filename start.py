def init():
    import tkinter as tk
    import sys
    import time as t
    win1=tk.Tk()
    wid=int(((win1.winfo_screenwidth()*0.9875)//2)-240)
    hgt=int(((win1.winfo_screenheight()*0.95)//2)-135)
    win1.geometry('480x270+{}+{}'.format(wid,hgt))
    win1.configure(bg='#000000')
    win1.overrideredirect(True)
    frame=tk.Frame(win1,width=480,height=270,bd=0,bg='#000000')
    frame.place(relx=0.5,rely=0.5,anchor='center')
    e1=tk.PhotoImage(file='images/start.png')
    q=tk.Label(frame,bd=0,image=e1)
    q.place(relx=0.5,rely=0.5,anchor='center')
    def load():
        w=tk.Label(frame,text='Loading...',font=('SF Pro Display',13),bd=0,bg='#000000',fg='#737373')
        w.place(relx=0.5,rely=0.75,anchor='center')
    def close():
       win1.destroy()
    win1.after(2000,load)
    win1.after(5000,close)
    win1.mainloop()
init()

