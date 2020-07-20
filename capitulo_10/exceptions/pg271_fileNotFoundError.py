print('Erro proposital')

'''
filename = 'txt/alice.txt'

# tratando o erro
try:
    with open(filename) as f:
        file = f.read()
except FileNotFoundError:
    msg = 'Sorry, the file '+ filename +' does not exist! '
    print(msg)
else:
    # expandir o exemplo para ver como o tratamento de erros
    # pode ajudar quando trabalhamos com mais de um arquivo.
    words  = file.split()
    num_words = len(words)
    print('o arquivo ', filename,' tem ',str(num_words), ' palavras')
    print('metodo split devolve uma lista:\n',words)
print('...\n')

#=============================================================================
'''

# função feita para fazer mais testes
def count_word(filename):
    """ Conta o numero aproximado de palavras em um arquivo """

    try:
        with open(filename) as f:
            file = f.read()
    except FileNotFoundError:
        # omitir o erro para o usuario nao o ve-lo
        pass
        #msg = 'Sorry, the file '+ filename +' does not exist! '
        #print(msg)
    else:
        # expandir o exemplo para ver como o tratamento de erros
        # pode ajudar quando trabalhamos com mais de um arquivo.
        words  = file.split()
        num_words = len(words)
        print('o arquivo ', filename,' tem ',str(num_words), ' palavras')
        print('metodo split devolve uma lista:\n',words)
        print('...\n')

filename = ['txt/alice.txt', 'txt/dia.txt', 'txt/mes.txt', 'txt/ano.txt', 'fileNot.txt']
for file in filename:
    count_word(file)



