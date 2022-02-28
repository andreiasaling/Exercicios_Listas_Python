# 10 - Faça um Programa que leia dois vetores com 10 elementos cada. Gere um
# terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos
# elementos intercalados dos dois outros vetores.

vetor_1=[]
vetor_2=[]
final=[]

for x in range(10):
  vetor_1.append(int(input(f'Digite o {x+1}º valor do vetor 1: ')))
for x in range(10):
  vetor_2.append(int(input(f'Digite o {x+1}º valor do vetor 2: ')))


print('\n Lista intercalada:\n')
for item in range(10):
  final.append(vetor_1[item])
  final.append(vetor_2[item])

print(final)
