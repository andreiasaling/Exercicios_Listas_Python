# 14 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
# As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

respostas=[]
soma_respostas=0

respostas.append(int(input("Telefonou para a vítima? (1-Sim 0-Não): ")))
respostas.append(int(input("Esteve no local do crime? (1-Sim 0-Não): ")))
respostas.append(int(input("Mora perto da vítima? (1-Sim 0-Não): ")))
respostas.append(int(input("Devia para a vítima? (1-Sim 0-Não): ")))
respostas.append(int(input("Já trabalhou com a vítima? (1-Sim 0-Não): ")))

for i in respostas:
    soma_respostas+=int(i)

if soma_respostas<2:
    print('Inocente')
elif soma_respostas==2:
    print('Suspeito')
elif (soma_respostas>=3 and soma_respostas<=4):
    print('Cúmplice')
elif soma_respostas==5:
    print('Assasino')