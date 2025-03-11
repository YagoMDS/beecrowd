# Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores digitados foram ímpares, quantos valores digitados foram positivos e quantos valores digitados foram negativos.

# Entrada
# O arquivo de entrada contém 5 valores inteiros quaisquer.

# Saída
# Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, não esquecendo o final de linha após cada uma.

def main():
    
    valores = []
    pares = []
    impares = []
    positivo = []
    negativo = []

    while True:
        try:
            valores.append(int(input()))
        except ValueError:
            print("Você não digitou um número válido")
            
        if len(valores) >= 5:
            break

    for valor in valores:
        
        if valor % 2 == 0:
            pares.append(valor)
        elif valor % 2 == 1:
            impares.append(valor)

    for valor in valores:
        if valor > 0:
            positivo.append(valor)
        elif valor < 0:
            negativo.append(valor)

    print(f"{len(pares)} valor(es) par(es)")
    print(f"{len(impares)} valor(es) impar(es)")
    print(f"{len(positivo)} valor(es) positivo(s)")
    print(f"{len(negativo)} valor(es) negativo(s)")

main()