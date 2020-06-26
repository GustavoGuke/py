#função range() gera uma serie de numeros

print("Exemplo usando um laço. função range() gera uma serie de numeros ")
for value in range(0,5):
    print(value)
    

print('\n')
print('Exemplo usando a função list(range())')
numbers = list(range(0,5))
print(numbers,'\n')


print('neste exemplo o primeiro valor e somado com o terceiro ate chegar o valor do meio ')
print('sera ignorado alguns numero em um dado intervalo')
num1 = list(range(1,10,2))
print(num1,'\n')


print('Usando range para criar uma lista com os numeros quadrados de 1 a 10')
quad = []
for value in range(1,11):
    quad.append(value**2)
print(quad,'\n')
print('min(menor valor da lista),max(maior valor),sum(ira somar minha lista)')
print(min(quad))
print(max(quad))
print(sum(quad),'\n')



print('usando lis comprehensions, abrangendo a lista')
print('funciona do mesmo jeito apenas encurta o codigo ')
lista_abran = [value+2 for value in range(1,6)] 
print(lista_abran)





