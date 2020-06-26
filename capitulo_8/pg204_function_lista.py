print('Refatorando o codigo "pg203_lista.py"')

#função ira receber como parametro duas listas e passara os dados de uma para outra
def modelo3d(design, models):
    while design:
        fazendo = design.pop()
        print('Printed: '+ fazendo)
        models.append(fazendo)
        
#função que ira mostrar os dados passados 
def mostrar(models):
    for i in models:
        print(i)

# listas
design = ['iphone case', 'robot', 'prototype']
models = []

# chamando as funções
# [:] chama a minha função mas passa a ela uma copia da minha lista.
modelo3d(design[:],models)
print('\n')
mostrar(models)
