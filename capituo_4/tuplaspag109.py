#Tuplas
#
#são definidas como listas, mas ao inves de usar colchetes[] usam parenteses()
dim = (200, 50)
print(dim[0],dim[1])


#mostrando tupla em um laço:
for i in dim:
    print(i)
print('\n')

#aletrando valor dentro de uma variavel em tuplas
print   ('dimensão original ',dim)
for     dime    in  dim:
     print(dime)


     

dim =   (400,150)   
print   ('dimensão modificada ',dim)
for     dime    in  dim:
    print(dime)

    

#exercicio pagina 111
#fazer uma tupla mostrar em um laço, e altera minha variaveis
eat = ('arroz', 'feijao', 'bife', 'suco')
print(eat)
           

for eats in eat:
    print(eats)

eat = ('camarao', 'picanha' )
for comer in eat:
        print(comer)
print(eat,'\n')



#outro exemplo de tuplas para assmilar
febre = ('amarela', 'suina','coronavirus')
print(febre)

for febres in febre:
    print(febres)

febre = ('35° baixa','38° alta','40° muito alta')
for i in febre:
    print(i)
print(febre)



