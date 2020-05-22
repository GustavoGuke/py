#importando numpy
import numpy as np

vetor  = np.array([8, 34, 67, 98])

#vendo os dados
print(vetor)
print('Shape: Informa a quantidade de colunas de um vetor\n',vetor.shape,'\n')
print('Dtype: Indica o tipo de dado dos valores armazenados no vetor\n',vetor.dtype,'\n')
print('Size: retorna a quantidade de elementos de um vetor\n',vetor.size,'\n')
print('Itemsize: retorna o tamanho de um elemento da matriz em bytes \n',vetor.itemsize,'\n')
print('Ndim: retornara o numero de dimenssoes da matriz\n',vetor.ndim,'\n')



vetor1 = np.array([8.87, 34, 67.89, 98,1.09])
 
# Imprimindo dados do vetor
print(vetor1)
print("Shape:",vetor1.shape)
print("Dtype:",vetor1.dtype)
print("Size:",vetor1.size)
print("Itemsize:",vetor1.itemsize)
print("Ndim:", vetor1.ndim)

print("\n")
print("acessando dados dos vetores, Vetor:",vetor[0])
print("acessando dados dos vetores, Vetor1:",vetor1[2])

print("\n")
print("Mudando dados Vetor")
vetor[1] = 231
vetor1[3] = 105
print(vetor
      )
print(vetor1)
