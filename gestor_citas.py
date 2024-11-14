# gestor_citas.py

from cola import Cola
from cita import Cita

class GestorCitas:
    def __init__(self):
        self.cola_citas = Cola()

    def crear_cita(self, nombre_usuario, fecha, hora):
        cita = Cita(nombre_usuario, fecha, hora)
        self.cola_citas.encolar(cita)
        print("Cita creada exitosamente.")

    def consultar_proxima_cita(self):
        proxima_cita = self.cola_citas.ver_primero()
        if proxima_cita:
            print("Próxima cita:", proxima_cita)
        else:
            print("No hay citas pendientes.")
