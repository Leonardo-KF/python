while True:
    print('Entre com o nome e nota final do aluno. Digite \'S\' para sair.')
    nomeAluno = input('Digite o nome do aluno: ')
    if nomeAluno == 'S':
        print('Saindo...')
        break
    elif nomeAluno.isalpha() == True and nomeAluno.isspace() == False:
        print(f'Nome do aluno: {nomeAluno}')
    else:
        print('Nome inválido, tente novamente.')
    notaFinal = input('Digite a nota final: ')
    if notaFinal.isalpha() == True and notaFinal == 'S':
        print('Saindo...')
        break
    elif notaFinal.isalnum() == True:
        print('Nota inválida, tente novamente')
    else:
        print(f'Nota final: {notaFinal:.1f}')
