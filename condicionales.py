menu = """
Bienvenido al comversor de monedas.

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opcion:
"""

opcion = input(menu)

numero = int(input('Escribe un numero: '))

if numero > 5:
    print('El numero es mayor a 5')
elif numero == 5:
    print('El numero es igual a 5')
else:
    print('el numero es menor que 5')