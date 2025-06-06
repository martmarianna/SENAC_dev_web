# pessoas = int(input('Qual o número de pessoas que vcoê vai cadastrar as idades? '))

# somatorio = 0

# for i in range(pessoas):
#     idades = int(input('Qual a idade das pessoas? '))
#     somatorio = somatorio + idades
#     media = somatorio / pessoas

# print (f'O número de pessoas é {pessoas} e a media das idades é {media}.')

numero_pessoas = 0
somatorio = 0

while True:
    idades = int(input('Qual idade quer cadastrar? '))
    somatorio = somatorio + idades
    numero_pessoas = numero_pessoas + 1
    media = somatorio / numero_pessoas

    continuar = input('Quer continuar (S/N)? ').upper() 
    
    if continuar == 'N':
        print (f'O número de pessoas é {numero_pessoas} e a media das idades é {media:.2f}.')
        break