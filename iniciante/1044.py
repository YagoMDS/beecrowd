# Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos", indicando se os valores lidos são múltiplos entre si.

# Entrada
# A entrada contém valores inteiros.

# Saída
# A saída deve conter uma das mensagens conforme descrito acima.

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
