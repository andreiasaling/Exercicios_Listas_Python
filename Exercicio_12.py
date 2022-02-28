# 12 - Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que
# determine quantos alunos com mais de 13 anos possuem altura inferior à média
# de altura desses alunos.

idades=[]
alturas=[]
qtde_inferior_media=0

for x in range(30):
  idades.append(int(input(f'Digite a idade do aluno {x+1}: ')))
  alturas.append(int(input(f'Digite a altura do aluno {x+1} (em cm): ')))

media_alturas=sum(alturas)/len(alturas)

for x in range(0,len(idades)):
  if idades[x]>13 and alturas[x]<media_alturas:
    qtde_inferior_media+=1

print(f'\nA média de altura da turma é: {media_alturas}')
print(f'{qtde_inferior_media} alunos possuem mais de 13 anos e altura abaixo da média.')