

import numpy as np
import math as m
import cmath as cm
import matplotlib.pyplot as plt
from tkinter import *
import mpmath as mp
from mpl_toolkits.mplot3d import Axes3D



def dibujo():
    xg=int(xgra.get())
    xm=int(xmin.get())
    xs=int(xseg.get())
    yg=int(ygra.get())
    ym=int(ymin.get())
    ys=int(yseg.get())
    
    term1=xs/60
    term2=xm+term1
    s=term2/60
    fit1=xg+s #grados decimal x
    
    ter1=ys/60
    ter2=ym+ter1
    s1=ter2/60
    landat1=yg+s1 #grados decimal y
    
    phi = np.linspace(0,2*np.pi, 256).reshape(256, 1) # the angle of the projection in the xy-plane
    theta = np.linspace(0, np.pi, 256).reshape(-1, 256) # the angle from the polar axis, ie the polar angle
    
    
    a1=float(a.get())
    b1=float(b.get())
    
    
    e2=(a1**2-b1**2)/(a1**2) #e^2
    ep2=(a1**2-b1**2)/(b1**2) #e'^2
    
    radius = ((a1)/(m.sqrt(1-e2*(m.sinh((fit1*m.pi)/180)**2))))
    
    x1=(radius)*m.cos((fit1*m.pi)/180)*m.cos((landat1*m.pi)/180)
    y1=(radius)*m.cos((fit1*m.pi)/180)*m.sin((landat1*m.pi)/180)
    z1=(radius*(1-e2))*m.sin((fit1*m.pi)/180)
    
    
    
    # Transformation formulae for a spherical coordinate system.
    x = radius*np.sin(theta)*np.cos(phi)
    y = radius*np.sin(theta)*np.sin(phi)
    z = radius*np.cos(theta)
    
    c.delete(0,"end")
    c.insert(0,e2)
    N.delete(0,"end")
    N.insert(0,radius)
    
    
    fig = plt.figure(figsize=plt.figaspect(1))  # Square figure
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, color='gray')
    ax.text(x1, y1, z1, "o", color='black')
    plt.title("Elipsoide 3D")
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()



Ventana = Tk()
Ventana.title("Elipsoide")
Ventana.geometry("700x370")

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



lgrados=Label(Ventana, text="°", bg="gray")
lgrados.place(x=125,y=200, width=50, height=30)
lminutos=Label(Ventana, text="'", bg="gray")
lminutos.place(x=245,y=200, width=50, height=30)
lsegundos=Label(Ventana, text="''", bg="gray")
lsegundos.place(x=365,y=200, width=50, height=30)

lx=Label(Ventana, text="φ", bg="gray")
lx.place(x=10,y=250, width=50, height=30)
xgra=Entry(Ventana, bg="white")
xgra.place(x=100,y=250, width=100, height=30)
xmin=Entry(Ventana, bg="white")
xmin.place(x=220,y=250, width=100, height=30)
xseg=Entry(Ventana, bg="white")
xseg.place(x=340,y=250, width=100, height=30)

ly=Label(Ventana, text="λ", bg="gray")
ly.place(x=10,y=290, width=50, height=30)
ygra=Entry(Ventana, bg="white")
ygra.place(x=100,y=290, width=100, height=30)
ymin=Entry(Ventana, bg="white")
ymin.place(x=220,y=290, width=100, height=30)
yseg=Entry(Ventana, bg="white")
yseg.place(x=340,y=290, width=100, height=30)



B1=Button(Ventana, text="Caso 1", command=dibujo)
B1.place(x=150,y=100, width=100, height=30)



Ventana.mainloop()