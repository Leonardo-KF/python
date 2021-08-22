# Escreva as seguintes expressões booleanas:

# O somatório de  2 com 2 é menor que 4
#print(2 + 2 < 4)

# O valor 7//3 é igual a 1+1
#print(7//3 == 1 + 1)

# A soma de 3 elevado ao quadrado com 4 elevado ao quadrado é igual a 25
#print(3**2 + 4**2 == 25)

# A soma de 2, 4 e 6 é maior que 12
#print(2+4+6 > 12)

# 1387 é divisível por 19
#print(1387 % 19 == 0)

# 31 é par
#impar = 'é impar'
#par = 'é par'
#num = 31
#if num % 2 == 0:
#    print(par)
#else:
#    print(impar)

# O menor valor entre 34, 29 e 31 é menor que 30
#num = 30
#n1 = 34
#n2 = 29
#n3 = 31
#if n1<n2 and n1<n3 and n1<num:
#    menor = n1
#    print('o menor numero é', menor)
#elif n2<n1 and n2<n3 and n2<num:
#    menor = n2
#    print('o menor numero é', menor)
#else:
#    menor = n3
#    print('o menor numero é', menor)

# Faça um algoritmo que receba 3 valores representando os lados de um triângulo, fornecidos pelo usuário.
# Verifique se os valores formam um triângulo e classifique como:
# a) Equilátero (3 lados iguais)
# b) Isósceles (2 lados iguais)
# c) Escaleno (3 lados diferentes)
ladoA = input('Digite o tamanho do lado A: ')
ladoB = input('Digite o tamanho do lado B: ')
ladoC = input('Digite o tamanho do lado C: ')
if ladoA or ladoB or ladoC == 0:
    print('Não pode ser zero, tente novamente')
    ladoA = input('Digite o tamanho do lado A: ')
    ladoB = input('Digite o tamanho do lado B: ')
    ladoC = input('Digite o tamanho do lado C: ')
else:
    if ladoA >= ladoB + ladoC or ladoB >= ladoC + ladoA or ladoC >= ladoA + ladoB:
        print('Lado grande demais, tente novamente')