#aula 86 tratamento de erros:

mot = ['suzuki', 'yamaha', 'xre', 'honda']
print(mot[-1])
print(len(mot))
print('lista len ira mostrar o tamanho , [-1] ira mostrar o ultimo dado.','\n')

mot.append('fan')
print(mot)
print(sorted(mot))
print(' append() ira acrescentar um dado, sorted() ira mostrar em ordem alfabetica','\n')


mot.reverse()
print(mot)
mot.reverse()
print(mot,)
print(' reverse inverte a lista .','\n')


poped_del = mot.pop(1)
print(mot)
print(poped_del)
print('pop() ira tirar um item da lista','\n')


mot.insert(2,'ducati')
print(mot)
mot.sort()
print(mot)
print(mot[-1])
print('insert ira inserir um item , metodo sort() ira  deixa em ordem alfabetica definitivo','\n')
