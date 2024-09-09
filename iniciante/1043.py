# Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:


# Perimetro = XX.X


# Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem


# Area = XX.X

# Entrada
# A entrada contém três valores reais.

# Saída
# O resultado deve ser apresentado com uma casa decimal.

def main():

    a, b, c = input().split()
    a = float(a)
    b = float(b)
    c = float(c)

    if ((a + b > c) and (a + c > b) and (b + c > a)):
        perimetro = a + b + c
        print(f"Perimentro = {perimetro:.1f}")
    else:
        area = ((a + b) * c) / 2
        print(f"Área: {area:.1f}")

main()

