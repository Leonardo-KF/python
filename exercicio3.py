# Crie uma variável que receba uma frase qualquer. Crie uma segunda variável, agora contendo a metade da string
# digitada. Imprima na tela somente os dois ultimos caracteres da segunda variavel do tipo string

frase1 = input("Digite uma frase qualquer: ")
tamanho = len(frase1)
frase2 = frase1[: int(tamanho / 2)]  # tambem pode ser feito [:tamanho//2]
print(frase2[-2:])
