# Leia um valor inteiro X (1 <= X <= 1000). Em seguida mostre os ímpares de 1 até X, um valor por linha, inclusive o X, se for o caso.

# Entrada
# O arquivo de entrada contém 1 valor inteiro qualquer.

# Saída
# Imprima todos os valores ímpares de 1 até X, inclusive X, se for o caso.

def main():

    x = int(input())
    impares = []
    i = 0

    while True:

        i += 1
        if i <= x:
            if i % 2 == 1:
                impares.append(i) 
        else:
            break

    for impar in impares: print(impar)

main()