from tkinter import *
from PIL import ImageTk,Image 
ph=Image.open
root=Tk()
root.geometry('500x500')
root.configure(bg='#000000')

p3=PhotoImage(file = 'images/assignments2.png')
b=Button(root,image=p3,bd=0,bg='#000000')
b.place(relx=0.5,rely=0.5,anchor='center')   

def ZOOM(img):
    path=img.cget('file')
    image=Image.open(path)    
    image1=ImageTk.PhotoImage(image)
    width=round(image1.width()+(0.025*image1.width()))
    height=round(image1.height()+(0.025*image1.height()))
    zoom_image=image.resize((width,height),Image.ANTIALIAS)
    new_image=ImageTk.PhotoImage(zoom_image)
    return new_image
def ANIMATE(img):
    def zoom(i):
        image=ZOOM(img)
        b.configure(image=image)
        b.image=image
    def reverse(i):
        b.configure(image=img)
        b.image=img
    b.bind('<Enter>',zoom)
    b.bind('<Leave>',reverse)
ANIMATE(p3)
root.mainloop()


