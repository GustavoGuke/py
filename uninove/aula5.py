def fimprograma():
    msg = "Fim do Programa"
    return msg

def mostarmsg(nome,media):
    print("Seu nome é ",nome, "e sua media foi de: ",media)


def media(nota1, nota2):
    resposta = (nota1 + nota2)/2
    return resposta

def colecao(objcolecao):
    maiorvalor=0
    for x in objcolecao:
        if x > maiorvalor:
            maiorvalor = x
    return maiorvalor


n = input("informe nome do aluno: ")
a = float(input("Nota 1: "))
b = float(input("Nota 2: "))
m = media(a,b)

mostarmsg(n,m)
print("maior item da coleção: ",colecao([4,75,89,66]))

mesg = fimprograma()
print(mesg)      


