# Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado
# pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas
# pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado
# quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo.

texto_saltos=['Primeiro:','Segundo:','Terceiro:','Quarto','Quinto']
saltos=[]
nome=input('Atleta: ')

if nome!="":
    for x in range(0,5):
        auxiliar=float(input(f'Digite o {texto_saltos[x]} salto: '))
        saltos.append(auxiliar)

media=sum(saltos)/len(saltos)

print(f'\nAtleta: {nome}\n')

for c in range(0,len(saltos)):
    print(f'{texto_saltos[c]} Salto: {saltos[c]}')

print(f'\nResultado final:')
print(f'Atleta: {nome}')
print(f'Saltos: {saltos[0]} - {saltos[1]} - {saltos[2]} - {saltos[3]} - {saltos[4]}')
print(f'Média dos saltos: {media}')