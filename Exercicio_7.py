# 7 - Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma,
# a multiplicação e os números.

numeros=[]
soma=0
multiplicacao=1

for item in range(5):
  numeros.append(int(input(f'Digite o {item+1}º número: ')))
  soma=sum(numeros)
  multiplicacao=multiplicacao*numeros[item]

print(f'A lista dos números digitados foi {numeros}')
print(f'A soma dos números digitados é {soma}')
print(f'O produto dos números digitados é {multiplicacao}')
