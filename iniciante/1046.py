# Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.

# Entrada
# A entrada contém dois valores inteiros representando a hora de início e a hora de fim do jogo.

# Saída
# Apresente a duração do jogo conforme exemplo abaixo.

def main():
    dia = 24
    h1, h2 = input().split()
    h1 = int(h1)
    h2 = int(h2)

    if (h1 >= 0) and (h2 >= 0):
        if (h1 < dia) and (h2 < dia):
            if h1 >= h2:
                jogo = (dia - h1) + h2
                print(f"O JOGO DUROU {jogo} HORA(S)")
            else:
                jogo = h2 - h1
                print(f"O JOGO DUROU {jogo} HORA(S)")
main()


