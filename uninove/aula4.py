#listas metodos que pode ser usados em listas

alu = ['leonardo', 'ricardo', 'monica', 'luiza']
print(alu)
alu.append('gustavo')
print('lista com inclusao de aluno usando o (append):\n',alu,'\n')
alu.insert(2,'gil')
print('lista com inclusao de aluno usando o (insert):\n',alu,'\n')
alu.remove('ricardo')
print('lista com remoção de um aluno usando (remove):\n',alu,'\n')
alu[4]= 'leonardo'
print('lista com alteração de um aluno:\n',alu,'\n')
contador = alu.count('leonardo')
print('quantidades de alunos com o nome "leonardo" usando o (metodo count):\n',contador,'\n')
print('quantidade de elementos da lista usando (len): ',len(alu),'\n')
alu.sort()
print('lista ordenada de A a Z usando (sort):\n',alu,'\n')

if 'leonardo' in alu:
    print('usando metodo (in) para ver se elemento esta na lista')
    print('leonardo pertence a lista')
if 'kaique' not in alu:
    print('usando metodo (not in) para ver se elemento pertence a lista')
    print('kaqiue nao pertence a lista')
print(type(alu))
