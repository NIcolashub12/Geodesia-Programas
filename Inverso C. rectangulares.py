

import numpy as np
import math as m
import cmath as cm
import matplotlib.pyplot as plt
from tkinter import *



def func4(): # función para la Solución exacta
    x1=float(x4.get())
    y1=float(y4.get())
    z1=float(z4.get())
    a1=float(a.get())
    b1=float(b.get())
    
    e2=(a1**2-b1**2)/(a1**2)
    ep2=(a1**2-b1**2)/(b1**2)
    landat1= m.atan(y1/x1)
    ler=m.atan((z1*a1)/(b1*m.sqrt(x1**2+y1**2)))
    ter1=z1+ep2*b1*(m.sin(ler)**3)
    ter2=(m.sqrt(x1**2+y1**2))-e2*a1*(m.cos(ler)**3)
    fit1=m.atan(ter1/ter2)
    N1=(a1)/(m.sqrt(1-(e2*(m.sin(fit1)**2))))
    h1=m.sqrt(x1**2+y1**2)-N1
    
    parte_decimal, parte_entera = m.modf(m.degrees(landat1))
    gradoslanda=str(parte_entera)
    mul=60*(parte_decimal)
    parte_decimalm, parte_enteram = m.modf(mul)
    minutoslanda=str(parte_enteram)
    mul1=parte_decimalm*60
    parte_decimals, parte_enteras = m.modf(mul1)
    segundoslanda=str(parte_enteras)
    
    gradoslan1=gradoslanda+"°"+minutoslanda+"'"+segundoslanda+"''"
    
    
    parte_decimalf, parte_enteraf = m.modf(m.degrees(fit1))
    gradosfi=str(parte_enteraf)
    mulf=60*(parte_decimalf)
    parte_decimalmf, parte_enteramf = m.modf(mulf)
    minutosfi=str(parte_enteramf)
    mulf1=parte_decimalmf*60
    parte_decimalsf, parte_enterasf = m.modf(mulf1)
    segundosfi=str(parte_enterasf)
    
    gradosfi1=gradosfi+"°"+minutosfi+"'"+segundosfi+"''"
    
    
   
    a.delete(0,"end")
    a.insert(0,a1)
    b.delete(0,"end")
    b.insert(0,b1)
    c.delete(0,"end")
    c.insert(0,e2)
    N.delete(0,"end")
    N.insert(0,N1)
    h4.delete(0,"end")
    h4.insert(0,m.degrees(h1))
    fit4.delete(0,"end")
    fit4.insert(0,m.degrees(fit1))
    landat4.delete(0,"end")
    landat4.insert(0,m.degrees(landat1))
    gradoslan.delete(0,"end")
    gradoslan.insert(0,(gradoslan1))
    gradosphi.delete(0,"end")
    gradosphi.insert(0,(gradosfi1))
    
    
def func5():# función para la Solución iterada h
    x1=float(x4.get())
    y1=float(y4.get())
    z1=float(z4.get())
    a1=float(a.get())
    b1=float(b.get())
    
    
    e2=(a1**2-b1**2)/(a1**2)
    ep2=(a1**2-b1**2)/(b1**2)
    
    landat1= m.atan(y1/x1)
    
    ter1=((z1)/(m.sqrt(x1**2+y1**2)))
    ter2=(1+((e2)/(1-e2)))
    fit1 =m.atan(ter1*ter2)
    
    N1=(a1)/(m.sqrt(1-(e2*(m.sin(fit1)*(m.sin(fit1))))))
    
    term1=m.sqrt(x1**2+y1**2)
    term2=m.cos(fit1)
    h1=((term1)/(term2))-N1
    
    parte_decimal, parte_entera = m.modf(m.degrees(landat1))
    gradoslanda=str(parte_entera)
    mul=60*(parte_decimal)
    parte_decimalm, parte_enteram = m.modf(mul)
    minutoslanda=str(parte_enteram)
    mul1=parte_decimalm*60
    parte_decimals, parte_enteras = m.modf(mul1)
    segundoslanda=str(parte_enteras)
    
    gradoslan1=gradoslanda+"°"+minutoslanda+"'"+segundoslanda+"''"
    
    
    parte_decimalf, parte_enteraf = m.modf(m.degrees(fit1))
    gradosfi=str(parte_enteraf)
    mulf=60*(parte_decimalf)
    parte_decimalmf, parte_enteramf = m.modf(mulf)
    minutosfi=str(parte_enteramf)
    mulf1=parte_decimalmf*60
    parte_decimalsf, parte_enterasf = m.modf(mulf1)
    segundosfi=str(parte_enterasf)
    
    gradosfi1=gradosfi+"°"+minutosfi+"'"+segundosfi+"''"
    
    
    a.delete(0,"end")
    a.insert(0,a1)
    b.delete(0,"end")
    b.insert(0,b1)
    c.delete(0,"end")
    c.insert(0,e2)
    N.delete(0,"end")
    N.insert(0,N1)
    h4.delete(0,"end")
    h4.insert(0,m.degrees(h1))
    fit4.delete(0,"end")
    fit4.insert(0,m.degrees(fit1))
    landat4.delete(0,"end")
    landat4.insert(0,m.degrees(landat1))
    gradoslan.delete(0,"end")
    gradoslan.insert(0,(gradoslan1))
    gradosphi.delete(0,"end")
    gradosphi.insert(0,(gradosfi1))
    

def func6(): # función para la Solución iterada N
    x1=float(x4.get())
    y1=float(y4.get())
    z1=float(z4.get())
    a1=float(a.get())
    b1=float(b.get())
    

    e2=(a1**2-b1**2)/(a1**2)
    ep2=(a1**2-b1**2)/(b1**2)
    
    landat1= m.atan(y1/x1)
    
    term1=m.sqrt(x1**2+y1**2+z1**2)
    term2=m.sqrt(a1*b1)
    h0 =term1-term2
    
    N1=a1
    
    ter1=((z1)/(m.sqrt(x1**2+y1**2)))
    ter2=(1+((e2*N1)/(N1+h0)))
    fit1 =m.atan(ter1*ter2)
    
    parte_decimal, parte_entera = m.modf(m.degrees(landat1))
    gradoslanda=str(parte_entera)
    mul=60*(parte_decimal)
    parte_decimalm, parte_enteram = m.modf(mul)
    minutoslanda=str(parte_enteram)
    mul1=parte_decimalm*60
    parte_decimals, parte_enteras = m.modf(mul1)
    segundoslanda=str(parte_enteras)
    
    gradoslan1=gradoslanda+"°"+minutoslanda+"'"+segundoslanda+"''"
    
    
    parte_decimalf, parte_enteraf = m.modf(m.degrees(fit1))
    gradosfi=str(parte_enteraf)
    mulf=60*(parte_decimalf)
    parte_decimalmf, parte_enteramf = m.modf(mulf)
    minutosfi=str(parte_enteramf)
    mulf1=parte_decimalmf*60
    parte_decimalsf, parte_enterasf = m.modf(mulf1)
    segundosfi=str(parte_enterasf)
    
    gradosfi1=gradosfi+"°"+minutosfi+"'"+segundosfi+"''"
    
    
    a.delete(0,"end")
    a.insert(0,a1)
    b.delete(0,"end")
    b.insert(0,b1)
    c.delete(0,"end")
    c.insert(0,e2)
    N.delete(0,"end")
    N.insert(0,N1)
    h4.delete(0,"end")
    h4.insert(0,m.degrees(h0))
    fit4.delete(0,"end")
    fit4.insert(0,m.degrees(fit1))
    landat4.delete(0,"end")
    landat4.insert(0,m.degrees(landat1))
    gradoslan.delete(0,"end")
    gradoslan.insert(0,(gradoslan1))
    gradosphi.delete(0,"end")
    gradosphi.insert(0,(gradosfi1))
    
    
Ventana4 = Tk()
Ventana4.title("Problema inverso de coordenas rectangulares")
Ventana4.geometry("700x370")

la=Label(Ventana4, text="a", bg="gray")
la.place(x=410,y=10, width=50, height=30)
a=Entry(Ventana4, bg="white")
a.place(x=510,y=10, width=100, height=30)

lb=Label(Ventana4, text="b", bg="gray")
lb.place(x=410,y=50, width=50, height=30)
b=Entry(Ventana4, bg="white")
b.place(x=510,y=50, width=100, height=30)

lf=Label(Ventana4, text="f", bg="gray")
lf.place(x=410,y=90, width=50, height=30)
f=Entry(Ventana4, bg="white")
f.place(x=510,y=90, width=100, height=30)


lc=Label(Ventana4, text="e'", bg="gray")
lc.place(x=410,y=130, width=50, height=30)
c=Entry(Ventana4, bg="white")
c.place(x=510,y=130, width=100, height=30)


lN=Label(Ventana4, text="N", bg="gray")
lN.place(x=410,y=170, width=50, height=30)
N=Entry(Ventana4, bg="white")
N.place(x=510,y=170, width=100, height=30)


Mx4=Label(Ventana4, text="x", bg="gray")
Mx4.place(x=10,y=10, width=50, height=30)
x4=Entry(Ventana4, bg="white")
x4.place(x=100,y=10, width=100, height=30)

My4=Label(Ventana4, text="y", bg="gray")
My4.place(x=10,y=50, width=50, height=30)
y4=Entry(Ventana4, bg="white")
y4.place(x=100,y=50, width=100, height=30)

Mz4=Label(Ventana4, text="z", bg="gray")
Mz4.place(x=10,y=90, width=50, height=30)
z4=Entry(Ventana4, bg="white")
z4.place(x=100,y=90, width=100, height=30)

B41=Button(Ventana4, text="S.Exacta", command=func4)
B41.place(x=250,y=30, width=100, height=30)

B42=Button(Ventana4, text="S.Iterada h", command=func5)
B42.place(x=250,y=80, width=100, height=30)

B41=Button(Ventana4, text="S.Iterada N", command=func6)
B41.place(x=250,y=130, width=100, height=30)

lh4=Label(Ventana4, text="h", bg="gray")
lh4.place(x=10,y=200, width=50, height=30)
h4=Entry(Ventana4, bg="white")
h4.place(x=100,y=200, width=100, height=30)

fi4=Label(Ventana4, text="φ", bg="gray")
fi4.place(x=10,y=250, width=50, height=30)
fit4=Entry(Ventana4, bg="white")
fit4.place(x=100,y=250, width=100, height=30)

landa4=Label(Ventana4, text="λ", bg="gray")
landa4.place(x=10,y=300, width=50, height=30)
landat4=Entry(Ventana4, bg="white")
landat4.place(x=100,y=300, width=100, height=30)



gradosphi=Entry(Ventana4, bg="white")
gradosphi.place(x=220,y=250, width=150, height=30)


gradoslan=Entry(Ventana4, bg="white")
gradoslan.place(x=220,y=300, width=150, height=30)


Ventana4.mainloop()