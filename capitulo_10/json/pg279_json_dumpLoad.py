import json

'''
# lista a ser gravada no arquivo json
numbers = [2, 4, 6, 8, 10]

# nome do arquivo
file = 'dumpLoad.json'

# abrindo o arquivo no modo escrita se não existir Python criara
with open(file, 'w') as f:

    # json.dump(arquivo que sera gravado, onde sera gravado)
    json.dump(numbers, f)
'''


file = 'dumpLoad.json'

# abrindo o arquivo modo leitura
with open(file) as f:

    # json.load(abre meu arquivo json)
    numbers = json.load(f)
    print(numbers)
