def main():
    a, b, c, d = input().split()

    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)

    resto = a % 2

    if (b > c) and (d > a) and (c + d > a + b) and (c >= 0) and (resto == 0):
        print("Valores aceitos")
    else:
        print("Valores nao aceitos")

main()
