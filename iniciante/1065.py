# Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.

# Entrada
# O arquivo de entrada contém 5 valores inteiros quaisquer.

# Saída
# Imprima a mensagem conforme o exemplo fornecido, indicando a quantidade de valores pares lidos.

def main():
    
    valores = []
    pares = []

    while True:
        try:
            valores.append(float(input()))
        except ValueError:
            print("Você não digitou um número válido")
            
        if len(valores) >= 5:
            break

    for valor in valores:
        if valor % 2 == 0:
            pares.append(valor)

    print(f"{len(pares)} valores pares")

main()