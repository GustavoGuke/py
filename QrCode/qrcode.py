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
senha_wifi = ''



# Gera uma senha com 8 caracter e salva em senha
for senha_num in range(0,9):
    senha_formada = random.choice(letras)
    senha.append(senha_formada)

# converte em string
for i in senha:
    senha_wifi += i
print(senha_wifi)


rede = input('Digite o Nome da Rede: ')
wifi_code = 'WIFI:S:' + rede + ';T:WPA2;P:' + senha_wifi + ';;'

# Cria o qrcode
qrcode_wifi = pyqrcode.create(wifi_code)

# Tipo do arquivo e tamanho
qrcode_wifi.png('Wifi_' + rede + '.png', scale = 8)
print(' Codigo gerado: \t', wifi_code)




