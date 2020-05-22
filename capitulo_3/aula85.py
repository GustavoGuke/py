#lição aula pag 85

print(' 1°:Fazer uma lista com 5 paises e imprimir')

cid = ['Paris', 'Napoli', 'Aruja', 'Zambia', 'Bologna']
print(cid,'\n')
print('° Modificar a lista em ordem alfabética usando Sorted()')
print(sorted(cid))
print(cid,'\n')


print('° inverte a lista mas não a deixa em ordem alfabetica, reverse()')
cid.reverse()
print(cid,'\n')

print('° inverte a lista mostrar que pode voltar a lista antiga, reverse()')
cid.reverse()
print(cid,'\n')

print('° ultilizar o metodo sort() para alterar a lista alfabeticamente.ultilizar o reverse=TRue')
cid.sort()
print(cid)
cid.sort(reverse=True)
print(cid,'\n')

print('função len() mostra o tamanho da lista')
print('minha lista tem ',len(cid), 'cidades')


