#16 - Uma empresa paga seus vendedores com base em comissões.
# O vendedor recebe $200 por semana mais 9% de suas vendas brutas daquela semana. Por exemplo, um vendedor
# que teve vendas brutas de $3000 em uma semana recebe $200 mais 9% de $3000, ou seja, um total de $470.
# Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos
# seguintes intervalos de valores: $200 - $299
# $300 - $399
# $400 - $499
# $500 - $599
# $600 - $699
# $700 - $799
# $800 - $899
# $900 - $999
# $1000 em diante
# Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.

vendas=[]
salarios=[]
cont1,cont2,cont3,cont4,cont5,cont6,cont7,cont8,cont9=0,0,0,0,0,0,0,0,0

print('>>> Digite -1 para sair <<<')
while True:
    venda=float(input('Valor vendido: '))
    if venda==-1: break;
    vendas.append(venda)

for x in range(0,len(vendas)):
    salarios.append(200+(vendas[x]*0.09))


for x in range(0,len(salarios)):
    if (salarios[x]>=200 and salarios[x]<=299):
        cont1+=1
    elif (salarios[x]>=300 and salarios[x]<=399):
        cont2+=1
    elif (salarios[x]>=400 and salarios[x]<=499):
        cont3+=1
    elif (salarios[x]>=500 and salarios[x]<=599):
        cont4+=1
    elif (salarios[x]>=600 and salarios[x]<=699):
        cont5+=1
    elif (salarios[x]>=700 and salarios[x]<=799):
        cont6+=1
    elif (salarios[x]>=800 and salarios[x]<=899):
        cont7+=1
    elif (salarios[x]>=900 and salarios[x]<=999):
        cont8+=1
    elif salarios[x]>=1000:
        cont9+=1

print(f'\n Vendedores com salário até R$ 299,00 : {cont1}')
print(f'\n Vendedores com salário até R$ 399,00 : {cont2}')
print(f'\n Vendedores com salário até R$ 499,00 : {cont3}')
print(f'\n Vendedores com salário até R$ 599,00 : {cont4}')
print(f'\n Vendedores com salário até R$ 699,00 : {cont5}')
print(f'\n Vendedores com salário até R$ 799,00 : {cont6}')
print(f'\n Vendedores com salário até R$ 899,00 : {cont7}')
print(f'\n Vendedores com salário até R$ 999,00 : {cont8}')
print(f'\n Vendedores com salário R$ 1000,00 ou mais : {cont9}')