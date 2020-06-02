# -*- coding: utf-8 -*-
import random
import pyqrcode


#lista de letras para gerar um senha aleatoria
letras = ['a','b','c','d','e',
          'f','g','h','i','j',
          'k','l','m','n','o',
          'p','q','r','s','t',
          'u','v','x','y','z']

#senha gerada 
senha = []

#conversao para string
ts = ''

# Gera uma senha com 8 caracter e salva em senha
for senha_num in range(0,9):
    senha_formada = random.choice(letras)
    senha.append(senha_formada)

# converte em string e guarda em ts
for i in senha:
    ts += i
print(senha)
print(ts)



# pega a string  ts
qr = ts
# Saida nome do arquivo
saida = input('teste')

# Cria o qrcode
url = pyqrcode.create(qr)

# Tipo do arquivo e tamanho
url.png(saida +'.png',scale = 8)


print(url)




