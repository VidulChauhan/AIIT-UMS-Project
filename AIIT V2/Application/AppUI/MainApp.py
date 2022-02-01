#import MainStart
from datetime import *
from tkinter import *
import ctypes
from tkinter.font import BOLD  # included library with Python install.


def Mbox(title, text, style=0):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


ph = PhotoImage
lb = Label
bt = Button
fr = Frame
ent = Entry
tx = Text
msg = Message
cv = Canvas
dt = datetime
day = dt.now().strftime('%A')
month = dt.now().strftime('%B')
DD = str(dt.now().day)
YY = str(dt.now().year)
DATE = day+', '+DD+' '+month+' '+YY
curtime = dt.now().time()

##############  MAIN WINDOW   ##############
mainbg = '#FFFFFF'
mainfg = '#000000'
sidebarbglight = '#CEECFF'
sidebarbgdark ='#292929'
main_window = Tk()
width = int(((main_window.winfo_screenwidth()*0.9875)//2)-575)
height = int(((main_window.winfo_screenheight()*0.95)//2)-325)
main_window.geometry('1150x650+{}+{}'.format(width, height))
main_window.title('MARK II')
main_window.configure(bg=mainbg)
main_window.minsize(1150,650)


settingicon = ph(
    file='Resources/App/AppUI Resources/SystemUI/settingslightmode.png')


####   MENU SIDEBAR   ####
mainBar = Frame(main_window, bd=0, width=325, bg=sidebarbglight)
mainBar.place(relx=0, rely=0.5, anchor='w', relheight=1)

mainView = Frame(main_window, bd=0, bg=mainbg)
mainView.place(x=325, rely=0, anchor='nw', relwidth=1, relheight=1)


def settings():
    setting_layer1 = Frame(mainView, bd=0, bg='#FFFFFF')
    setting_layer1.place(relx=0, rely=0, anchor='nw', relwidth=1, relheight=1)

    setting_l1 = Label(setting_layer1, bd=0, font=('consolas', 32, 'bold'), fg='#000000',
                       bg='#FFFFFF', text='Settings')
    setting_l1.place(relx=0.02, rely=0.015, anchor='nw')


setting_button = Button(mainBar, image=settingicon,
                        bd=0, bg='#FFFFFF', activebackground='#FFFFFF', command=settings)
#setting_button.place(relx=0.02, rely=0.99, anchor='sw')


main_window.mainloop()
