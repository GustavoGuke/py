import re

string = "O aluno josé foi reprovado. A aluna ana e os alunos thiago e andre ficaram em dependencia"


#Metodo MATCH procura a string desejada no inicio da linha 
procurar = re.match("O aluno",string)
print(procurar,'\n')

procurar = re.match("ana",string)
print(procurar,'\n')

#Metodo SEARCH procura a string desejada em toda linha 
procurar = re.search("O aluno",string)
print(procurar,'\n')

procurar = re.search("ana",string)
print(procurar,'\n')


procurar = re.search("monica",string)
print(procurar,'\n')


print("Raw string faz tratamento da string pura sem caracteres especiais")
print("Gustavo\nGustavo")
print(r"Gustavo\nGustavo")
