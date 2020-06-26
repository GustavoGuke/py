print('Lista usada de parametro para fazer outra usando função')

# lista de designs que devem ser impressos
designs = ['iphone case', 'robot pendant', 'prototype']
completed_models = []


# simula a impressao de cada design, ate que nao haja mais nenhum.
# transfere para completed_models
while designs:
    current_design = designs.pop()

    #simula a criação de cata item
    print('Printing model: '+ current_design)
    completed_models.append(current_design)

# exibe todos os designs finaliados
print('\n The following models have been printed: ')
for models in completed_models:
    print(models)
