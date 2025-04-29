
def es_mayor(edad):
    '''tiene que ser un numero integro'''
    if edad >= 18:
        print("El usuario es mayor de edad")
    else:
        print("El usuario no es mayor")

es_mayor(15)
es_mayor(20)
es_mayor(50)



def saludar_con_nombre(nombre):
    print(f'Hola, {nombre}, ¿cómo estás?')

saludar_con_nombre("Solcito")
saludar_con_nombre("Valen")
