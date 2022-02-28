# 15 - Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
# encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado).
# Após esta entrada de dados, faça:
# Mostre a quantidade de valores que foram lidos;
# Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# Calcule e mostre a soma dos valores;
# Calcule e mostre a média dos valores;
# Calcule e mostre a quantidade de valores acima da média calculada;
# Calcule e mostre a quantidade de valores abaixo de sete;
# Encerre o programa com uma mensagem;


notas=[]
notas_acima_media=0
notas_abaixo_sete=0

while True:
    controle = float(input('Digite a nota: '))
    if controle==-1: break;
    notas.append(controle)

print(f'Quantidade de notas digitadas: {len(notas)}')
print(f'Notas digitadas: {notas}')

lista_inversa=list(reversed(notas))
for x in range(0,len(lista_inversa)):
    print(f'\n {lista_inversa[x]}')

soma_notas=sum(notas)
media_notas=sum(notas)/len(notas)

for x in range(0,len(notas)):
    if notas[x]>=media_notas:
        notas_acima_media+=1

for x in range(0,len(notas)):
    if notas[x]<7:
        notas_abaixo_sete+=1

print("")
print(f'Soma das notas digitadas: {soma_notas}')
print(f'Média das notas digitadas: {media_notas}')
print(f'Notas acima da média: {notas_acima_media}')
print(f'Notas abaixo de 7: {notas_abaixo_sete}')

print("")
print('-- PROGRAMA ENCERRADO --')