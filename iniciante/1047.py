# Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

# Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

# Entrada
# Quatro números inteiros representando a hora de início e fim do jogo.

# Saída
# Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .

def main():
    dia = 24
    minuto = 60
    h1, m1, h2, m2 = input().split()
    h1 = int(h1)
    h2 = int(h2)
    m1 = int(m1)
    m2 = int(m2)

    if (h1 >= 0 and m1 >= 0) and (h2 >= 0 and m2 >= 0):
        if (h1 < dia and m1 < minuto) and (h2 < dia and m2 < minuto):
            if h1 >= h2 and m1 >= m2:
                jogo = (dia - h1) + h2
                jogomin = m1 - m2
                print(f"O JOGO DUROU {jogo} HORA(S) E {jogomin} MINUTOS(S)")
            else:
                jogo = h2 - h1
                if m1 > m2:
                    jogomin = (minuto - m1) + m2
                    print(f"O JOGO DUROU {jogo} HORA(S) E {jogomin} MINUTOS(S)")
                elif m1 < m2:
                    jogomin = m2 - m1
                    print(f"O JOGO DUROU {jogo} HORA(S) E {jogomin} MINUTOS(S)")
main()
