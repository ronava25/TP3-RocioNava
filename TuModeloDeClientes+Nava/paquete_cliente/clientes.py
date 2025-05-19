from paquete_cliente.usuarios import Usuario

class Cliente(Usuario):
    def __init__(self, nombre, apellido, correo, contrasena):
        super().__init__(nombre, apellido, correo, contrasena, tipo_usuario="Cliente")
