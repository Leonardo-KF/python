#Escreva um programa que pergunte a quantidade de quilômetros percorridos por um carro alugado pelo usuário, assim
#como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60
#por dia e R$0,15 por km rodado.

km_rodado = float(input('Informe a quilometragem: '))
dias_alugados = int(input('Informe quantos dias: '))

a_pagar = (km_rodado*0.15)+(dias_alugados*60)

print('O valor a pagar é de R$',a_pagar)