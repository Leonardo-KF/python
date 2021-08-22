# Um cinema cobra preços diferentes para os ingressos, de acordo com a idade de uma pessoa. Se a pessoa tiver
# menos de 3 anos, o ingresso será gratuito; entre 3 e 12 anos o ingresso custará R$15; se tiver mais de 12
# anos, custará R$30.

# Escreva um laço em que você pergunte a idade aos usuários, e então lhes informe o preço do ingresso;
# Encerre o laço usando um break quando o usuário digitar 'sair'.
# Após encerrar o laço, apresente na tela o total de pessoas que compraram ingressos, o total de dinheiro
# arrecadado e a média de idade das pessoas.

ingresso = [0,15,30]
counter = 0

for i in ingresso:
    pergunta = int(input('Qual sua idade: '))
    if pergunta < 3:
        print('')