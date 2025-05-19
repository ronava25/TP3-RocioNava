from paquete_cliente import Cliente
from paquete_cliente import Usuario
from paquete_cliente import ver_usuarios, nuevo_usuario, login

def main():
    database = {}

    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar nuevo usuario")
        print("2. Ver usuarios registrados")
        print("3. Iniciar sesión")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nuevo_usuario(database)
        elif opcion == "2":
            ver_usuarios(database)
        elif opcion == "3":
            login(database)
        elif opcion == "4":
            print("Sesión finalizada.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
