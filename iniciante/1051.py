# Em um país imaginário denominado Lisarb, todos os habitantes ficam felizes em pagar seus impostos, pois sabem que nele não existem políticos corruptos e os recursos arrecadados são utilizados em benefício da população, sem qualquer desvio. A moeda deste país é o Rombus, cujo símbolo é o R$.

# Leia um valor com duas casas decimais, equivalente ao salário de uma pessoa de Lisarb. Em seguida, calcule e mostre o valor que esta pessoa deve pagar de Imposto de Renda, segundo a tabela abaixo.



# Lembre que, se o salário for R$ 3002.00, a taxa que incide é de 8% apenas sobre R$ 1000.00, pois a faixa de salário que fica de R$ 0.00 até R$ 2000.00 é isenta de Imposto de Renda. No exemplo fornecido (abaixo), a taxa é de 8% sobre R$ 1000.00 + 18% sobre R$ 2.00, o que resulta em R$ 80.36 no total. O valor deve ser impresso com duas casas decimais.

# Entrada
# A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

# Saída
# Imprima o texto "R$" seguido de um espaço e do valor total devido de Imposto de Renda, com duas casas após o ponto. Se o valor de entrada for menor ou igual a 2000, deverá ser impressa a mensagem "Isento".


def calcula_imposto(valor):
    # Dicionário com as faixas de renda e as respectivas taxas de imposto
    renda = {
        (0, 2000.00): 'Isento',
        (2000.01, 3000.00): 8,
        (3000.01, 4500.00): 18,
        (4500.01, float("inf")): 28
    }

    # Verifica em qual faixa o valor se encaixa
    for faixa, taxa in renda.items():
        if faixa[0] < valor <= faixa[1]:
            return taxa
    return 0

def main():
    valor = float(input().strip())
    imposto = calcula_imposto(valor)

    if imposto == 'Isento':
        print("Isento")
    elif imposto == 8:
        # Calcula imposto para a faixa de 2000.01 a 3000.00
        if valor > 2000.00:
            taxa = 8 / 100
            valor_imposto = (valor - 2000.00) * taxa
            print(f"R$ {valor_imposto:.2f}")
    elif imposto == 18:
        # Calcula imposto para a faixa de 3000.01 a 4500.00
        if valor > 3000.00:
            imposto_8 = (1000.00) * (8 / 100)
            imposto_18 = (valor - 3000.00) * (18 / 100)
            print(f"R$ {imposto_8 + imposto_18:.2f}")
    elif imposto == 28:
        # Calcula imposto para valores acima de 4500.00
        imposto_8 = (1000.00) * (8 / 100)
        imposto_18 = (1500.00) * (18 / 100)
        imposto_28 = (valor - 4500.00) * (28 / 100)
        print(f"R$ {imposto_8 + imposto_18 + imposto_28:.2f}")

# Chama a função principal
main()