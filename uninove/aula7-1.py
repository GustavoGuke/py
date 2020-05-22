import re

string = "O aluno José foi reprovado. Ele tirou 10 na segunda nota"
procurar = re.search(r"\w\w\w\w\w\w",string)
if procurar:
    print(procurar.group())
else:
    print("Não encontrado")

# a expressão D ira trazer numeros decimais
procurar = re.search(r"\d+",string)
if procurar:
    print(procurar.group())
else:
    print("Não encontrado")

#a expressao W ira trazer strings 
procurar = re.search(r"\w\w\w\w\w\w+",string)
if procurar:
    print(procurar.group())
else:
    print("Não encontrado")

# a expressao {6,8} ira trazer strings que estao entre 
procurar = re.search(r"\w{6,8}",string)
if procurar:
    print(procurar.group())
else:
    print("não encontrado")

procurar = re.search(r"\w{5}\w+",string)
if procurar:
    print(procurar.group())
else:
    print("Não encontrado")

    
procuarar = re.search(r"\d+\.d+",string)
if procurar:
    print(procurar.group())
else:
    procurar = re.search(r"\d+",string)
    if procurar:
        print(procurar.group())
    else:
        print("Não encontrado")


    
