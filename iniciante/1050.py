# Leia um número inteiro que representa um código de DDD para discagem interurbana. Em seguida, informe à qual cidade o DDD pertence, considerando a tabela abaixo:

# Se a entrada for qualquer outro DDD que não esteja presente na tabela acima, o programa deverá informar:
# DDD nao cadastrado

# Entrada
# A entrada consiste de um único valor inteiro.

# Saída
# Imprima o nome da cidade correspondente ao DDD existente na entrada. Imprima DDD nao cadastrado caso não existir DDD correspondente ao número digitado.

def busca_ddd(valor):

    ddd = {
        61 : 'Brasilia',
        71 : 'Salvador',
        11 : 'Sao Paulo',
        21 : 'Rio de Janeiro',
        32 : 'Juiz de Fora',
        19 : 'Campinas',
        27 : 'Vitoria',
        31 : 'Belo Horizonte',
    }

    if valor in ddd:
        return ddd[valor]
    else:
        return ("DDD nao cadastrado")

def main():

    valor = int(input().strip())
    ddd = busca_ddd(valor)

    print(ddd)

main()