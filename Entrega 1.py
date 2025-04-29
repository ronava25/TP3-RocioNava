database = {}

def nuevo_usuario():
    usuario = input("Ingrese un nombre de usuario: ")
    while usuario == "" or usuario == " ":
        print("El nombre de usuario no puede estar vacío o contener solo espacios.")
        usuario = input("Ingrese un nombre de usuario: ")

    if usuario in database:
        print("Usuario existente. Intente de nuevo.")
    else:
        contraseña = input("Ingrese una contraseña: ")
        while contraseña == "" or contraseña == " ":
            print("La contraseña no puede estar vacía o contener solo espacios.")
            contraseña = input("Ingrese una contraseña: ")
        database[usuario] = contraseña
        print("Nuevo usuario registrado con éxito.")


def ver_database():
    if len(database)== 0:
        print("No hay usuarios registrados aún.")
    else:
        print("Usuarios registrados:")
        for usuario in database:
            print(usuario + database[usuario])
        print()

def login():
    usuario = input("Nombre de usuario: ")
    if usuario in database:
        contraseña = input("Contraseña: ")
        if database[usuario] == contraseña:
            print("Sesión iniciada con éxito.")
        else:
            print("Contraseña incorrecta. Intente de nuevo.")
    else:
        print("El usuario ingresado no existe.")