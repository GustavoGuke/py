# escrever dados em um arquivo vazio

# caminho do arquivo passado a uma variavel
# se não existir o arquivo ele é criado
filename = 'arquivosTxt/_a_pi.txt'


# abrir com função  open(nome_arquivo, 'w' modo escrita) passando dois argumentos.
# 'r' leitura , 'w' escrita, 'r+' leitura e escrita, 'a' concatenar ao arquivo
# metodo write() escreve uma string no arquivo.
'''

texto = input('Escreva o que vc quer alterar: ')
with open(filename, 'w') as file:
    file.write(texto,'\n')

print('arquivo txt alterado')
print('caminho arquivo "arquivosTxt/_a_pi.txt" \n')




# abrindo o arquivo no terminal atualizado
with open('arquivosTxt/_a_pi.txt') as file_obj:
    content = file_obj.read()
    print(content)
print('...\n')

'''
#===============================================================================
# 'a' concatenando

arquivo = 'arquivosTxt/_a_pi.txt'
while True:
    
    msg = input('digite algo: ')
    pararlaco = ''
    pararlaco += msg

    if pararlaco != '.':
        with open(arquivo, 'a') as file:
            file.write(msg+'\n')
    
    
    if pararlaco == '.':
        break
   

with open('arquivosTxt/_a_pi.txt') as file_obj:
    content = file_obj.read()
    print(content)
print('...\n')


#=========================================================================
