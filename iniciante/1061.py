# Pedrinho está organizando um evento em sua Universidade. O evento deverá ser no mês de Abril, iniciando e terminando dentro do mês. O problema é que Pedrinho quer calcular o tempo que o evento vai durar, uma vez que ele sabe quando inicia e quando termina o evento.

# Sabendo que o evento pode durar de poucos segundos a vários dias, você deverá ajudar Pedrinho a calcular a duração deste evento.

# Entrada
# Como entrada, na primeira linha vai haver a descrição “Dia”, seguido de um espaço e o dia do mês no qual o evento vai começar. Na linha seguinte, será informado o momento no qual o evento vai iniciar, no formato hh : mm : ss. Na terceira e quarta linha de entrada haverá outra informação no mesmo formato das duas primeiras linhas, indicando o término do evento.

# Saída
# Na saída, deve ser apresentada a duração do evento, no seguinte formato:

# Função para converter dias, horas, minutos e segundos em segundos totais
def converter_para_segundos(dia, hora, minuto, segundo):
    return dia * 86400 + hora * 3600 + minuto * 60 + segundo

# Função para converter segundos totais de volta para dias, horas, minutos e segundos
def converter_de_segundos(total_segundos):
    dias = total_segundos // 86400
    total_segundos %= 86400
    horas = total_segundos // 3600
    total_segundos %= 3600
    minutos = total_segundos // 60
    segundos = total_segundos % 60

    return dias, horas, minutos, segundos


def main():

   # Ler a entrada
    dia_inicio = int(input().split()[1])
    hora_inicio, minuto_inicio, segundo_inicio = map(int, input().split(" : "))
    dia_fim = int(input().split()[1])
    hora_fim, minuto_fim, segundo_fim = map(int, input().split(" : "))

    # Converter o tempo de início e término para segundos
    inicio_em_segundos = converter_para_segundos(dia_inicio, hora_inicio, minuto_inicio, segundo_inicio)
    fim_em_segundos = converter_para_segundos(dia_fim, hora_fim, minuto_fim, segundo_fim)

    # Calcular a diferença em segundos
    duracao_em_segundos = fim_em_segundos - inicio_em_segundos

    # Converter a diferença de volta para dias, horas, minutos e segundos
    dias, horas, minutos, segundos = converter_de_segundos(duracao_em_segundos)

    # Exibir o resultado
    print(f"{dias} dia(s)")
    print(f"{horas} hora(s)")
    print(f"{minutos} minuto(s)")
    print(f"{segundos} segundo(s)")
    

main()