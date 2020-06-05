import time
print('While roda enquanto uma condição for verdadeira')

cont = 1
while cont <= 5:
    print(cont)
    cont = cont + 1
print('\n')
#=============================================================================

print('deixando o usuario decidir a saida do programa')
entrada = 'Digite algo e eu repetirei ate vc dizer sair: '
repetir = ''
while repetir != 'sair':
    repetir = input(entrada)
    #print(repetir)
    if repetir != 'sair':
        print(repetir)
print('\n')   



'''
Exercicios: 
num = int(input('digite um numero: '))
ate = int(input('ele vai ate: '))
passo = int(input('digite o passso: '))
for i in range(num,ate,passo):
    time.sleep(2)
    print(i)




num1 = int(input('digite o numero que queira saber a tabuada: '))
cont = 1
while cont <= 9:
    tabuada = num1*cont
    print(num1, 'x', cont, '=', tabuada)
    cont = cont + 1


num2 = int(input('digite o numero que queira saber a tabuada: '))

for i in range(1,10):
    tabu = num2 * i
    print(num2, 'x', i, '=', tabu)

'''
#==================================== ate pg174 =============================
