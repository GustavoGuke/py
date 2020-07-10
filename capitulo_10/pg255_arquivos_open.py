# abrindo um arquivo txt
with open('arquivosTxt/_a_pi.txt') as file_obj:
    content = file_obj.read()
    print(content)
print('...\n')


# lendo um arquivo atraves do for
file = 'arquivosTxt/_a_pi.txt'
with open(file) as arquivo:
    for line in arquivo:
        print(line)
print('...\n')



# criando uma lista de linhas de um arquivo
# trabalhar com o arquivo fora da função with 
# readlines salva o arquivo em um lista e passa para lines
file_name = 'arquivosTxt/_a_pi.txt'

with open(file_name) as obj:
    lines = obj.readlines()

for line in lines:
    print(line.rstrip())