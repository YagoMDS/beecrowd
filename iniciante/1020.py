# Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

# Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

# Entrada
# O arquivo de entrada contém um valor inteiro.

# Saída
# Imprima a saída conforme exemplo fornecido.



dias_ano = 365
dias_mes = 30

n = int(input())

ano_int = n // dias_ano
resto_mes = n
resto_mes %= dias_ano
mes = resto_mes // dias_mes
resto_dia = resto_mes
resto_dia %= dias_mes


if(n > 0):
    print(f"{ano_int} ano(s)")
    print(f"{mes} mes(es)")
    print(f"{resto_dia} dia(s)")


# OU PODEMOS FAZER DESTA MANEIRA

# Lê o valor inteiro correspondente à idade em dias
dias_totais = int(input())

# Calcula o número de anos
anos = dias_totais // 365
dias_restantes = dias_totais % 365

# Calcula o número de meses
meses = dias_restantes // 30
dias_restantes = dias_restantes % 30

# Imprime o resultado no formato requerido
print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias_restantes} dia(s)")