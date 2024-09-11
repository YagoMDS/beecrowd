# Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, da esquerda para a direita.  Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.

# Entrada
# A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a figura acima, com todas as letras minúsculas.

# Saída
# Imprima o nome do animal correspondente à entrada fornecida.


def main():

    p1 = input().strip()
    p2 = input().strip()
    p3 = input().strip()

    if p1 == 'vertebrado':
        if p2 == 'ave':
            if p3 == 'carnivoro':
                print("aguia")
            elif p3 == "onivoro":
                print("pomba")
        elif p2 =='mamifero':
            if p3 == 'onivoro':
                print("homem")
            elif p3 == 'herbivoro':
                print("vaca")
    elif p1 == 'invertebrado':
        if p2 == 'inseto':
            if p3 == 'hematofago':
                print("pulga")
            elif p3 == "herbivoro":
                print("lagarta")
        elif p2=='anelideo':
            if p3 == 'hematofago':
                print("sanguessuga")
            elif p3 == 'onivoro':
                print("minhoca")
    else:
        return 0
main()