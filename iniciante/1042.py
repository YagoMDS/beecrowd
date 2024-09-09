# Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.

# Entrada
# A entrada contem três números inteiros.

# Saída
# Imprima a saída conforme foi especificado.


def main():

    x, y, z = input().split()
    x = int(x)
    y = int(y)
    z = int(z)

  
# Armazenar os valores originais
    valores_originais = [x, y, z]

    # Ordenar os valores manualmente usando if-else
    if x <= y <= z:
        valores_ordenados = [x, y, z]
    elif x <= z <= y:
        valores_ordenados = [x, z, y]
    elif y <= x <= z:
        valores_ordenados = [y, x, z]
    elif y <= z <= x:
        valores_ordenados = [y, z, x]
    elif z <= x <= y:
        valores_ordenados = [z, x, y]
    else:  # valor3 <= valor2 <= valor1
        valores_ordenados = [z, y, x]

    # Exibir os valores em ordem crescente
    print("\n".join(map(str, valores_ordenados)))

    # Linha em branco
    print()

    # Exibir os valores na ordem original
    print("\n".join(map(str, valores_originais)))
main()
