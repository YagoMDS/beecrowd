# Leia um valor inteiro N. Apresente todos os números entre 1 e 10000 que divididos por N dão resto igual a 2.

# Entrada
# A entrada contém um valor inteiro N (N < 10000).

# Saída
# Imprima todos valores que quando divididos por N dão resto = 2, um por linha.

def main():
    
    n = int(input())
    i = 1

    while i <= 10000:
    
        if i % n == 2:
            print(i)
        i+=1
    
main()

## Ou

# def main():
#     N = int(input())


#     for i in range(1, 10001):
#         if i % N == 2:  # Verifica se o resto da divisão por N é 2
#             print(i)
# main()