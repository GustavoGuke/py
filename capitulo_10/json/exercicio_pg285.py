import json

'''
# Exercicio 10.11
filename = 'exercicioPg285.json'

try:
    number = int(input('Digite um numero: '))
    with open(filename, 'w') as f:
        json.dump(number, f)

except ValueError:
    print('Apenas numeros, abra o programa novamente')
    
else:
    print('Numero gravado')
    
# continuação do exercicio  mostrando arquivo 

filename = 'exercicioPg285.json'

with open(filename) as f:
    number = json.load(f)
    print('Numero: ',number)

'''

#===========================================================================

# refatorando exercicio usando funções
def show_number():
    """ Mostrar numero gravado """
    
    filename = 'exercicioPg285.json'
    try:
        with open(filename) as f:
            number = json.load(f)            
    except FileNotFoundError:
        return None
    except json.decoder.JSONDecodeError:
        print('nenhum numero salvo favor preencher: ')
        return None
    else:
        return number




def other_number():
    """ Troca o  numero salvo  """

    filename = 'exercicioPg285.json'
    trocar_numero=input('Deseja reescrever o numero: digite(s)\n'
                        'Para ignorar digite qualquer letra: ')
    n_other = ''
    
    
    if trocar_numero != 's':
        print('Numero não trocado')
    if trocar_numero == 's':         
        try:
            n_other = int(input('Digite o Numero: '))
            with open(filename, 'w') as f:
                json.dump(n_other, f)
        except ValueError:
            print('apenas Numeros')
    return n_other





def loading_number():
    """ Gravar numero caso arquivo esteja vazio """
    
    filename = 'exercicioPg285.json'
    try:
        number = int(input('Digite um numero: '))
        with open(filename, 'w') as f:
            json.dump(number, f)
    except ValueError:
        print('Apenas numeros, abra o programa novamente')
    else:
        return number




    
def prog():
    """ startando o programa """
    number = show_number()
    if number:
        print(number)
        troca = other_number()
    else:
        load = loading_number()
  
prog()



'''
   if trocar_numero != 's':
        try:
            n_other = int(input('Digite o Numero: '))
            with open(filename, 'w') as f:
                json.dump(n_other, f)
        except ValueError:
            print('apenas Numeros')
            n_other = ''
    elif trocar_numero == 'n':
        print('Numero nao trocado')
        n_other = ''
    else:
        print('Digite s: sim, n: nao ')
        n_other = ''
    return n_other
'''




    
