

import numpy as np
import math as m
import cmath as cm
import matplotlib.pyplot as plt
from tkinter import *

def func3():
    
    fitg=float(fitgra.get())
    fitm=float(fitmin.get())
    fits=float(fitseg.get())
    landag=float(landagra.get())
    landam=float(landamin.get())
    landas=float(landaseg.get())
    h1=float(h.get())
    a1=float(a.get())
    b1=float(b.get())
    
    
    e2=(a1**2-b1**2)/(a1**2) #e^2
    ep2=(a1**2-b1**2)/(b1**2) #e'^2
    
    
    term1=fits/60
    term2=fitm+term1
    s=term2/60
    fit1=fitg+s
    
    ter1=landas/60
    ter2=landam+ter1
    s1=ter2/60
    landat1=landag+s1
    
    N1=((a1)/(m.sqrt(1-e2*(m.sinh((fit1*m.pi)/180)**2))))
    
    x1=(N1+h1)*m.cos((fit1*m.pi)/180)*m.cos((landat1*m.pi)/180)
    y1=(N1+h1)*m.cos((fit1*m.pi)/180)*m.sin((landat1*m.pi)/180)
    z1=(N1*(1-e2)+h1)*m.sin((fit1*m.pi)/180)
    
    x3.delete(0,"end")
    x3.insert(0,x1)
    y3.delete(0,"end")
    y3.insert(0,y1)
    z3.delete(0,"end")
    z3.insert(0,z1)
    N.delete(0,"end")
    N.insert(0,N1)
    a.delete(0,"end")
    a.insert(0,a1)
    b.delete(0,"end")
    b.insert(0,b1)
    c.delete(0,"end")
    c.insert(0,e2)


Ventana3 = Tk()
Ventana3.title("Problema directo de coordenadas rectangulares")
Ventana3.geometry("700x370")


la=Label(Ventana3, text="a", bg="gray")
la.place(x=450,y=10, width=50, height=30)
a=Entry(Ventana3, bg="white")
a.place(x=550,y=10, width=100, height=30)

lb=Label(Ventana3, text="b", bg="gray")
lb.place(x=450,y=50, width=50, height=30)
b=Entry(Ventana3, bg="white")
b.place(x=550,y=50, width=100, height=30)

lf=Label(Ventana3, text="f", bg="gray")
lf.place(x=450,y=90, width=50, height=30)
f=Entry(Ventana3, bg="white")
f.place(x=550,y=90, width=100, height=30)


lc=Label(Ventana3, text="e^2", bg="gray")
lc.place(x=450,y=130, width=50, height=30)
c=Entry(Ventana3, bg="white")
c.place(x=550,y=130, width=100, height=30)


lN=Label(Ventana3, text="N", bg="gray")
lN.place(x=450,y=170, width=50, height=30)
N=Entry(Ventana3, bg="white")
N.place(x=550,y=170, width=100, height=30)


Mx3=Label(Ventana3, text="x", bg="gray")
Mx3.place(x=10,y=10, width=50, height=30)
x3=Entry(Ventana3, bg="white")
x3.place(x=100,y=10, width=100, height=30)

My3=Label(Ventana3, text="Y", bg="gray")
My3.place(x=10,y=50, width=50, height=30)
y3=Entry(Ventana3, bg="white")
y3.place(x=100,y=50, width=100, height=30)

Mz3=Label(Ventana3, text="z", bg="gray")
Mz3.place(x=10,y=90, width=50, height=30)
z3=Entry(Ventana3, bg="white")
z3.place(x=100,y=90, width=100, height=30)

B31=Button(Ventana3, text="C.Meridianas", command=func3)
B31.place(x=250,y=30, width=100, height=30)



lh=Label(Ventana3, text="h", bg="gray")
lh.place(x=10,y=150, width=50, height=30)
h=Entry(Ventana3, bg="white")
h.place(x=100,y=150, width=100, height=30)

lgrados=Label(Ventana3, text="°", bg="gray")
lgrados.place(x=125,y=200, width=50, height=30)
lminutos=Label(Ventana3, text="'", bg="gray")
lminutos.place(x=245,y=200, width=50, height=30)
lsegundos=Label(Ventana3, text="''", bg="gray")
lsegundos.place(x=365,y=200, width=50, height=30)

fi3=Label(Ventana3, text="φ", bg="gray")
fi3.place(x=10,y=250, width=50, height=30)
fitgra=Entry(Ventana3, bg="white")
fitgra.place(x=100,y=250, width=100, height=30)
fitmin=Entry(Ventana3, bg="white")
fitmin.place(x=220,y=250, width=100, height=30)
fitseg=Entry(Ventana3, bg="white")
fitseg.place(x=340,y=250, width=100, height=30)

landa3=Label(Ventana3, text="λ", bg="gray")
landa3.place(x=10,y=300, width=50, height=30)
landagra=Entry(Ventana3, bg="white")
landagra.place(x=100,y=300, width=100, height=30)
landamin=Entry(Ventana3, bg="white")
landamin.place(x=220,y=300, width=100, height=30)
landaseg=Entry(Ventana3, bg="white")
landaseg.place(x=340,y=300, width=100, height=30)

Ventana3.mainloop()