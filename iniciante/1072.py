# Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida.
# Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo, mostrando essas informações.

# Entrada
# A primeira linha da entrada contém um valor inteiro N (N < 10000), que indica o número de casos de teste.
# Cada caso de teste a seguir é um valor inteiro X (-107 < X <107).
 

# Saída
# Para cada caso, imprima quantos números estão dentro (in) e quantos valores estão fora (out) do intervalo.

def main():

    n = int(input())
    lista = []
    saida = 0
    entrada = 0
    
    while len(lista) < n:
        lista.append(int(input()))

    for i in lista:
        
        if i < 10 or i > 20:
            saida += 1
        else:
            entrada += 1
    
    print(f"{entrada} in")
    print(f"{saida} out")

main()

# # Outra formar de ser feito

# def contar_numeros_no_intervalo():
#     # Lendo o número de casos de teste
#     n = int(input())

#     # Inicializando contadores
#     dentro = 0
#     fora = 0

#     # Lendo os valores e contando quantos estão dentro e fora do intervalo [10,20]
#     for _ in range(n):
#         x = int(input())
#         if 10 <= x <= 20:
#             dentro += 1
#         else:
#             fora += 1

#     # Exibindo os resultados
#     print(f"{dentro} in")
#     print(f"{fora} out")

# # Chamando a função principal
# contar_numeros_no_intervalo()