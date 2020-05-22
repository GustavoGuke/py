#while
'''
repetir = 'y'

while repetir =='y':
    av1= float(input('Informe AV1: '))
    av2= float(input('Informe AV2: '))
    media =  (av1+av2)/2
    if media < 6 :
        print('aluno Burro tiro apenas ', media ,'de nota')
    print('A media do aluno é {}'.format(media))
    repetir = input('Digite y caso queria calcular nova media: ')
print('Fim do Programa')    
'''


#for
qtde = int(input('Quantidade de Alunos: '))
for x in range (0,qtde,1):
    av1= float(input("Informe AV1: "))
    av2= float(input("Informe AV2: "))
    media= (av1+av2)/2
    print("Media do aluno foi de: ",media)
print('Fim')    
               
           


