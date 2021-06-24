import pyqrcode
import png
from pyqrcode import QRCode
import tkinter as tk
import os
from PIL import ImageTk,Image

win=tk.Tk()
win.title("QRcode Generater")
s=tk.StringVar()
S=tk.StringVar()

def generate():
    c=pyqrcode.create(s.get())
    c.png(s.get()+".png",scale=10)
    show()

def show():
    img=Image.open(s.get()+".png")
    img=ImageTk.PhotoImage(img)
    p=tk.Label(win,image=img)
    p.image=img
    p.pack()

tk.Label(win,text="ENTER THE LINK YOU WANT TO MAKE QRCODE  OF:").pack(side="top")
e=tk.Entry(win,textvariable=s).pack()
tk.Button(win,text="GENERATE",command=generate).pack()
win.mainloop()
