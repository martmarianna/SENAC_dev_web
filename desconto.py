#ENTRADAS
hr_aula = float(input ('Qual o valor da sua hora/aula? '))
num_hrs_mes = float(input ('Quantas horas você trabalhou esse mês? '))

#PROCESSAMENTO
sal_brt = hr_aula * num_hrs_mes
desc_inss = sal_brt * 10/100

sal_liq = sal_brt - desc_inss 

#SAÍDAS

print (f'O seu salário no mês será de R$ {round(sal_liq, 2)}.')