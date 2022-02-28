# 11 - Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
vetor_1=[]
vetor_2=[]
vetor_3=[]
final=[]

for x in range(10):
  vetor_1.append(int(input(f'Digite o {x+1}º valor do vetor 1: ')))
for x in range(10):
  vetor_2.append(int(input(f'Digite o {x+1}º valor do vetor 2: ')))
for x in range(10):
  vetor_3.append(int(input(f'Digite o {x+1}º valor do vetor 3: ')))

print('\n Lista intercalada:\n')
for item in range(10):
  final.append(vetor_1[item])
  final.append(vetor_2[item])
  final.append(vetor_3[item])

print(final)
