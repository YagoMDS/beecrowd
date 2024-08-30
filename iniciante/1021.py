def calcular_notas(valor):
    # Notas disponíveis
    notas = [100, 50, 20, 10, 5, 2, 1]
    quantidade_notas = {}

    # Calcula a quantidade de cada nota
    for nota in notas:
        quantidade_notas[nota] = valor // nota
        valor %= nota

    return quantidade_notas

def calcular_moedas(valor):
    moedas = [1.0, 0.50, 0.25, 0.10, 0.05, 0.01]
    for moeda in moedas:
        quantidade_moedas = {}
        quantidade_moedas[moeda] = valor // moeda
        valor %= moeda

    return quantidade_moedas
def main():
    # Leitura do valor
    valor = float(input())

    # Calcula as notas necessárias
    quantidade_notas = calcular_notas(valor)
    # Impressão do valor lido
    print(valor)

    quantidade_moedas = calcular_moedas(valor)
    print(valor)
    
    

    # Impressão da quantidade de cada nota
    for nota in [100, 50, 20, 10, 5, 2, 1]:
        print(f"{quantidade_notas[nota]} nota(s) de R$ {nota},00")

    for moeda in [1.0, 0.50, 0.25, 0.10, 0.05, 0.01]:
        print(f"{quantidade_moedas[moeda]} nota(s) de R$ {moeda}")

if __name__ == "__main__":
    main()