#ENTRADAS
valor = float(input('Qual o valor da sua prestação em atraso? '))
tempo = int(input('Há quanto tempo esta em atraso - em meses? '))
taxa = float(input('Qual a taxa de juros sobre cada mês de atraso da sua prestação? '))
#PROCESSAMENTO
prestacao = valor + (valor*taxa/100) * tempo
#SAÍDA
print(f'O novo valor que você tem que pagar é R$ {prestacao:.2f}' )