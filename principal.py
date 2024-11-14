# principal.py

from gestor_citas import GestorCitas

def main():
    gestor = GestorCitas()

    while True:
        print("\nBienvenido a la aplicación de citas")
        print("1. Crear una cita")
        print("2. Consultar próxima cita")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre_usuario = input("Ingrese el nombre del usuario: ")
            fecha = input("Ingrese la fecha de la cita (AAAA-MM-DD): ")
            hora = input("Ingrese la hora de la cita (HH:MM): ")
            gestor.crear_cita(nombre_usuario, fecha, hora)

        elif opcion == "2":
            gestor.consultar_proxima_cita()

        elif opcion == "3":
            print("Saliendo de la aplicación.")
            break

        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    main()
