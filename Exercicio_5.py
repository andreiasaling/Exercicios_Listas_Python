# 5 - Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
# Imprima os três vetores.

numeros=[]

for i in range(10):
  numeros.append(int(input('Digite um número: ')))

par=list(filter(lambda x : x%2==0, numeros))
impar=list(filter(lambda x : x%2!=0, numeros))

print(f'\nLista original: {numeros}')
print(f'Lista dos pares: {par}')
print(f'Lista dos ímpares: {impar}')