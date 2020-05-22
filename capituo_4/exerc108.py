#EXERCICIO PAGINHA 108

#FAZER UM ALISTA E APRESENTAR OS 3 PRIMEIROS ITENS.
#APRESENTAR ITENS DO MEIO E DO FINAL.
aprend = ['html','css','php','java script','python','java','sql','mysql','c']
print(aprend)
print(aprend[0:3])
print(aprend[3:6])
print(aprend[6:9])
print('\n')


#COPIAR A LISTA E FAZER ALTERAÇOES PARA VER SE ELAS SAO DISTINTAS.
friend_ap = aprend [:]
print(friend_ap)
friend_ap.remove('java script')
aprend.remove('c')
print(friend_ap)
print(aprend)
print('\n')


#FAZER UM LAÇO PARA MOSTAR UMA DAS LISTAS.
for i in aprend:
    print(i.title())

