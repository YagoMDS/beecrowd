# Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

# Entrada
# O arquivo de entrada contém um valor inteiro N.

# Saída
# Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.

total = 3600
n = int(input())
hora = n // total
n %= total
minuto = int(n / 60)
segundos = n - (minuto * 60)
print(f'{hora}:{minuto}:{segundos}')


# OU PODEMOS FAZER DESTA MANEIRA 


SEGUNDOS_EM_HORA = 3600
SEGUNDOS_EM_MINUTO = 60


n = int(input("Digite o número de segundos: "))
horas = n // SEGUNDOS_EM_HORA
n %= SEGUNDOS_EM_HORA

minutos = n // SEGUNDOS_EM_MINUTO
segundos = n % SEGUNDOS_EM_MINUTO

print(f'{horas:02}:{minutos:02}:{segundos:02}')
