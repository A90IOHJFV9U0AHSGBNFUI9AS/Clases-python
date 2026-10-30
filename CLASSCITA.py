import tkinter as tk
 
 
class Cita:
    ETIQUETAS = {
        "paciente": "Paciente",
        "medico": "Médico",
        "fecha": "Fecha",
        "hora": "Hora",
        "tipo": "Tipo",
    }
 
    def __init__(self, paciente, medico, fecha, hora, tipo):
        self.paciente = paciente
        self.medico = medico
        self.fecha = fecha
        self.hora = hora
        self.tipo = tipo
 
    def mostrar_cita(self):
        return "\n".join(
            f"{etiqueta}: {getattr(self, clave)}"
            for clave, etiqueta in self.ETIQUETAS.items()
        )
 
 
class VentanaCitas(tk.Tk):
    CAMPOS = [
        ("paciente", "Paciente"),
        ("medico", "Médico"),
        ("fecha", "Fecha (DD/MM/AAAA)"),
        ("hora", "Hora (HH:MM)"),
        ("tipo", "Tipo de cita"),
    ]
 
    def __init__(self):
        super().__init__()
        self.title("Registro de Citas")
        self.geometry("320x350")
        self.entradas = {}
        self._crear_formulario()
        self.resultado = tk.Label(self, text="")
        self.resultado.pack()
 
    def _crear_formulario(self):
        for clave, etiqueta in self.CAMPOS:
            tk.Label(self, text=etiqueta).pack()
            self.entradas[clave] = tk.Entry(self)
            self.entradas[clave].pack()
        tk.Button(self, text="Registrar cita", command=self.registrar).pack(pady=10)
 
    def registrar(self):
        datos = {clave: entrada.get() for clave, entrada in self.entradas.items()}
        self.resultado.config(text=Cita(**datos).mostrar_cita())
 
 
if __name__ == "__main__":
    VentanaCitas().mainloop()