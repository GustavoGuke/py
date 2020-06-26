print('Exercicio 8.9')
print('Make a list and pass it to function')

# Listas que servirao de parametro
magic = ['cris angel', 'dynamo', 'lance burton', 'david blaine']
show_news = []

# função para mostar a lista
def show_magic(show):
    for i in show:
        print('Magic famous: ' + i)

# chamando função
show_magic(magic)
print('...\n')

print('start with the previous program and pass the information to another list')


# Função que ira pegar os dados de uma e passar para outra
def make_greet(magic, show_news):
    while magic:
        big_magic = magic.pop()

        show_news.append(big_magic)
    for i in show_news:
        print('The big: ' + i)


make_greet(magic, show_news)
print('Modified list' + magic)

# Chamando a função e passando a ela uma cópia em vez da lista original a lista não sera alterada.
# make_greet(magic[:], show_news)

