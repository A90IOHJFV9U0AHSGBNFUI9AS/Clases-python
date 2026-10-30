import tkinter as tk
from datetime import date
 
 
class Persona:
    def __init__(self, nombre, nacimiento):
        self.nombre = nombre
        self.nacimiento = date.fromisoformat(nacimiento)
 
    def calcular_edad(self):
        hoy = date.today()
        ya_cumplio = (hoy.month, hoy.day) >= (self.nacimiento.month, self.nacimiento.day)
        return hoy.year - self.nacimiento.year - (not ya_cumplio)
 
 
def registrar():
    try:
        p = Persona(nombre.get(), nacimiento.get())
        resultado.config(text=f"{p.nombre}: {p.calcular_edad()} años")
    except ValueError:
        resultado.config(text="Ingresa los datos correctamente")
 
 
ventana = tk.Tk()
ventana.title("Registro de Persona")
ventana.geometry("300x220")
 
tk.Label(ventana, text="Nombre").pack()
nombre = tk.Entry(ventana)
nombre.pack()
 
tk.Label(ventana, text="Nacimiento (AAAA-MM-DD)").pack()
nacimiento = tk.Entry(ventana)
nacimiento.pack()
 
tk.Button(ventana, text="Calcular edad", command=registrar).pack(pady=10)
resultado = tk.Label(ventana, text="")
resultado.pack()
 
ventana.mainloop()