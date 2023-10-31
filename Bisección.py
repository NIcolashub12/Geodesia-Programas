

import numpy as np
import math as m
import cmath as cm
import matplotlib.pyplot as plt
from tkinter import *
import mpmath as mp



X=np.zeros(4)
Y=np.zeros(4)
x=np.zeros(200)
y=np.zeros(200)

def biseccion():
    NAA=int(NA.get())
    NBB=int(NB.get())
    EAA=int(EA.get())
    EBB=int(EB.get())
    ALFAgra=int(Alfagra.get())
    ALFAm=int(Alfamin.get())
    ALFAs=int(Alfaseg.get())
    betag=int(betagra.get())
    betam=int(betamin.get())
    betas=int(betaseg.get())
    
    term1=ALFAs/60
    term2=ALFAm+term1
    s=term2/60
    term3=ALFAgra+s
    
    ter1=betas/60
    ter2=betam+ter1
    s1=ter2/60
    ter3=betag+s1
    
    
    N1=(EBB-EAA)+NAA*mp.cot((ter3*m.pi)/180)+NBB*mp.cot((term3*m.pi)/180)
    D1=mp.cot((term3*m.pi)/180)+mp.cot((ter3*m.pi)/180)
    NP=N1/D1
    
    N2=(NAA-NBB)+EAA*mp.cot((ter3*m.pi)/180)+EBB*mp.cot((term3*m.pi)/180)
    D2=mp.cot((term3*m.pi)/180)+mp.cot((ter3*m.pi)/180)
    EP=N2/D2
    
    print(NP)
    print(EP)
    
    X[0]=EAA
    X[1]=EP
    X[2]=EBB
    X[3]=EAA
    
    Y[0]=NAA
    Y[1]=NP
    Y[2]=NBB
    Y[3]=NAA
    
    

    plt.plot(X,Y, color = "blue" ,linestyle = "-")
    plt.scatter(X[0],Y[0],color = "red", marker="o",label="A")
    plt.scatter(X[1],Y[1],color = "green", marker="D",label="P")
    plt.scatter(X[2],Y[2],color = "black", marker="^",label="B")
    plt.annotate("A", (EAA+50,NAA+50))
    plt.annotate("P", (EP-50,NP-50))
    plt.annotate("B", (EBB-50,NBB-50))
    plt.title("Bisección")
    plt.xlabel("Este")
    plt.ylabel("Norte")
    plt.legend( )
    plt.show()
    
    
Ventana = Tk()
Ventana.title("Bisección")
Ventana.geometry("700x370")

lNA=Label(Ventana, text="NA", bg="gray")
lNA.place(x=10,y=10, width=50, height=30)
NA=Entry(Ventana, bg="white")
NA.place(x=100,y=10, width=100, height=30)

lNB=Label(Ventana, text="NB", bg="gray")
lNB.place(x=10,y=50, width=50, height=30)
NB=Entry(Ventana, bg="white")
NB.place(x=100,y=50, width=100, height=30)

lEA=Label(Ventana, text="EA", bg="gray")
lEA.place(x=10,y=90, width=50, height=30)
EA=Entry(Ventana, bg="white")
EA.place(x=100,y=90, width=100, height=30)

lEB=Label(Ventana, text="EB", bg="gray")
lEB.place(x=10,y=130, width=50, height=30)
EB=Entry(Ventana, bg="white")
EB.place(x=100,y=130, width=100, height=30)



lgrados=Label(Ventana, text="°", bg="gray")
lgrados.place(x=125,y=200, width=50, height=30)
lminutos=Label(Ventana, text="'", bg="gray")
lminutos.place(x=245,y=200, width=50, height=30)
lsegundos=Label(Ventana, text="''", bg="gray")
lsegundos.place(x=365,y=200, width=50, height=30)

lalfa=Label(Ventana, text="α", bg="gray")
lalfa.place(x=10,y=250, width=50, height=30)
Alfagra=Entry(Ventana, bg="white")
Alfagra.place(x=100,y=250, width=100, height=30)
Alfamin=Entry(Ventana, bg="white")
Alfamin.place(x=220,y=250, width=100, height=30)
Alfaseg=Entry(Ventana, bg="white")
Alfaseg.place(x=340,y=250, width=100, height=30)

lbeta=Label(Ventana, text="β", bg="gray")
lbeta.place(x=10,y=290, width=50, height=30)
betagra=Entry(Ventana, bg="white")
betagra.place(x=100,y=290, width=100, height=30)
betamin=Entry(Ventana, bg="white")
betamin.place(x=220,y=290, width=100, height=30)
betaseg=Entry(Ventana, bg="white")
betaseg.place(x=340,y=290, width=100, height=30)

B31=Button(Ventana, text="DIBUJO", command=biseccion)
B31.place(x=410,y=30, width=100, height=30)

Ventana.mainloop()