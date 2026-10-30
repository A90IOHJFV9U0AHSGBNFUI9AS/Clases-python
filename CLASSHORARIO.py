import tkinter as tk
 
 
class Horario:
    def __init__(self, medico, dia, hora_inicio, hora_fin):
        self.medico, self.dia = medico, dia
        self.hora_inicio, self.hora_fin = hora_inicio, hora_fin
        self.disponible = True
 
    def mostrar_horario(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return (
            f"Médico: {self.medico}\nDía: {self.dia}\n"
            f"Horario: {self.hora_inicio} - {self.hora_fin}\nEstado: {estado}"
        )
 
 
def registrar():
    horario = Horario(*[e.get() for e in entradas])
    resultado.config(text=horario.mostrar_horario())
 
 
ventana = tk.Tk()
ventana.title("Registro de Horarios")
ventana.geometry("320x300")
 
entradas = []
for texto in ["Médico", "Día", "Hora de inicio", "Hora de finalización"]:
    tk.Label(ventana, text=texto).pack()
    entradas.append(tk.Entry(ventana))
    entradas[-1].pack()
 
tk.Button(ventana, text="Registrar horario", command=registrar).pack(pady=10)
resultado = tk.Label(ventana, text="")
resultado.pack()
 
ventana.mainloop()