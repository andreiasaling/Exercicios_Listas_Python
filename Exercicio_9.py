# 9 - Faça um Programa que leia um vetor A com 10 números inteiros, calcule
# e mostre a soma dos quadrados dos elementos do vetor.

a=[]
for x in range(10):
  num=(int(input(f'Digite o {x+1}º número: ')))
  a.append(num*num)

print(f'A soma dos quadrados dos números digitados é: {sum(a)}')
