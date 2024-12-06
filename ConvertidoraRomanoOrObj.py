import tkinter as tk
from tkinter import ttk
from ClaseRomanos import ConvertidoraRomano 

def para_convertir():
    try:

        numero = int(input_decimal.get())  

        convertidor = ConvertidoraRomano()

        convertidor.rangoNumero(numero)  

        resultado = convertidor.Convertir() 

        etiqueta_romano.config(text=f"Su número en romano es: ", font=("Times New Roman", 12))
        etiqueta_rrespuesta.config(text=f"{resultado}", foreground="red" ,font=("Times New Roman", 12))
        ventana.after(6000, lambda: etiqueta_rrespuesta.config(text=""))
        ventana.after(14000, lambda: etiqueta_rrespuesta.config(text=""))
        ventana.after(6000, lambda: etiqueta_romano.config(text="Ingresa otro número...",foreground="green", font=("Times New Roman", 12)))
        ventana.after(14000, lambda: etiqueta_romano.config(text=""))
    except ValueError as e:
        etiqueta_letras.config(text="Introduce valores dentro del rango 1 - 3999.", foreground="red")
        ventana.after(2000, lambda: etiqueta_letras.config(text=""))

ventana = tk.Tk()
ventana.title("Convertidor de número decimal a romano")
ventana.config(width=610, height=150)

etiqueta_decimal = ttk.Label(ventana, text="Introduce el número decimal:", font=("Times New Roman", 12))
etiqueta_decimal.place(x=50, y=20)

etiqueta_romano = ttk.Label(ventana)
etiqueta_romano.place(x=50, y=100)

etiqueta_rrespuesta = ttk.Label(ventana)
etiqueta_rrespuesta.place(x=210, y=100)

etiqueta_letras = ttk.Label(ventana)
etiqueta_letras.place(x=368, y=23)


input_decimal = ttk.Entry(ventana)
input_decimal.place(x=233, y=22)

button_convertir = ttk.Button(ventana, text="Convertir", command=para_convertir)
button_convertir.place(x=250, y=52, width=80)

ventana.mainloop()
