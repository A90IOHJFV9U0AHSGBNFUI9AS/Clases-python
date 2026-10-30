import tkinter as tk
 
 
class Medico:
    MESES_ANIO = 12
 
    def __init__(self, nombre, especialidad, sueldo):
        self.nombre = nombre
        self.especialidad = especialidad
        self.sueldo = float(sueldo)
 
    def calcular_sueldo_anual(self):
        return self.sueldo * self.MESES_ANIO
 
    def resumen(self):
        return (
            f"Médico: {self.nombre}\n"
            f"Especialidad: {self.especialidad}\n"
            f"Sueldo anual: ${self.calcular_sueldo_anual():,.0f}"
        )
 
 
class VentanaMedico(tk.Tk):
    CAMPOS = [
        ("nombre", "Nombre del médico"),
        ("especialidad", "Especialidad"),
        ("sueldo", "Sueldo mensual"),
    ]
 
    def __init__(self):
        super().__init__()
        self.title("Registro de Médico")
        self.geometry("320x280")
        self.entradas = {}
        self._crear_formulario()
        self.resultado = tk.Label(self, text="")
        self.resultado.pack()
 
    def _crear_formulario(self):
        for clave, etiqueta in self.CAMPOS:
            tk.Label(self, text=etiqueta).pack()
            self.entradas[clave] = tk.Entry(self)
            self.entradas[clave].pack()
        tk.Button(self, text="Registrar médico", command=self.registrar).pack(pady=10)
 
    def registrar(self):
        datos = {clave: entrada.get() for clave, entrada in self.entradas.items()}
        try:
            self.resultado.config(text=Medico(**datos).resumen())
        except ValueError:
            self.resultado.config(text="Ingresa un sueldo válido")
 
 
if __name__ == "__main__":
    VentanaMedico().mainloop()