

import numpy as np
import math as m
import cmath as cm
import matplotlib.pyplot as plt
from tkinter import *
import mpmath as mp


X=np.zeros(8)
Y=np.zeros(8)

def caso1():
    NAA=float(NA.get())
    NBB=float(NB.get())
    EAA=float(EA.get())
    EBB=float(EB.get())
    NCC=float(NC.get())
    ECC=float(EC.get())
    xg=int(xgra.get())
    xm=int(xmin.get())
    xs=int(xseg.get())
    yg=int(ygra.get())
    ym=int(ymin.get())
    ys=int(yseg.get())
    zg=int(zgra.get())
    zm=int(zmin.get())
    zs=int(zseg.get())
    
    term1=xs/60
    term2=xm+term1
    s=term2/60
    term3=xg+s #grados decimal x
    
    ter1=ys/60
    ter2=ym+ter1
    s1=ter2/60
    ter3=yg+s1 #grados decimal y
    
    te1=zs/60
    te2=zm+te1
    s2=te2/60
    te3=zg+s2 #grados decimal z
    
    
    a=m.degrees(m.atan((ECC-EAA)/(NCC-NAA))-m.atan((EBB-EAA)/(NBB-NAA)))
    b=m.degrees(m.atan((EAA-EBB)/(NAA-NBB))-(m.atan((ECC-EBB)/(NCC-NBB))))
    c=m.degrees(m.atan((EBB-ECC)/(NBB-NCC))-(m.atan((EAA-ECC)/(NAA-NCC))))

    k1= 1/(mp.cot((a*m.pi)/180)-mp.cot((term3*m.pi)/180))
    k2= 1/(mp.cot((b*m.pi)/180)-mp.cot((ter3*m.pi)/180))
    k3= 1/(mp.cot((c*m.pi)/180)-mp.cot((te3*m.pi)/180))
    
    
    N1=k1*EAA+k2*EBB+k3*ECC
    D1=k1+k2+k3
    EP=N1/D1
    
    N2=k1*NAA+k2*NBB+k3*NCC
    D2=k1+k2+k3
    NP=N2/D2
    
    
    print(NP)
    print(EP)

    
    X[0]=EAA
    X[1]=EBB
    X[2]=ECC
    X[3]=EAA
    X[4]=EP
    X[5]=ECC
    X[6]=EBB
    X[7]=EP
    
    Y[0]=NAA
    Y[1]=NBB
    Y[2]=NCC
    Y[3]=NAA
    Y[4]=NP
    Y[5]=NCC
    Y[6]=NBB
    Y[7]=NP


    plt.plot(X,Y, color = "blue" ,linestyle = "-")
    plt.scatter(X[0],Y[0],color = "red", marker="o",label="A")
    plt.scatter(X[1],Y[1],color = "green", marker="D",label="B")
    plt.scatter(X[2],Y[2],color = "black", marker="^",label="C")
    plt.scatter(X[4],Y[4],color = "black", marker="^",label="P")
    plt.annotate("A", (EAA,NAA+8))
    plt.annotate("P", (EP-8,NP-5))
    plt.annotate("B", (EBB,NBB+5))
    plt.annotate("C", (ECC-8,NCC))
    plt.title("trisección")
    plt.xlabel("Este")
    plt.ylabel("Norte")
    plt.legend( )
    plt.show()


    
    

    
    

Ventana = Tk()
Ventana.title("Trisección")
Ventana.geometry("700x470")

lNA=Label(Ventana, text="NA", bg="gray")
lNA.place(x=10,y=10, width=50, height=30)
NA=Entry(Ventana, bg="white")
NA.place(x=100,y=10, width=100, height=30)

lNB=Label(Ventana, text="NB", bg="gray")
lNB.place(x=10,y=50, width=50, height=30)
NB=Entry(Ventana, bg="white")
NB.place(x=100,y=50, width=100, height=30)

lNC=Label(Ventana, text="NC", bg="gray")
lNC.place(x=10,y=90, width=50, height=30)
NC=Entry(Ventana, bg="white")
NC.place(x=100,y=90, width=100, height=30)

lEA=Label(Ventana, text="EA", bg="gray")
lEA.place(x=220,y=10, width=50, height=30)
EA=Entry(Ventana, bg="white")
EA.place(x=310,y=10, width=100, height=30)

lEB=Label(Ventana, text="EB", bg="gray")
lEB.place(x=220,y=50, width=50, height=30)
EB=Entry(Ventana, bg="white")
EB.place(x=310,y=50, width=100, height=30)

lEC=Label(Ventana, text="EC", bg="gray")
lEC.place(x=220,y=90, width=50, height=30)
EC=Entry(Ventana, bg="white")   
EC.place(x=310,y=90, width=100, height=30)



lgrados=Label(Ventana, text="°", bg="gray")
lgrados.place(x=125,y=200, width=50, height=30)
lminutos=Label(Ventana, text="'", bg="gray")
lminutos.place(x=245,y=200, width=50, height=30)
lsegundos=Label(Ventana, text="''", bg="gray")
lsegundos.place(x=365,y=200, width=50, height=30)

lx=Label(Ventana, text="ẋ", bg="gray")
lx.place(x=10,y=250, width=50, height=30)
xgra=Entry(Ventana, bg="white")
xgra.place(x=100,y=250, width=100, height=30)
xmin=Entry(Ventana, bg="white")
xmin.place(x=220,y=250, width=100, height=30)
xseg=Entry(Ventana, bg="white")
xseg.place(x=340,y=250, width=100, height=30)

ly=Label(Ventana, text="ŷ", bg="gray")
ly.place(x=10,y=290, width=50, height=30)
ygra=Entry(Ventana, bg="white")
ygra.place(x=100,y=290, width=100, height=30)
ymin=Entry(Ventana, bg="white")
ymin.place(x=220,y=290, width=100, height=30)
yseg=Entry(Ventana, bg="white")
yseg.place(x=340,y=290, width=100, height=30)

lz=Label(Ventana, text="ẑ", bg="gray")
lz.place(x=10,y=340, width=50, height=30)
zgra=Entry(Ventana, bg="white")
zgra.place(x=100,y=340, width=100, height=30)
zmin=Entry(Ventana, bg="white")
zmin.place(x=220,y=340, width=100, height=30)
zseg=Entry(Ventana, bg="white")
zseg.place(x=340,y=340, width=100, height=30)

B1=Button(Ventana, text="Caso 1", command=caso1)
B1.place(x=510,y=20, width=100, height=30)



Ventana.mainloop()