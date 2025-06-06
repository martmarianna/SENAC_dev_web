#ENTRADAS
tempo_viagem = float(input('Qual seu tempo de viagem? '))
vel_med = float(input('Qual sua velocidade média ao longo da viagem? '))
#PROCESSAMENTO
distancia = tempo_viagem * vel_med
ltrs_usados = distancia/12
#SAÍDAS
print (f'Sua velocidade média foi de {vel_med}, seu tempo de viagem foi de {tempo_viagem}, a distância percorrida de {distancia} e a quantidade de litros consumidos foi {ltrs_usados:.3f}.')