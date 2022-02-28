# 13 - Faça um programa que receba a temperatura média de cada mês do ano e
# armazene-as em uma lista. Após isto, calcule a média anual das temperaturas
# e mostre todas as temperaturas acima da média anual, e em que mês elas
# ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

temperatura=[]
acima_media=[]
mes = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']

for i in range(12):
    temperatura.append(float(input(f'Digite a temperatura média de {mes[i]}: ')))


media_temperaturas=sum(temperatura)/len(temperatura)
print('\nTemperatura média anual: {0:.1f}°C'.format(media_temperaturas))


for x in range(0,len(temperatura)):
  if temperatura[x]>media_temperaturas:
    print(f'{mes[x]} - {temperatura[x]}')