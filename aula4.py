# Um cinema cobra preços diferentes para os ingressos, de acordo com a idade de uma pessoa. Se a pessoa tiver
# menos de 3 anos, o ingresso será gratuito; entre 3 e 12 anos o ingresso custará R$15; se tiver mais de 12
# anos, custará R$30.

# Escreva um laço em que você pergunte a idade aos usuários, e então lhes informe o preço do ingresso;
# Encerre o laço usando um break quando o usuário digitar 'sair'.
# Após encerrar o laço, apresente na tela o total de pessoas que compraram ingressos, o total de dinheiro
# arrecadado e a média de idade das pessoas.

print('Sistema de venda de ingressos!')
pes = ingresso =0
while True:
    idade = str(input('Digite a sua idade ("sair" encerra o programa)? ')).strip()
    if idade.isnumeric():
        idade = int(idade)
        pes += 1
        if idade < 3:
            ingresso += 0
        elif 3 <= idade <= 12:
            ingresso += 15
        else:
            ingresso += 30
        print(f'Ingresso no valor de: R${ingresso:.2f} adicionado ao carrinho com sucesso!')
        print('='*60)
    elif idade in 'SAIRsair':
        break
    else:
        print('Você digitou uma opção inválida! Tente novamente!')
print(f'O numero de ingressos comprados foi {pes}! O valor total da sua compra é: R${ingresso:.2f}')