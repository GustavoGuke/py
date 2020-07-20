# Exercicio 10.8


filename = 'txt/exercicio_pg277_10.8.txt'

try:
    with open(filename) as f:
        line = f.read()
        print(line)
except FileNotFoundError:
    print('Arquivo nao encontrado')

# contando quantas vezes uma palavra aparece
print(line.lower().count('cat'))



print('Erro proposital FileNotFoundError')
filename = 'txt/exercicio_pg277_10.81.txt'
filenameCorreto = 'txt/exercicio_pg277_10.8.1.txt'

try:
    with open(filename) as f:
        line = f.read()
        print(line)
except FileNotFoundError:
    pass
    #print('Arquivo nao encontrado')


