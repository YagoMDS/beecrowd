# Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. 
# Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.

# Entrada
# Leia três valores de ponto flutuante (double) A, B e C.

# Saída
# Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel calcular". 
# Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto, com uma mensagem correspondente conforme exemplo abaixo. Imprima sempre o final de linha após cada mensagem.

import math 

def main():
    a, b, c = input().split()

    a = float(a)
    b = float(b)
    c = float(c)
    
    delta = (b*b) - (4*a*(c))
    
    if delta > 0 and a != 0:
        raizdelta = math.sqrt(delta)
        if raizdelta > 0:
            x1 = (-b + (raizdelta)) / (2*a)
            x2 = (-b - (raizdelta)) / (2*a)
            print(f'R1 = {x1:.5f}')
            print(f'R2 = {x2:.5f}')
    else:
        print("Impossivel calcular")

main()