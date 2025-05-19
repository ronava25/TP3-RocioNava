class Usuario:
    def __init__(self, nombre, apellido, correo, contrasena, tipo_usuario="Cliente"):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.contrasena = contrasena
        self.tipo_usuario = tipo_usuario

    def __str__(self):
        return  f"{self.nombre} {self.apellido}"

    def actualizar_correo(self, nuevo_correo):
        self.correo = nuevo_correo
        return f"Correo actualizado a {self.correo}."

    def actualizar_contrasena(self, nueva_contrasena):
        self.contrasena = nueva_contrasena
        return "Contraseña actualizada exitosamente."
