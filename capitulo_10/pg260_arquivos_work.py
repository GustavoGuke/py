# criando uma lista de linhas de um arquivo
# trabalhar com o arquivo fora da função with 
# readlines salva o arquivo em um lista e passa para lines
file_name = 'arquivosTxt/_a_pi.txt'

with open(file_name) as obj:
    lines = obj.readlines()

# string vazia para armazenar os dados do arquivo que estamos lendo
pi_string = ''

# for para passar os dados para a string
for line in lines:
    pi_string += line.rstrip()

# vendo o resultado final
print(pi_string[:4]+ '...')

# tamanho da string
print(len(pi_string))
