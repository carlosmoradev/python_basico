def run():
    frase = input('Ingresa una frase: ')
    for caracter in frase:
        print(caracter.capitalize()) #responde igual a upper porque solo esta tomando la primera letra
        
        
    print(frase.capitalize())


if __name__ == '__main__':
    run()