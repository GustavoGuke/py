comeco = 'sim'
while comeco == 'sim':
    idade = int (input('DIGITE SUA IDADE: '))

    if idade < 2:
        print('BEBE')
    elif idade < 13:
        print('CRIANÇA')
    elif idade < 18:
        print('ADOLESCENTE')
    elif idade < 65:
        print('ADULTO')
    elif idade >= 65:
        print('IDOSO')
    else:
        print('erro')
    comeco = input ('PARA REPETIR DIGITE "SIM": ')
    
print('FIM PROGRAMA')
