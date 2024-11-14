# cita.py

class Cita:
    def __init__(self, nombre_usuario, fecha, hora):
        self.nombre_usuario = nombre_usuario
        self.fecha = fecha
        self.hora = hora

    def __str__(self):
        return f"Cita para {self.nombre_usuario} el {self.fecha} a las {self.hora}"
