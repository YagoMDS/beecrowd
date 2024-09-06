def main():
    cod1 = 4.0
    cod2 = 4.5
    cod3 = 5.0
    cod4 = 2.0
    cod5 = 1.5

    valor1, valor2 = input().split()
    valor1 = float(valor1)
    valor2 = float(valor2)

    if valor1 == 1:
        total = cod1 * valor2
        print(f'Total: R$ {total:.2f}')
    elif valor1 == 2:
        total = cod2 * valor2
        print(f'Total: R$ {total:.2f}')
    elif valor1 == 3:
        total = cod3 * valor2
        print(f'Total: R$ {total:.2f}')
    elif valor1 == 4:
        total = cod4 * valor2
        print(f'Total: R$ {total:.2f}')
    elif valor1 == 5:
        total = cod5 * valor2
        print(f'Total: R$ {total:.2f}')
main()