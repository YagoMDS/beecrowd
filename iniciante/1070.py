# Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos a partir de X, um valor por linha, inclusive o X ser for o caso.

# Entrada
# A entrada será um valor inteiro positivo.

# Saída
# A saída será uma sequência de seis números ímpares.

def main():

    x = int(input())
    i = 0

    while i < 6:

        if x % 2 == 1:   
            print(x)
            i += 1
        x += 1
main()