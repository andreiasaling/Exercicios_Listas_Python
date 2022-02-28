# 4 - Faça um Programa que leia um vetor de 10 caracteres, e diga quantas
# consoantes foram lidas. Imprima as consoantes.

lista=[]

for i in range(10):
  lista.append(input('Digite uma letra: '))

lista_nova=[]

for item in lista:
  if item!='a' and item!='e' and item!='i' and item!='o' and item!='u':
    lista_nova.append(item)

print(f'\nForam digitadas {len(lista_nova)} consoantes. São elas:\n {lista_nova}')