# Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o lado A representa o maior dos 3 lados. A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos, sempre escrevendo uma mensagem adequada:

# se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
# se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
# se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
# se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
# se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
# se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES
# Entrada
# A entrada contem três valores de ponto flutuante de dupla precisão A (0 < A) , B (0 < B) e C (0 < C).

# Saída
# Imprima todas as classificações do triângulo especificado na entrada.

def main():

    x, y, z = input().split()
    x = float(x)
    y = float(y)
    z = float(z)

    valores_originais = [x, y, z]

    # Ordenar os valores manualmente usando if-else
    if x >= y >= z:
        valores_ordenados = [x, y, z]
    elif x >= z >= y:
        valores_ordenados = [x, z, y]
    elif y >= x >= z:
        valores_ordenados = [y, x, z]
    elif y >= z >= x:
        valores_ordenados = [y, z, x]
    elif z >= x >= y:
        valores_ordenados = [z, x, y]
    else:  # valor3 <= valor2 <= valor1
        valores_ordenados = [z, y, x]

    x = valores_ordenados[0]
    y = valores_ordenados[1]
    z = valores_ordenados[2]

    if x >= (y + z):
        print("NAO FORMA TRIANGULO")

    elif x*x == (y*y + z*z):
        print("TRIANGULO RETANGULO")

    elif x*x > (y*y + z*z):
        print("TRIANGULO OBTUSANGULO")
        if x == y or y == z or x == z:
            print("TRIANGULO ISOSCELES")

    elif x*x < (y*y + z*z):
        print("TRIANGULO ACUTANGULO")
        if x == y == z:
            print("TRIANGULO EQUILATERO")
        elif x == y or y == z or x == z:
            print("TRIANGULO ISOSCELES")

    elif x == y == z:
        print("TRIANGULO EQUILATERO")

    elif x == y or y == z or x == z:
        print("TRIANGULO ISOSCELES")
    
main()
