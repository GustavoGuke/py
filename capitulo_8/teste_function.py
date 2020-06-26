# retorna uma lista
def recebe_tupla(*tupla):
    times = []
    for i in tupla:
        times.append(i)
    return times

time = recebe_tupla('palmeiras','sp','peixa','gamba')

print(time)

# retorna um dicionario
def recebe_dicionario(**dicionario):
    dic = {}

    for key, values in dicionario.items():
        dic[key]=values
    return dic

def mostrar_dicionario(pessoas):
    for k, v  in pessoas.items():
        print(k,':',v)

nome = input('Digite seu nome: ')
pessoas = recebe_dicionario(nome=nome, sobreNome='silva', idade='25')

print(pessoas)
mostrar_dicionario(pessoas)