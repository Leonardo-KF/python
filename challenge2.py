# Um show organizado, com pessoas verificando ingressos, e os seguranças olhando os participantes foi feito
# com o público de p pessoas (suponha que pode ser, por exemplo, 2.749).Para as pessoas entrarem, a média de
# tempo entre entregar o ingresso e poder acessar a área dos shows é de s segundos (suponha, por exemplo, 50).
#
# Para agilizar a entrada, a produção do evento disponibilizou n portões de entrada (suponha 8).
# Qual o tempo mínimo, em minutos, para que todos os participantes entrem completamente na área dos shows?


def retorna_tempo_minimo_em_minutos(p, s, n):
    from math import ceil

    pe = 2749
    s = 50
    po = 8
    tempo_minimo = ((pe * s) / po) / 60
    print(ceil(tempo_minimo))


retorna_tempo_minimo_em_minutos(2749, 50, 8)
