# O Maior
#
# Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:
#
# Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.
# Entrada
#
# O arquivo de entrada contém três valores inteiros.
# Saída
#
# Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".

a, b, c = input().split(" ")
lista = [int(a), int(b), int(c)]
maior = 0

for i in lista:
    if i > maior:
        maior = i

print(f'{maior} eh o maior')

teste = 0