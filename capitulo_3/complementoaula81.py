"""
#Concatenação recebe duas variaveis depois concatena elas:


#Exemplo_1: criar mensagem usando concatenacao com base em um valor de uma lista.
print('Usuario ira colocar nome e depois sera emitido uma mensagem concatenando o nome e sobre nome.')
name = input ("Digite seu Nome: ")    
last_name = input ("Digite seu Sobre nome: ")
dado = name +' '+ last_name
print(dado.upper(),'\n')

print('fazer uma lista e imprimir uma mensagem pegando um item da lista com o nome do usuario.')
bike = ['pequena', 'media', 'grande'] #listas
print(bike)
message = (" A primeira bike de ", dado, "era " +bike[0]+".") 
print (message,"\n")

print('pegar um item da lista jogando a posicao [2] ')
print(bike[2].title(),'\n') #mostra [a posicao dentro da lista]

print('usando o laco para percorrer minha lista')
for dado in bike:     # laço para percorrer a lista
    print(dado.title(),'\n')

print('acrescentando um item na lista com o metodo append')    
bike.append('tricicclo')  # append() acrescenta no final insert() acrescenta no inicio.
print(bike,'\n')





"""
#Exemplo_2: fazer uma lista vazia e adc itens a ela.

print('fazer uma lista vazia e o usuario ira adc um item a ela')
lista = []    
dado =  (input("adicione um dado: "))
lista.append(dado) # insere um dado
print(lista,'\n')

print('insere um dado com o append e insert')
lista.insert(0, 'bola') #insere um dado
lista.append('chuteira')
print(lista,'\n')

print('remove um item da lista com o metodo pop() e depois imprima o item.' )
popped_lista =  lista.pop(1) #deleta um dado , mas conseguimos trabalhar com ele.
print(popped_lista)
lista.remove('bola') # remove um dado que eu quiser na lista.
print('o dado que foi retirado e ' +popped_lista+'.','\n')
print('Foi retirado da lista a bola e '+popped_lista+', ', ' apenas ',lista, ' sobrou .','\n')
print(lista)

print('deleta um item na lista com o metodo del')
del lista[0] # deleta uma posicao conhecida
print('imprimindo minha lista vazia depois de usar o metodo del ',lista)


  


  
    
