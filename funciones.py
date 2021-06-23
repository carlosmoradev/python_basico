# def imprimir_mensaje():
#     print('Mensaje especial: ')
#     print('Estoy aprendiendo a usar funciones!!!')

# imprimir_mensaje()

def conversacion(mensaje):
    print('Hola')
    print('Como estas')
    print(mensaje)
    print('Adios!')

opcion = int(input('Elige una opcion (1, 2, 3):'))
if opcion == 1:
    conversacion('Elegiste la primera opcion')
elif opcion == 2:
    conversacion('Segunda opcion elegida')
elif opcion == 3:
    conversacion('Haz elegido la tercera')
else:
    print('Elige una opcion correcta.')