### EXERCÍCIO 1 

#### Escreva um programa que leia o nome de um aluno e sua nota final. Em seguida, informe o conceito conforme a tabela abaixo. A saída do programa deve exibir na tela uma frase com o padrão descrito a seguir: 

Nome do aluno: Fábio José 

Nota final: 73.4 

Frase a ser exibida: O aluno Fabio José tirou nota 3.5 e se enquadra no conceito D  

Nota            | Conceito
-------         |:-------: 
de 0,0 a 2,9    | E
de 3,0 a 4,9    | D
de 5,0 a 6,9    | C
de 7,0 a 8,9    | B
de 9,0 a 10,0   | A

#### Todos os dados devem ser lidos do teclado, sendo que o nome do aluno é uma string e a nota final é um número real. Não é necessário armazenar os dados em uma estrutura de dados, basta imprimir na tela.  

#### Coloque todo o seu programa dentro de um laço de repetição e faça-o se encerrar quando uma determinada condição for satisfeita. A condição fica a seu critério, como por exemplo, encerrar o programa ao digitar a palavra sair, ou então uma nota inválida.  

#### Imprima na tela um teste do seu programa utilizando o seu nome e os dois últimos dígitos do seu RU para a nota.  
---

### EXERCÍCIO 2 

#### Faça uma função que receba o nome e sobrenome de uma pessoa e retorne a primeira letra de seu nome e seu sobrenome, concatenando com a string @algoritmos.com.br. No algoritmo principal, deverá ser apresentada a mensagem ao usuário contendo seu nome completo e seu e-mail. Imprima na tela um teste do seu programa utilizando o seu nome e sobrenome concatenado com os dois últimos dígitos do seu RU. 

Ex.: Sra. Luciane Kanashiro, seu e-mail é lkanashiro16@algoritmos.com.br.  

---  

### EXERCÍCIO 3 

#### Um canal de jogos do youtube está fazendo um sorteio para angarias doações para pessoas em situação de vulnerabilidade social. A cada 10 reais doados, o nome da pessoa é inserido em uma lista de sorteio. Por exemplo: 

Ruth doou 20,00 

Maria doou 30,00 

Fernando doou 50,00 

#### A lista de sorteio estará com os valores: 

`ListaSorteio = [‘Ruth’, ‘Ruth’, ‘Maria’, ‘Maria’, ‘Maria’, ’Fernando’, ’Fernando’, ’Fernando’, ’Fernando’, ’Fernando’]` 

#### Implemente um programa para cadastrar o nome das pessoas que doaram. O programa deve embaralhar a lista, sortear o ganhador e imprimir seu nome. 

#### Imprima na tela um teste do seu programa utilizando como primeiro doador o seu nome e os dois últimos dígitos do seu RU para o valor doado. Não se esqueça de imprimir também a lista de sorteio.  
---

### EXERCÍCIO 4 

#### Considere a tabela a seguir referente a produtos armazenados em um depósito, em que são considerados o estoque atual de cada produto e o estoque mínimo necessário.  

Código|Estoque|Mínimo
:--:  |:--:   |:--:
<span style="color:red">1</span>     |<span style="color:green">35</span>     |<span style="color:blue">20</span>
5     |75     |50
2     |43     |45
3     |26     |18
20    |35     |20  

#### Armazene as informações acima em uma estrutura de lista com dicionário, substituindo a primeira linha com os dados: no campo código coloque o primeiro digito do seu RU, no estoque os dois dígitos seguintes de seu RU, e no campo mínimo os dois últimos dígitos do seu RU. Por exemplo, tendo o RU: <span style="color:red">1</span><span style="color:green">23</span>4<span style="color:blue">56</span> 

#### As informações devem ser inseridas no dicionário via teclado. Ao digitar o código 0 (zero), o programa interrompe a leitura e se encerra. Ordene os produtos em ordem crescente de código. Imprima na tela um teste do seu programa usando como primeiro cadastro o primeiro digito do seu RU, como estoque os dois dígitos seguintes de seu RU, e como mínimo os dois últimos dígitos do seu RU.