# Juego basico para adivinar un numero
import random


def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input('Eligen un numero entre el 1 y el 100: '))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('Busca un numero mas grande.')
        else:
            print('Busca un numero mas pequeño.')
            numero_elegido = int(input('Elige otro numero: '))
    print('Ganaste!!!')


if __name__ == '__main__':
    run()