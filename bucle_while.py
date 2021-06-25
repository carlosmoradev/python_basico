# Escribir todas las potencias de 2 hasta el numero limite indicado.


def run():
    LIMITE = 1000 #Se declara en mayusculas cuando es una constante
    contador = 0
    potencia_2 = 2**contador


    while potencia_2 < LIMITE:
        print('2 Elevado a la ' + str(contador) + ' es igual a: ' + str(potencia_2))
        contador += 1
        potencia_2 = 2**contador
    
    print('El calculo ha finalizado con ' + str(contador) + ' repeticiones'  )




if __name__ == '__main__':
    run()