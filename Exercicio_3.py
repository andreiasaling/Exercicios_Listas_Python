# 3 - Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = []

for i in range(4):
    notas.append(float(input(f'Digite a nota {i+1}: ')))

print('Média = {0:.1f}'.format(sum(notas)/len(notas)))