# Escreva um programa que leia um valor inteiro N. Este N é a quantidade de linhas de saída que serão apresentadas na execução do programa.

# Entrada
# O arquivo de entrada contém um número inteiro positivo N.

# Saída
# Imprima a saída conforme o exemplo fornecido.

def main():

    N = int(input())  # Lê o valor inteiro N

    num = 1
    for _ in range(N):
        print(num, num + 1, num + 2, "PUM")
        num += 4

        
main()