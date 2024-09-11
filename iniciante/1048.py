#  empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:


# Salário	                    Percentual de Reajuste
# 0 - 400.00                            15%                                        
# 400.01 - 800.00                       12%                           
# 800.01 - 1200.00                      10%
# 1200.01 - 2000.00                     7%
# Acima de 2000.00                      4%


# Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.

# Entrada
# A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

# Saída
# Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste (ambos devem ser apresentados com 2 casas decimais) e o percentual de reajuste ganho, conforme exemplo abaixo.

def obter_reajuste(valor):
    descontos = {
        (0, 400.00): 15,
        (400.01, 800.00): 12,
        (800.01, 1200.00): 10,
        (1200.01, 2000.00): 7,
        (2000.01, float('inf')): 4,
    }

    for faixa, desconto in descontos.items():
        if faixa[0] <= valor <= faixa[1]:
            return desconto
    return 0

def main():

    salario = float(input())
    percentual_reajuste = obter_reajuste(salario)
    reajuste_ganho = salario * (percentual_reajuste / 100)
    novo_salario = salario + reajuste_ganho
    
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {reajuste_ganho:.2f}")
    print(f"Em percentual: {percentual_reajuste:.0f} %")
main()