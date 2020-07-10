# Exercicio 10.3
# abrir um arquivo e escrever nele

'''
nome = input('digite seu nome: ')
filename = 'arquivosTxt/exercicio_pg266.txt'
# escrever no arquivo
with open(filename, 'w') as f:
    f.write(nome)




# abrir o arquivo apenas leitura
with open(filename) as f:
    line = f.readlines()
for i in line:
    if nome in i:
        print('seja bem vindo: ', nome)





# Exercicio 10.4
# escrver nomes em um arquivo sem apagar os que ja esta nele

filename = 'arquivosTxt/exercicio_pg266_10.4.txt'

while True:
    nome = input('digite seu nome: ')
    parar_laco = ''
    parar_laco += nome
    
    if parar_laco != '.':
        with open(filename, 'a') as f:
            f.write(nome +'\n')
        print('Nome arquivado: ',nome)

    if parar_laco == '.':
        break
'''

# exercicio 10.5
# capturar respostas e guardalas em um arquivo


filename = 'arquivosTxt/exercicio_pg266_10.5.txt'

while True:
    print('Para sair coloque um ponto final na segunda pergunta:\n')
    msg = 'Respondeu a enquete:'
    nome = input('digite seu nome: ')
    stack = input('digite o que vc estuda: ')

    with open(filename, 'a') as f:
        f.write(msg)
        f.write('\n Nome: '+nome+'\n')
        f.write('\t Estuda: '+stack+'\n')

    
    if '.' in stack:
        break
    
        


























