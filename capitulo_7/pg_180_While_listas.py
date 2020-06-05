print('While em listas')

usuarios_novos = ['Bia', 'jose', 'sandro','gustavo']
usuarios_confirmados = []

while usuarios_novos:
    usuario_atual = usuarios_novos.pop()
    print('Verificando',usuario_atual.title())
    usuarios_confirmados.append(usuario_atual)

    
for confirmados in usuarios_confirmados:
    print("Confirmados: ",confirmados.title())
print('...')
print('\n\n')
#=============================================================================
print('Remove')
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit','cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)
print('...')
print('\n\n')
#=============================================================================
print('enquete')

enquete = {}
flag_ativo = True

while flag_ativo:
    nome = input('Digite seu Nome: ')
    resposta = input('Qual sua linguagem preferida? ')

    # armazenr o nome ea resposta no dicionario
    enquete[nome]= resposta

    repetir = input('Alguem mais quer responder? (yes/no): ')
    if repetir == 'no':
        flag_ativo = False
        
print('Resultados')
for nomes, respostas in enquete.items():
    print('Nomes: ',nomes)
    print('Linguagens preferidas: ',respostas)
print(enquete)
#================================ ate pg183 ===================================



        
