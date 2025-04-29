from Paquete.acciones import Acciones

def main():
    acciones = Acciones()

    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar nuevo usuario")
        print("2. Ver usuarios registrados")
        print("3. Iniciar sesión")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            acciones.nuevo_usuario()
        elif opcion == "2":
            acciones.ver_usuarios()
        elif opcion == "3":
            acciones.login()
        elif opcion == "4":
            print("Sesión finalizada.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
