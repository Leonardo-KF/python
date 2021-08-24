while True:
    nomeAluno = str(input('Insira o nome do aluno: '))
    if nomeAluno.isalpha() == True and not(nomeAluno.isspace()) == True:
        print(f'Nome do aluno: {nomeAluno}')
    else:
        print('Nome inválido, digite novamente.')
    notaFinal = input('Digite a nota final do aluno: ')
    break
    if not(notaFinal.isspace()) == True:
            print('Nota Inválida, digite novamente')
    else:
            print(f'Nota final: {notaFinal}')