# def ingresar_notas():
#     notas = []
#     while True:
#         entrada = input("Ingrese una nota (escriba 'fin' para finalizar): ")
#         if entrada == "fin":
#             break
#         elif entrada == "":
#             print("No se ingresó ninguna nota.")
#             continue
#         #convertir decimales en enteros
#         if entrada.isdecimal():
#             nota = int(entrada)
#             if nota < 0 or nota > 10:
#                 print("La nota debe estar entre 0 y 10")
#                 continue
#             #pegar las notas añadidas a la lista de notas
#             notas.append(nota)
#         else:
#             print("La nota debe ser un número")
#     return notas

# def promediar(notas):
#     return sum(notas) / len(notas)

# def mostrar(promedio, notas):
#     print("Las notas son:", notas)
#     print("El promedio es:", promedio)

# def main():
#     notas = ingresar_notas()
#     promedio = promediar(notas)
#     if len(promedio) > 4
#     mostrar(promedio, notas)
# main()


# def regresiva(parametros):
#     if parametros <= 0:
#         print("Despegue!")
#     else:
#         print(parametros)
#         regresiva(parametros-1) 
# regresiva(5)

def año_bisiesto():
    while int:
        año = input(int("Ingrese un año: "))
        if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
            print("El año es bisiesto")
        else:
            print("El año no es bisiesto")

def main():
    año_bisiesto
main()