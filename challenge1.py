def retorna_tempo_arena_em_milisegundos(distancia,velocidade):
    d = 450
    velocidade = 340
    tempo = (d/velocidade)*1000
    print('O som será ouvido pela ultima pessoa em aproximadamente {}'.format(tempo))

retorna_tempo_arena_em_milisegundos(450,340)