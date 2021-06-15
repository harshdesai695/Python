from tkinter import *
import math as m
win=Tk()
win.title("Calculator")
win.geometry("280x410")

#variable
exp=""

def PRESS(x,equation):
    global exp
    exp=exp+str(x)
    equation.set(exp)
    
def evaluate(equation):
    global exp
    try:
        result = str(eval(exp))
        equation.set(result)
        exp = ""
    except:
        exp = ""

def cancle(equation):
    global exp
    exp=""
    equation.set(exp)

def fact(equation):
    global exp
    result = str(m.factorial(int(exp)))
    equation.set(result)
    exp=""

def square(x,equation):
    global exp
    if x==1:
        result = str(m.pow(int(exp),2))
        equation.set(result)
    elif x==2:
        result = str(m.pow(int(exp),1/2))
        equation.set(result)  
    exp=""

def log(equation):
    global exp
    result = str(m.log10(int(exp)))
    equation.set(result)
    exp=""
    
    
def main():
    equation=StringVar()
    e1=Entry(win,textvariable=equation,font=("Calibri",50),justify='right').place(x=5,y=5,width=270,height=100)
    b1=Button(win,text='1',padx=10,pady=10,activeforeground="red",command=lambda:PRESS(1,equation)).place(x=10,y=110,width=50,height=50)
    b2=Button(win,text='2',padx=10,pady=10,activeforeground="red",command=lambda:PRESS(2,equation)).place(x=60,y=110,width=50,height=50)
    b3=Button(win,text='3',padx=10,pady=10,activeforeground="red",command=lambda:PRESS(3,equation)).place(x=110,y=110,width=50,height=50)
    b4=Button(win,text='4',padx=10,pady=10,activeforeground="red",command=lambda:PRESS(4,equation)).place(x=10,y=170,width=50,height=50)
    b5=Button(win,text='5',padx=10,pady=10,activeforeground="red",command=lambda:PRESS(5,equation)).place(x=60,y=170,width=50,height=50)
    b6=Button(win,text='6',padx=10,pady=10,activeforeground="red",command=lambda:PRESS(6,equation)).place(x=110,y=170,width=50,height=50)
    b7=Button(win,text='7',padx=10,pady=10,activeforeground="red",command=lambda:PRESS(7,equation)).place(x=10,y=230,width=50,height=50)
    b8=Button(win,text='8',padx=10,pady=10,activeforeground="red",command=lambda:PRESS(8,equation)).place(x=60,y=230,width=50,height=50)
    b9=Button(win,text='9',padx=10,pady=10,activeforeground="red",command=lambda:PRESS(9,equation)).place(x=110,y=230,width=50,height=50)
    b0=Button(win,text='0',padx=10,pady=10,activeforeground="red",command=lambda:PRESS(0,equation)).place(x=10,y=290,width=100,height=50)
    bpoint=Button(win,text='.',padx=10,pady=10,activeforeground="red",command=lambda:PRESS('.',equation)).place(x=110,y=290,width=50,height=50)
    bplus=Button(win,text='+',padx=10,pady=10,activeforeground="red",command=lambda:PRESS('+',equation)).place(x=160,y=110,width=50,height=50)
    bminus=Button(win,text='-',padx=10,pady=10,activeforeground="red",command=lambda:PRESS('-',equation)).place(x=160,y=170,width=50,height=50)
    bdiv=Button(win,text='/',padx=10,pady=10,activeforeground="red",command=lambda:PRESS('/',equation)).place(x=160,y=230,width=50,height=50)
    bmulti=Button(win,text='X',padx=10,pady=10,activeforeground="red",command=lambda:PRESS('*',equation)).place(x=160,y=290,width=50,height=50)
    bequal=Button(win,text='=',padx=10,pady=10,activeforeground="red",command=lambda:evaluate(equation)).place(x=10,y=350,width=200,height=50)
    bcancle=Button(win,text='C',padx=10,pady=10,activeforeground="red",command=lambda:cancle(equation)).place(x=210,y=110,width=50,height=50)
    bfact=Button(win,text='!',padx=10,pady=10,activeforeground="red",command=lambda:fact(equation)).place(x=210,y=170,width=50,height=50)
    bpower=Button(win,text='^2',padx=10,pady=10,activeforeground="red",command=lambda:square(1,equation)).place(x=210,y=230,width=50,height=50)
    blog=Button(win,text='log10(x)',padx=10,pady=10,activeforeground="red",command=lambda:log(equation)).place(x=210,y=290,width=50,height=50)
    broot=Button(win,text='√',padx=10,pady=10,activeforeground="red",command=lambda:square(2,equation)).place(x=210,y=350,width=50,height=50)
    win.mainloop()
    

if __name__=='__main__':
    main()
    
