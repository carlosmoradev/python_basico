menu = """
Bienvenido al comversor de monedas.

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opcion:
"""

opcion = int(input(menu))

if opcion == 1:
    pesos = float(input("cuantos pesos Colombianos tienes? "))
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    print("Tienes $" + str(round(dolares, 2)) + " dolares.")
elif opcion == 2:
    pesos = float(input("cuantos pesos Argentinos tienes? "))
    valor_dolar = 65
    dolares = pesos / valor_dolar
    print("Tienes $" + str(round(dolares, 2)) + " dolares.")
elif opcion == 3:
    pesos = float(input("cuantos pesos Mexicanos tienes? "))
    valor_dolar = 24
    dolares = pesos / valor_dolar
    print("Tienes $" + str(round(dolares, 2)) + " dolares.")
else:
    print('Ingresa una opcion correcta por favor')