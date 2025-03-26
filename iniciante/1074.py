# Leia um valor inteiro N. Este valor será a quantidade de valores que serão lidos em seguida. 
# Para cada valor lido, mostre uma mensagem em inglês dizendo se este valor lido é par (EVEN), ímpar (ODD), 
# positivo (POSITIVE) ou negativo (NEGATIVE). No caso do valor ser igual a zero (0), embora a descrição correta 
# seja (EVEN NULL), pois por definição zero é par, seu programa deverá imprimir apenas NULL.

# Entrada
# A primeira linha da entrada contém um valor inteiro N(N < 10000) que indica o número de casos de teste. 
# Cada caso de teste a seguir é um valor inteiro X (-107 < X <107).

# Saída
# Para cada caso, imprima uma mensagem correspondente, de acordo com o exemplo abaixo. Todas as letras deverão ser
# maiúsculas e sempre deverá haver um espaço entre duas palavras impressas na mesma linha.

def main():

    qtd_valores = int(input())
    i = 1

    while True:

        valor = int(input())
        i += 1

        if valor > 0 and valor % 2 == 0:
            print("EVEN POSITIVE")
        elif valor > 0 and valor % 2 == 1:
            print("ODD POSITIVE")
        if valor < 0 and valor % 2 == 0:
            print("EVEN NEGATIVE")
        elif valor < 0 and valor % 2 == 1:
            print("ODD NEGATIVE")
        elif valor == 0:
            print("NULL")

        if i <= qtd_valores:
            continue
        else:
            break

main()

# Forma curta
# N = int(input())  # Lê a quantidade de casos de teste

# for _ in range(N):
#     X = int(input())  # Lê o número a ser analisado
    
#     if X == 0:
#         print("NULL")  # Caso seja zero, imprime NULL
#     else:
#         resultado = "EVEN" if X % 2 == 0 else "ODD"  # Verifica se é PAR ou ÍMPAR
#         resultado += " POSITIVE" if X > 0 else " NEGATIVE"  # Verifica se é POSITIVO ou NEGATIVO
#         print(resultado)