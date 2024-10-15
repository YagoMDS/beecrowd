# Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos (desconsidere os valores nulos). A seguir, mostre a quantidade de valores positivos digitados.

# Entrada
# Seis valores, negativos e/ou positivos.

# Saída
# Imprima uma mensagem dizendo quantos valores positivos foram lidos.

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