#CAPITULO 5 APRENDENDO A USAR if
"""
#com a condição if sempre que aparecer bmw ela vai formatar para que tds as letras  fiquem maiuscula.
cars = ['audi','bmw','fiat','mercedes']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
print('\n')

#expressão and retornara false se um dos testes nao passar , or retorna true se um dos testes passar.
print('jo e ja vão a cinema')
jo=17
ja=17

if jo >=18 or ja >=18:
    print('entrada liberada')
else:
    print('apenas para maiores de 18','\n')

    

    


"""
#condição if ira mostar se os nomes são iguais e mostrara uma das msg
nome = input('digite um nome: ')
nomes = input('digite outro nome: ')

minu=nome.lower()
minus=nomes.lower()

if minu == minus:
    print('Nome já ultilizado!')
    

else:
    print('gravado','\n')


