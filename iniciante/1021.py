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


def main():
    # Leitura do valor
    valor = float(input())

    # Calcula as notas necessárias
    quantidade_notas = calcular_notas(valor)

    # Impressão do valor lido
    print(valor)

    # Impressão da quantidade de cada nota
    for nota in [100, 50, 20, 10, 5, 2, 1]:
        print("NOTAS:")
        print(f"{quantidade_notas[nota]} nota(s) de R$ {nota},00")

if __name__ == "__main__":
    main()

    teste