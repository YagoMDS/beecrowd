# Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

# Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

# Entrada
# Quatro números inteiros representando a hora de início e fim do jogo.

# Saída
# Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .

def main():
    # Lê as horas e minutos de início e fim
    h1, m1, h2, m2 = map(int, input().split())

    # Valida se as horas e minutos estão dentro do intervalo permitido
    if (0 <= h1 < 24 and 0 <= m1 < 60) and (0 <= h2 < 24 and 0 <= m2 < 60):
        # Calcula o total de minutos desde o início do dia para as horas e minutos fornecidos
        inicio = h1 * 60 + m1
        fim = h2 * 60 + m2

        # Se o tempo final for menor que o tempo inicial, adiciona 24 horas (1440 minutos)
        if fim <= inicio:
            fim += 24 * 60  # Adiciona 24 horas em minutos

        # Calcula a duração total em minutos
        duracao = fim - inicio

        # Calcula horas e minutos da duração
        horas = duracao // 60
        minutos = duracao % 60

        print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")

# Chama a função principal
main()
