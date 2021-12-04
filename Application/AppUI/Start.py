#██╗░░░██╗███████╗██████╗░░██████╗██╗░█████╗░███╗░░██╗  ░░███╗░░░░░███████╗
#██║░░░██║██╔════╝██╔══██╗██╔════╝██║██╔══██╗████╗░██║  ░████║░░░░░██╔════╝
#╚██╗░██╔╝█████╗░░██████╔╝╚█████╗░██║██║░░██║██╔██╗██║  ██╔██║░░░░░██████╗░
#░╚████╔╝░██╔══╝░░██╔══██╗░╚═══██╗██║██║░░██║██║╚████║  ╚═╝██║░░░░░╚════██╗
#░░╚██╔╝░░███████╗██║░░██║██████╔╝██║╚█████╔╝██║░╚███║  ███████╗██╗██████╔╝
#░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝░╚════╝░╚═╝░░╚══╝  ╚══════╝╚═╝╚═════╝░

# 𝙱𝚄𝙸𝙻𝙳 𝚟𝟷.𝟻.𝟸
# ©️ 𝚅𝚒𝚍𝚞𝚕 𝙲𝚑𝚊𝚞𝚑𝚊𝚗 2021 

import ctypes  # included library with Python install.
import ErrorLogger as elog

def Mbox(title, text, style=0):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

try: 
    import tkinter as tk
    import time as t
    win1 = tk.Tk()
    wid = int(((win1.winfo_screenwidth()*0.9875)//2)-240)
    hgt = int(((win1.winfo_screenheight()*0.95)//2)-135)
    win1.geometry('480x270+{}+{}'.format(wid, hgt))
    win1.configure(bg='#000000')
    win1.overrideredirect(True)
    frame = tk.Frame(win1, width=480, height=270, bd=0, bg='#000000')
    frame.place(relx=0.5, rely=0.5, anchor='center')
    e1 = tk.PhotoImage(file='Resources/App/AppUI Resources/Images/start.png')
    q = tk.Label(frame, bd=0, image=e1)
    q.place(relx=0.5, rely=0.5, anchor='center')

    def load():
        w = tk.Label(frame, text='Loading', font=(
            'SF Pro Display', 13,"bold"), bd=0, bg='#000000', fg='#737373')
        w.place(relx=0.5, rely=0.75, anchor='center')

    def dot1():
        global w1
        w1 = tk.Label(frame, text='.', font=('SF Pro Display', 13),
                        bd=0, bg='#000000', fg='#737373')
        w1.place(relx=0.57, rely=0.75, anchor='center')

    def dot2():
        global w2
        w2 = tk.Label(frame, text='.', font=('SF Pro Display', 13),
                        bd=0, bg='#000000', fg='#737373')
        w2.place(relx=0.59, rely=0.75, anchor='center')

    def dot3():
        global w3
        w3 = tk.Label(frame, text='.', font=('SF Pro Display', 13),
                        bd=0, bg='#000000', fg='#737373')
        w3.place(relx=0.61, rely=0.75, anchor='center')

    def wipe():
        w1.place_forget()
        w2.place_forget()
        w3.place_forget()

    def close():
        win1.destroy()

    win1.after(1100, load)
    win1.after(1500, dot1)
    win1.after(1900, dot2)
    win1.after(2300, dot3)
    win1.after(2700, wipe)
    win1.after(3100, dot1)
    win1.after(3500, dot2)
    elog.createLog('Successful startup','The app started successfully and has proceeded to run the Main UI.')

    win1.after(3900, close)

    win1.mainloop()
except:
    Mbox("Runtime Error",'There was an issue during the startup of the App. Please Try Again later while we fix this.')
    elog.createLog('Start Screen Error','The Start Screen Didnt appear and error message prompted after which program unexpectedly stopped.')
