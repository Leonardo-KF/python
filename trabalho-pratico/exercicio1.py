while True:
    print('Entre com o nome e nota final do aluno. Digite \'S\' para sair.')
    nomeAluno = str(input('Digite o nome do aluno: ')).strip().upper()
    notaFinal = ''
    if nomeAluno == 'S':
        print('Saindo...')
        break
    elif nomeAluno.isalpha():
        while True:
            notaFinal = str(input('Digite a nota final: '))
            if notaFinal.isnumeric():
                notaFinal = float(notaFinal)
            if notaFinal == 'S':
                print('Saindo...')
                break
            else:
                print('Nota inválida, tente novamente')
            break    
    else:
        print('Nome inválido, tente novamente.')

    
    
