#dicionários
dici = {"RA":317106869, "nome":"Gustavo", "idade":25}
#para acessar o valor da chave:
print('acessando valores.\n ', dici["RA"], dici["nome"])

#para alterar o valor de uma chave:
dici["RA"]= 10
print("alterando um valor.\n ", dici["RA"],'\n')


# acesso apenas as chaves:
for i in dici:
    print(i)
print('\n')



#acesso as chaves e valores:
for z,x in dici.items():
    print(z,x)
print('\n')


#verificando se chave pertence no dicionario:
if "idade" in dici:
    print('Chave idade se encontra no dicionario.\n','Idade:',dici["idade"],'\n')


#verificando se valor pertence:
if "Gustavo" in dici.values():
    print("Valor se encontra.\n",'Nome:',dici["nome"],'\n')


#deletenda uma chave e valor:
del dici["idade"]
print('dicionario apos apagar a chave idade.\n',dici,'\n')


#incluindo chave e valor:
dici["av1"]=8
dici["av2"]=6
media= (dici["av1"]+ dici["av2"])/2
dici["media"]= media
print(dici)
