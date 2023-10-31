

import math
import tkinter as tk
from tkinter import *

def decimal_a_grados_minutos_segundos(decimal):
    grados = int(decimal)
    minutos = int((decimal - grados) * 60)
    segundos = ((decimal - grados) * 60 - minutos) * 60
    return f"{grados}° {minutos}' {segundos:.2f}\""

def convert_latitudes():
    a = float(a_entry.get())
    f = 1.0 / 297
    b = a * (1.0 - f)

    opci = int(option_var.get())

    if opci == 1:
        phi = float(phi_entry.get())
        teta = math.atan((b/a) * math.tan(math.radians(phi)))
        w = math.atan((b/a) * math.tan(teta))
        w_deg = math.degrees(w)
        teta_deg = math.degrees(teta)
        result_w_label.config(text=decimal_a_grados_minutos_segundos(w_deg))
        result_teta_label.config(text=decimal_a_grados_minutos_segundos(teta_deg))
    elif opci == 2:
        w = float(w_entry.get())
        teta = math.atan((a/b) * math.tan(math.radians(w)))
        phi = math.atan((a/b) * math.tan(teta))
        phi_deg = math.degrees(phi)
        teta_deg = math.degrees(teta)
        result_phi_label.config(text=decimal_a_grados_minutos_segundos(phi_deg))
        result_teta_label.config(text=decimal_a_grados_minutos_segundos(teta_deg))
    elif opci == 3:
        teta = float(teta_entry.get())
        w = math.atan((b/a) * math.tan(math.radians(teta)))
        phi = math.atan((a/b) * math.tan(math.radians(teta)))
        w_deg = math.degrees(w)
        phi_deg = math.degrees(phi)
        result_w_label.config(text=decimal_a_grados_minutos_segundos(w_deg))
        result_phi_label.config(text=decimal_a_grados_minutos_segundos(phi_deg))

root = Tk()
root.title("Latitud de la elipse meridiana")
root.geometry("700x470")
# Create and arrange widgets
a_label = Label(root, text="Value of a:")
a_label.pack()
a_entry = Entry(root)
a_entry.pack()

f_label = Label(root, text="Value of f:")
f_label.pack()
f_entry = Entry(root)
f_entry.pack()

option_label = Label(root, text="Select an option:")
option_label.pack()

option_var = StringVar()
option_var.set("1")
option_1 = tk.Radiobutton(root, text="φ in (w,Θ)", variable=option_var, value="1")
option_2 = tk.Radiobutton(root, text="w in (φ,Θ)", variable=option_var, value="2")
option_3 = tk.Radiobutton(root, text="Θ in (w,φ)", variable=option_var, value="3")
option_1.pack()
option_2.pack()
option_3.pack()

convert_button = Button(root, text="Convert", command=convert_latitudes)
convert_button.pack()

phi_label = Label(root, text="φ:")
phi_label.pack()
phi_entry = Entry(root)
phi_entry.pack()

w_label = Label(root, text="w:")
w_label.pack()
w_entry = Entry(root)
w_entry.pack()

teta_label = Label(root, text="Θ:")
teta_label.pack()
teta_entry = Entry(root)
teta_entry.pack()

result_w_label = Label(root, text="")
result_w_label.pack()
result_phi_label = Label(root, text="")
result_phi_label.pack()
result_teta_label = Label(root, text="")
result_teta_label.pack()

# Start the GUI main loop
root.mainloop()
