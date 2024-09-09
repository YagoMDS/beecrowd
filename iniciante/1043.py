# Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:

# Perimetro = XX.X

# Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem

# Area = XX.X

# Entrada
# A entrada contém três valores reais.

# Saída
# O resultado deve ser apresentado com uma casa decimal.

def main():

    a, b = input().split()
    a = int(a)
    b = int(b)

    if (a > b):
        resto = a % b
        if(resto == 0): 
            print("Sao Multiplos")
        else:
            print("Nao sao Multiplos")
    elif (b > a):
        resto = b % a
        if(resto == 0): 
            print("Sao Multiplos")
        else:
            print("Nao sao Multiplos")
    else:
        print("Nao sao Multiplos")
main()

