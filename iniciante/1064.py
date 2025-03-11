# Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos. Na próxima linha, deve-se mostrar a média de todos os valores positivos digitados, com um dígito após o ponto decimal.

# Entrada
# A entrada contém 6 números que podem ser valores inteiros ou de ponto flutuante. Pelo menos um destes números será positivo.

# Saída
# O primeiro valor de saída é a quantidade de valores positivos. A próxima linha deve mostrar a média dos valores positivos digitados.

from statistics import mean


def main():
    
    valores = []
    valores_positivos = []

    while True:
        try:
            valores.append(float(input()))
        except ValueError:
            print("Você não digitou um número válido")
            
        if len(valores) >= 6:
            break

    for valor in valores:
        if valor >= 0:
            valores_positivos.append(valor)
        

    print(f"{len(valores_positivos)} valores positivos")
    print(f"{mean(valores_positivos):.1f}")


main()

