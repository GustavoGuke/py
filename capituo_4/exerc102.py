#exercico pág 102.

#fazer uma lista e mostrar ele no lçao for
#mostrar menor num , o max num ea soma dos valores com sum()
quad = []
for value in range(1,250):
   quad.append(value)
print(quad)
print(min(quad))
print(max(quad))
print(sum(quad))
print('\n')


#Mostrar uma lista apenas com numeros impares de 1 a 20
num = list(range(1,21,2))
print(num,'\n')


#MULTIPLOS DE 3 ATE 30 
quad1 = []
for value in range(1,30):
   quad1.append(value*3)
print(quad1,'\n')


#ELEVADO AO CUBO
quad2 = []
for value in range(1,10):
   quad2.append(value**3)
print(quad2,'\n')

#USANSO LIST COMPREHENSIONS, ENCURTANDO O CODIGO ACIMA.
Quad = [value**3 for value in range(1,10)]
print(Quad)
