
import tkinter as tk
from tkinter import messagebox


class Paciente:
    def __init__(self, nombre, identificacion, edad, ciudad):
        self.nombre = nombre
        self.identificacion = identificacion
        self.edad = edad
        self.ciudad = ciudad

    def mostrar_datos(self):
        return f"👤 {self.nombre}\n🪪 {self.identificacion}\n🎂 {self.edad} años\n📍 {self.ciudad}"


def registrar():
    try:
        n, i, e, c = nombre.get().strip(), identificacion.get().strip(), edad.get(), ciudad.get().strip()

        if not n or not i or not c:
            messagebox.showwarning("Aviso", "Completa todos los campos")
            return

        e = int(e)
        if e < 0 or e > 120:
            raise ValueError

        paciente = Paciente(n, i, e, c)
        resultado.config(text=paciente.mostrar_datos(), fg="#67E8F9")

    except ValueError:
        messagebox.showerror("Error", "Ingresa una edad válida entre 0 y 120")


ventana = tk.Tk()
ventana.title("Gestión de Pacientes")
ventana.geometry("360x440")
ventana.configure(bg="#0F172A")
ventana.resizable(False, False)

tk.Label(ventana, text="✚ GESTIÓN DE PACIENTES", font=("Arial", 16, "bold"),
         bg="#0F172A", fg="#38BDF8").pack(pady=20)

campos = {}
for texto in ("Nombre", "Identificación", "Edad", "Ciudad"):
    tk.Label(ventana, text=texto, bg="#0F172A", fg="white").pack()
    campos[texto] = tk.Entry(ventana, font=("Arial", 11), bg="#1E293B",
                             fg="white", insertbackground="white", relief="flat")
    campos[texto].pack(padx=40, fill="x", ipady=5, pady=(3, 10))

nombre, identificacion, edad, ciudad = [campos[x] for x in
                                         ("Nombre", "Identificación", "Edad", "Ciudad")]

tk.Button(ventana, text="REGISTRAR PACIENTE", command=registrar,
          bg="#0284C7", fg="white", font=("Arial", 10, "bold"),
          relief="flat", cursor="hand2").pack(pady=12, ipadx=15, ipady=6)

resultado = tk.Label(ventana, text="Los datos aparecerán aquí",
                     bg="#1E293B", fg="#94A3B8", font=("Arial", 11),
                     justify="left", padx=15, pady=12)
resultado.pack(fill="x", padx=25, pady=5)

ventana.mainloop()
