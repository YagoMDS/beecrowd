# Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

# Entrada
# O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

# Saída
# Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.


"""
# CÓDIGO FUNCIONA PORÉM NÃO IMPRIME COM O CENTAVO É 0,03 OU QUANDO É 0,08

from decimal import Decimal, ROUND_FLOOR

def calcular_notas_moedas(valor):
    # Notas e moedas disponíveis
    notas = [100, 50, 20, 10, 5, 2]
    moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

    # Quantidade de notas e moedas
    quantidade_notas = {}
    quantidade_moedas = {}

    # Calcula a quantidade de cada nota
    for nota in notas:
        quantidade_notas[nota] = int(valor // nota)
        valor = round(valor % nota, 2)  
    
    # Calcula a quantidade de cada moeda
    for moeda in moedas:
        quantidade_moedas[moeda] = int(round(valor // moeda))
        valor = round(valor % moeda, 2)  

    return quantidade_notas, quantidade_moedas

def main():
    # Leitura do valor
    valor = float(input())

    # Calcula as notas necessárias
    quantidade_notas, quantidade_moedas = calcular_notas_moedas(valor)

    # Impressão da quantidade de cada nota
    print("NOTAS:")
    for nota in [100, 50, 20, 10, 5, 2]:
            print(f"{quantidade_notas[nota]} nota(s) de R$ {nota:.2f}")

    # Impressão da quantidade de moedas
    print("MOEDAS:")
    for moeda in [1, 0.5, 0.25, 0.10, 0.05, 0.01]:
            print(f"{quantidade_moedas[moeda]} moeda(s) de R$ {moeda:.2f}")
            

if __name__ == "__main__":
    main()
"""
def main():
    valor = float(input())

    if valor >= 100:
        nota_100 = valor // 100
        valor = valor - nota_100 * 100

        nota_50 = valor // 50
        valor = valor - nota_50 * 50

        nota_20 = valor // 20
        valor = valor - nota_20 * 20
        
        nota_10 = valor // 10
        valor = valor - nota_10 * 10

        nota_5 = valor // 5
        valor = valor - nota_5 * 5

        nota_2 = valor // 2
        valor = valor - nota_2 * 2

    else: 
        nota_100 = 0
        nota_50 = valor // 50
        valor = valor - nota_50 * 50

        nota_20 = valor // 20
        valor = valor - nota_20 * 20
        
        nota_10 = valor // 10
        valor = valor - nota_10 * 10

        nota_5 = valor // 5
        valor = valor - nota_5 * 5

        nota_2 = valor // 2
        valor = valor - nota_2 * 2

    #moedas 

    moeda_1 = valor // 1
    valor = valor - moeda_1 * 1
    moeda_1 = float("%.2f"% moeda_1)
    valor = float("%.2f"%valor)

    moeda_050 = valor // 0.50
    valor = valor - moeda_050 * 0.50
    moeda_050 = float("%.2f"% moeda_050)
    valor = float("%.2f"%valor)

    moeda_025 = valor // 0.25
    valor = valor - moeda_025 * 0.25
    moeda_025 = float("%.2f"% moeda_025)
    valor = float("%.2f"%valor)

    moeda_010 = valor // 0.10
    valor = valor - moeda_010 * 0.10
    moeda_010 = float("%.2f"% moeda_010)
    valor = float("%.2f"%valor)

    moeda_005 = valor // 0.05
    valor = valor - moeda_005 * 0.05
    moeda_005 = float("%.2f"% moeda_005)
    valor = float("%.2f"%valor)

    moeda_001 = valor * 100
    moeda_001 = float("%.2f"% moeda_001)
    valor = float("%.2f"%valor)

    print("NOTAS:")
    print("{} nota(s) de R$ 100.00".format(int(nota_100)))
    print("{} nota(s) de R$ 50.00".format(int(nota_50)))
    print("{} nota(s) de R$ 20.00".format(int(nota_20)))
    print("{} nota(s) de R$ 10.00".format(int(nota_10)))
    print("{} nota(s) de R$ 5.00".format(int(nota_5)))
    print("{} nota(s) de R$ 2.00".format(int(nota_2)))

    print("MOEDAS:")
    print("{} moeda(s) de R$ 1.00".format(int(moeda_1)))
    print("{} moeda(s) de R$ 0.50".format(int(moeda_050)))
    print("{} moeda(s) de R$ 0.25".format(int(moeda_025)))
    print("{} moeda(s) de R$ 0.10".format(int(moeda_010)))
    print("{} moeda(s) de R$ 0.05".format(int(moeda_005)))
    print("{} moeda(s) de R$ 0.01".format(int(moeda_001)))
main()