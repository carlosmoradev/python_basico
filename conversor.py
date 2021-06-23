def conversor(tipo_moneda, valor_dolar):
    pesos = float(input("cuantos " + tipo_moneda + " tienes? "))
    dolares = pesos / valor_dolar
    print("Tienes $" + str(round(dolares, 2)) + " dolares.")

menu = """
Bienvenido al comversor de monedas.

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opcion:
"""

opcion = int(input(menu))

if opcion == 1:
    conversor("Pesos Colombianos", 3875)
elif opcion == 2:
    conversor("Pesos Argentinos", 65)
elif opcion == 3:
    conversor("Pesos Mexicanos", 24)
else:
    print('Ingresa una opcion correcta por favor')