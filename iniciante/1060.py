def main():

    lista = []
    i = 0
    positivo = 0
    negativo = 0

    while i < 6:
        lista.append(float(input()))
        if lista[i] >= 0:
            positivo+=1
        else:
            negativo+=1
        i+=1

    print(f'{positivo} valores positivos')
    
main()