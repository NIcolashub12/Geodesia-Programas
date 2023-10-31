

import numpy as np
import math as m
import cmath as cm
import matplotlib.pyplot as plt
from tkinter import *



def meridiana1():
    x1=float(x.get())
    z1=float(z.get())
    a1=float(a.get())
    b1=float(b.get())
    
    
    e2=(a1**2-b1**2)/(a1**2) #e^2
    ep2=(a1**2-b1**2)/(b1**2) #e'^2
    
    #c1=float(c.get())
    #e=c1/a1
    rg=m.sqrt(x1**2+z1**2)
    
    var=m.degrees(m.acos(x1/rg))
    var1=m.degrees(m.acos(x1/a1))
    v=m.atan((a1**2/b1**2)*(z1/x1))
    var2=m.degrees(v)
    N1=(a1/(m.sqrt(1-e2*(m.sinh(v)**2))))
    
    print(var)
    print(var1)
    print(var2)
    
    parte_decimal, parte_entera = m.modf(var2)
    gradoslanda=str(parte_entera)
    mul=60*(parte_decimal)
    parte_decimalm, parte_enteram = m.modf(mul)
    minutoslanda=str(parte_enteram)
    mul1=parte_decimalm*60
    parte_decimals, parte_enteras = m.modf(mul1)
    segundoslanda=str(parte_enteras)
    
    
    
    
    parte_decimalf, parte_enteraf = m.modf(var)
    gradosfi=str(parte_enteraf)
    mulf=60*(parte_decimalf)
    parte_decimalmf, parte_enteramf = m.modf(mulf)
    minutosfi=str(parte_enteramf)
    mulf1=parte_decimalmf*60
    parte_decimalsf, parte_enterasf = m.modf(mulf1)
    segundosfi=str(parte_enterasf)
    
    parte_decimalt, parte_enterat = m.modf(var1)
    gradost=str(parte_enterat)
    mult=60*(parte_decimalt)
    parte_decimalmt, parte_enteramt = m.modf(mult)
    minutost=str(parte_enteramt)
    mult1=parte_decimalmt*60
    parte_decimalst, parte_enterast = m.modf(mult1)
    segundost=str(parte_enterast)
    
    
    wgra.delete(0,"end")
    wgra.insert(0,gradosfi)
    wmin.delete(0,"end")
    wmin.insert(0,minutosfi)
    wseg.delete(0,"end")
    wseg.insert(0,segundosfi)
    tgra.delete(0,"end")
    tgra.insert(0,gradost)
    tmin.delete(0,"end")
    tmin.insert(0,minutost)
    tseg.delete(0,"end")
    tseg.insert(0,segundost)
    figra.delete(0,"end")
    figra.insert(0,gradoslanda)
    fimin.delete(0,"end")
    fimin.insert(0,minutoslanda)
    fiseg.delete(0,"end")
    fiseg.insert(0,segundoslanda)
    fidec.delete(0,"end")
    fidec.insert(0,var2)
    wdec.delete(0,"end")
    wdec.insert(0,var)
    tdec.delete(0,"end")
    tdec.insert(0,var1)
    a.delete(0,"end")
    a.insert(0,a1)
    b.delete(0,"end")
    b.insert(0,b1)
    c.delete(0,"end")
    c.insert(0,e2)
    N.delete(0,"end")
    N.insert(0,N1)
        
def meridianaome():
    
    wg=float(wgra.get())
    wm=float(wmin.get())
    ws=float(wseg.get())
    a1=float(a.get())
    b1=float(b.get())
    
    
    e2=(a1**2-b1**2)/(a1**2) #e^2
    ep2=(a1**2-b1**2)/(b1**2) #e'^2
    
    term1=ws/60
    term2=wm+term1
    s=term2/60
    omega1=wg+s
    
    fit1=m.atan((m.tan((omega1*m.pi)/180))/(1-(e2)**2))
    N1=(a1/(m.sqrt(1-e2*(m.sinh(fit1)**2))))
    fit1=m.degrees(fit1)
    
    
    parte_decimal, parte_entera = m.modf(fit1)
    gradoslanda=str(parte_entera)
    mul=60*(parte_decimal)
    parte_decimalm, parte_enteram = m.modf(mul)
    minutoslanda=str(parte_enteram)
    mul1=parte_decimalm*60
    parte_decimals, parte_enteras = m.modf(mul1)
    segundoslanda=str(parte_enteras)
    
    
    figra.delete(0,"end")
    figra.insert(0,gradoslanda)
    fimin.delete(0,"end")
    fimin.insert(0,minutoslanda)
    fiseg.delete(0,"end")
    fiseg.insert(0,segundoslanda)
    fidec.delete(0,"end")
    fidec.insert(0,fit1)
    a.delete(0,"end")
    a.insert(0,a1)
    b.delete(0,"end")
    b.insert(0,b1)
    c.delete(0,"end")
    c.insert(0,e2)
    N.delete(0,"end")
    N.insert(0,N1)
    
def meridianateta():
    
    tg=float(tgra.get())
    tm=float(tmin.get())
    ts=float(tseg.get())
    a1=float(a.get())
    b1=float(b.get())
    
    
    e2=(a1**2-b1**2)/(a1**2) #e^2
    ep2=(a1**2-b1**2)/(b1**2) #e'^2
    
    term1=ts/60
    term2=tm+term1
    s=term2/60
    teta1=tg+s

   
    fit1=m.atan((m.tan((teta1*m.pi)/180))/(m.sqrt((1-(e2)**2))))
    
    N1=(a1/(m.sqrt(1-e2*(m.sinh(fit1)**2))))
    fit1=m.degrees(fit1)
    
    parte_decimal, parte_entera = m.modf(fit1)
    gradoslanda=str(parte_entera)
    mul=60*(parte_decimal)
    parte_decimalm, parte_enteram = m.modf(mul)
    minutoslanda=str(parte_enteram)
    mul1=parte_decimalm*60
    parte_decimals, parte_enteras = m.modf(mul1)
    segundoslanda=str(parte_enteras)
    
    
    figra.delete(0,"end")
    figra.insert(0,gradoslanda)
    fimin.delete(0,"end")
    fimin.insert(0,minutoslanda)
    fiseg.delete(0,"end")
    fiseg.insert(0,segundoslanda)
    fidec.delete(0,"end")
    fidec.insert(0,fit1)
    a.delete(0,"end")
    a.insert(0,a1)
    b.delete(0,"end")
    b.insert(0,b1)
    c.delete(0,"end")
    c.insert(0,e2)
    N.delete(0,"end")
    N.insert(0,N1)
    
Ventana = Tk()
Ventana.title("Elipse Meridiana")
Ventana.geometry("700x470")

la=Label(Ventana, text="a", bg="gray")
la.place(x=450,y=10, width=50, height=30)
a=Entry(Ventana, bg="white")
a.place(x=550,y=10, width=100, height=30)

lb=Label(Ventana, text="b", bg="gray")
lb.place(x=450,y=50, width=50, height=30)
b=Entry(Ventana, bg="white")
b.place(x=550,y=50, width=100, height=30)

lf=Label(Ventana, text="f", bg="gray")
lf.place(x=450,y=90, width=50, height=30)
f=Entry(Ventana, bg="white")
f.place(x=550,y=90, width=100, height=30)


lc=Label(Ventana, text="e^2", bg="gray")
lc.place(x=450,y=130, width=50, height=30)
c=Entry(Ventana, bg="white")
c.place(x=550,y=130, width=100, height=30)


lN=Label(Ventana, text="N", bg="gray")
lN.place(x=450,y=170, width=50, height=30)
N=Entry(Ventana, bg="white")
N.place(x=550,y=170, width=100, height=30)


#Coordenadas Meridianas
Mx=Label(Ventana, text="x", bg="gray")
Mx.place(x=10,y=50, width=50, height=30)
x=Entry(Ventana, bg="white")
x.place(x=100,y=50, width=100, height=30)

Mz=Label(Ventana, text="z", bg="gray")
Mz.place(x=10,y=100, width=50, height=30)
z=Entry(Ventana, bg="white")
z.place(x=100,y=100, width=100, height=30)

B1=Button(Ventana, text="C.Meridianas", command=meridiana1)
B1.place(x=250,y=30, width=100, height=30)

B2=Button(Ventana, text="ω=f(φ)", command=meridianaome)
B2.place(x=250,y=80, width=100, height=30)

B3=Button(Ventana, text="θ=f(φ)", command=meridianateta)
B3.place(x=250,y=130, width=100, height=30)







lgrados=Label(Ventana, text="°", bg="gray")
lgrados.place(x=125,y=200, width=50, height=30)
lminutos=Label(Ventana, text="'", bg="gray")
lminutos.place(x=245,y=200, width=50, height=30)
lsegundos=Label(Ventana, text="''", bg="gray")
lsegundos.place(x=365,y=200, width=50, height=30)

Mre=Label(Ventana, text="ω", bg="gray")
Mre.place(x=10,y=250, width=50, height=30)
wgra=Entry(Ventana, bg="white")
wgra.place(x=100,y=250, width=100, height=30)
wmin=Entry(Ventana, bg="white")
wmin.place(x=220,y=250, width=100, height=30)
wseg=Entry(Ventana, bg="white")
wseg.place(x=340,y=250, width=100, height=30)
wdec=Entry(Ventana, bg="white")
wdec.place(x=460,y=250, width=100, height=30)

Mre1=Label(Ventana, text="θ", bg="gray")
Mre1.place(x=10,y=300, width=50, height=30)
tgra=Entry(Ventana, bg="white")
tgra.place(x=100,y=300, width=100, height=30)
tmin=Entry(Ventana, bg="white")
tmin.place(x=220,y=300, width=100, height=30)
tseg=Entry(Ventana, bg="white")
tseg.place(x=340,y=300, width=100, height=30)
tdec=Entry(Ventana, bg="white")
tdec.place(x=460,y=300, width=100, height=30)

Mre2=Label(Ventana, text="φ", bg="gray")
Mre2.place(x=10,y=350, width=50, height=30)
figra=Entry(Ventana, bg="white")
figra.place(x=100,y=350, width=100, height=30)
fimin=Entry(Ventana, bg="white")
fimin.place(x=220,y=350, width=100, height=30)
fiseg=Entry(Ventana, bg="white")
fiseg.place(x=340,y=350, width=100, height=30)
fidec=Entry(Ventana, bg="white")
fidec.place(x=460,y=350, width=100, height=30)

Ventana.mainloop()