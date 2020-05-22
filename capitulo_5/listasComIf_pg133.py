ingredientes = ['calabreza','tomate','mussarela']

for i in ingredientes:
    if i == 'tomate':
        print('desculpe mas nao temos tomate no momento')
    else:
        print('adicionado ' + i + '.')
print('\n\n')


#VERIFICANDO SE UMA LISTA ESTA VAZIA ===========================================

pedido = []
if pedido:
    for i in pedido:
        print('adicionado',i)
else:
    print('tem certeza que quer uma pizza simples')
print('\n\n')

#USANDO VARIAS LISTAS =========================================================

estoque_ingredientes = ['cogumelos', 'milho', 'calabreza',
                       'mussarela', 'catupiry', 'frango']

solicitado = ['calabreza','queijo extra','catupiry']

for i in solicitado:
    if i in estoque_ingredientes:
        print('adicionados ' + i)
    else:
        print('O ingrediente ' +i+ ' nao se encontra no estoque')
print('\n\n')
