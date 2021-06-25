def run():
    for contador in range(1000):
        if contador % 2 != 0:
            continue            #Salta a la proxima iteracion
        print(contador)
        if contador == 630:
            break               #finaliza las iteraciones


if __name__ == '__main__':
    run()