# 8 - Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada
# informação no seu respectivo vetor. Imprima a idade e a altura na ordem
# inversa a ordem lida.

idade=[]
altura=[]

for pessoa in range(5):
  idade.append(int(input(f'Digite a idade da {pessoa+1}ª pessoa: ')))
  altura.append(int(input(f'Digite a altura (em cm) da {pessoa+1} pessoa: ')))

print(f'\nA ordem inversa das idades é: {list(reversed(idade))}')
print(f'A ordem inversa das alturas é: {list(reversed(altura))}')
