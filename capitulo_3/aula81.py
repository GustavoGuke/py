"""moto = ['honda', 'suzuki', 'yamaha', 'ducati']
print(moto)

rem_moto = 'suzuki'

moto.remove(rem_moto)
print(moto)
print('\n A ' +rem_moto.title()+' foi removida da lista')"""

print('exercicio 3_4: Fazer uma lista  e imprimir um convite ')
conv_dados = [ 'joao ', 'gabriel', 'lorena']
print(conv_dados)

for i in conv_dados: #otimizando o codigo com for
    print('Favor '+i.title()+', comparecer na reuniao!')
"""
print('favor '+conv_dados[0].title()+ ' comparecer na reuniao! ')
print('favor '+conv_dados[1].title()+' comparecer na reuniao! ')
print('favor '+conv_dados[2].title()+' comparecer na reuniao!\n ')
"""
print('\n')
print('exercicio 3_5: retirar um nome e imprimir uma menssagem dizendo pq foi removida')
conv_dados = [ 'joao', 'gabriel', 'lorena']
print(conv_dados)
print('esses são o numero de convidados ate agora',len(conv_dados))
                   
no_ir = 'joao'
conv_dados.remove(no_ir)
print(conv_dados)
print('O SR ' +no_ir.title()+ ' nao ira a reuniao!\n')


print('exercicio 3_5: Adiciona um nome na lista e imprime um mensagem a ela')
conv_dados.append('jussara')
print('favor '+conv_dados[2].title()+ ' comparecer na reuniao! ')
print (conv_dados,'\n')


print('exercicio 3_6: adc mais tres convidados (inicio,meio,fim) imprimir uma mensagem')
conv_dados.insert(0,'beto')
conv_dados.insert(3,'ceara')
conv_dados.append('dominguinho')
print(conv_dados)
for c in conv_dados:#otimizando com o laço for
    print('Favor, '+c.title()+' comparecer na reuniao! ')
print('\n')    
"""
print('favor '+conv_dados[0].title()+ ' comparecer na reuniao! ')
print('favor '+conv_dados[3].title()+' comparecer na reuniao! ')
print('favor '+conv_dados[5].title()+' comparecer na reuniao!\n ')
"""

print('exercicio 3_6: remover 4 nomes e imprimir mensagens')
popped_dados = conv_dados.pop(0)
print(popped_dados)
print('SR '+popped_dados.title()+ ' nao precisara ir mais! ')
popped_dados = conv_dados.pop(0)
print(popped_dados)
print('SR '+popped_dados.title()+ ' nao precisara ir mais! ')
popped_dados = conv_dados.pop(0)
print(popped_dados)
print('SR '+popped_dados.title()+ ' nao precisara ir mais! ')
popped_dados = conv_dados.pop(0)
print(popped_dados)
print('SR '+popped_dados.title()+ ' nao precisara ir mais! \n')

print('exercicio 3_6: imprimir mensagem para as pessoas que sobraram! ')
print('SR '+conv_dados[0].title()+ ' ainda precisa ir ! ')
print('SR '+conv_dados[1].title()+ ' ainda precisa ir ! \n')

print('exercicio 3_6: remover os 2 que sobro e mostrar a lista vazia')
del conv_dados [0]
del conv_dados [0]
print('minha lista esta vazia ', conv_dados)





