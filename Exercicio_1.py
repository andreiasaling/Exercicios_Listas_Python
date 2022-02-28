# 1 - Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

numeros=[]

numeros.append(int(input('Digite um número: ')))
numeros.append(int(input('Digite um número: ')))
numeros.append(int(input('Digite um número: ')))
numeros.append(int(input('Digite um número: ')))
numeros.append(int(input('Digite um número: ')))

print(f'A lista criada foi: {numeros}')


# Variação do exercício 1 - Utilizando while

numeros=[]

cont=1
while cont<=5:
  numeros.append(int(input('Digite um número: ')))
  cont+=1

print(numeros)