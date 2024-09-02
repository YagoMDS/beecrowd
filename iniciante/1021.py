# Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

# Entrada
# O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

# Saída
# Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.

def calcular_notas(valor):
    # Notas disponíveis
    notas = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.10, 0.05, 0.01]
    quantidade_notas = {}

    # Calcula a quantidade de cada nota
    for nota in notas:
        quantidade_notas[nota] = valor // nota
        valor %= nota

    return quantidade_notas

def main():
    # Leitura do valor
    valor = float(input())

    # Calcula as notas necessárias
    quantidade_notas = calcular_notas(valor)
    verificar = '1'
    

    # Impressão do valor lido
    print(valor)

    # Impressão da quantidade de cada nota
    for nota in [100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.10, 0.05, 0.01]:
            if nota >= 1:
                print(f"{int(quantidade_notas[nota])} nota(s) de R$ {nota:.2f}")
            else:
                print(f"{quantidade_notas[nota]:.0f} moeda(s) de R$ {nota:.2f}")
            

if __name__ == "__main__":
    main()