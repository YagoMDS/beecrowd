# Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.

# Entrada
# O arquivo de entrada contém dois valores inteiros.

# Saída
# O programa deve imprimir um valor inteiro. Este valor é a soma dos valores ímpares que estão entre os valores fornecidos na entrada que deverá caber em um inteiro.

def main():

    x = int(input())
    y = int(input())

    soma = 0

    if x < y:
        y -= 1
        while x < y:
            x += 1
            if x % 2 != 0:
                soma += x
    elif x > y:
        x -= 1
        while x > y:
            y += 1
            if y % 2 != 0:
                soma += y
    
    print(soma)

main()

# Solução com list comprehension

# def main():
#     x = int(input())
#     y = int(input())

#     # Garante que x seja sempre o menor valor
#     if x > y:
#         x, y = y, x

#     # Soma dos ímpares no intervalo aberto (x+1 até y-1)
#     soma = sum(n for n in range(x + 1, y) if n % 2 != 0)

#     print(soma)

# main()