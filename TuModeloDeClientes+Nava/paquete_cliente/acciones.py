from paquete_cliente.clientes import Cliente

def nuevo_usuario(database):
    nombre = input("Nombre: ")
    while nombre == "" or " " in nombre:
        print("El nombre no puede estar en blanco. Intente de nuevo.")
        nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    while apellido == "" or " " in apellido:
        print("El apellido no puede estar en blanco. Intente de nuevo.")
        apellido = input("Apellido: ")
    correo = input("Correo electrónico: ")
    while correo == "" or " " in correo:
        print("El correo no puede estar en blanco. Intente de nuevo")
        correo = input("Correo electrónico: ")
    if correo in database:
        print("Correo ya registrado. Inicie sesión o intente con otro correo.")
    else:
        contrasena = input("Contraseña: ")
        while contrasena == "" or " " in contrasena:
            print("La contraseña no puede estar en blanco. Intente de nuevo.")
            contrasena = input("Contraseña: ")
        else:
            cliente = Cliente(nombre, apellido, correo, contrasena)
            database[correo] = cliente
            print("Nuevo usuario registrado con éxito.")


def ver_usuarios(database):
    if not database:
        print("No hay usuarios registrados aún.")
    else:
        print("Usuarios registrados:")
        for cliente in database.values():
            print(f"Correo: {cliente.correo} // Contraseña: {cliente.contrasena}")


def login(database):
    correo = input("Correo: ")
    if correo in database:
        while True:
            contrasena = input("Contraseña: ")
            if contrasena == database[correo].contrasena:
                usuario = database[correo]
                while True:
                    print(f"Hola, {usuario.nombre}! ¿Qué te gustaría hacer ahora?")
                    print("1. Cambiar correo electrónico")
                    print("2. Cambiar contraseña")
                    print("3. Cerrar sesión")
                
                    opcion = input("Seleccione una opción: ")
                
                    if opcion == "1":
                        nuevo_correo = input("Ingrese el nuevo correo: ")
                        print(usuario.actualizar_correo(nuevo_correo))
                        database.pop(correo)
                        database[nuevo_correo] = usuario
                        correo = nuevo_correo
                    elif opcion == "2":
                        nueva_contrasena = input("Ingrese la nueva contraseña: ")
                        print(usuario.actualizar_contrasena(nueva_contrasena))
                    elif opcion == "3":
                        print("Sesión finalizada.")
                        break
                    else:
                        print("Opción inválida. Intente de nuevo.")
                return usuario
            else:
                print("Contraseña incorrecta. Intente de nuevo.")
    else:
        print("Correo no registrado. Intente de nuevo.")
