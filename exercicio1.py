#Desenvolva um algoritmo que solicite ao usuario o preço de um produto e um percentual de desconto
#a ser aplicado a ele. Calcule e exiba o valor do desconto e o preço final do produto.

preco = float(input('Digite o preço do produto: '))
p = float(input('Digite o percentual de desconto: '))

valor_desc = preco*(p/100)
preco_final = preco-valor_desc

print('O valor do desconto é de {}% e o preço final é R${}'.format(valor_desc,preco_final))