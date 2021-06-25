def run():
    for contador in range(1000):
        if contador % 2 != 0:
            continue            #Salta a la proxima iteracion
        print(contador)
        if contador == 630:
            break               #finaliza las iteraciones

    
    texto = input('Escribe un texto:')
    for letra in texto:
        if letra == "j":
            break
        print(letra)


if __name__ == '__main__':
    run()