print ('''
    MENU:
hotdog = 100
hamburguer = 103
cheeseburguer = 104
refrigerante = 105''')

total_lanches = 0
while True:
    
    codigo = input ('Qual o código do que você quer de lanche? ')
    quantidade = int (input ('Qual a quantidade do item? '))

    if codigo == '100':
        hotdog_preco = 12.00
        valor_total = (hotdog_preco * quantidade)
    elif codigo == '103':
        hamburguer_preco = 12.00
        valor_total = (hamburguer_preco * quantidade)
    elif codigo == '104':
        cheeseburguer_preco = 13.00
        valor_total = (cheeseburguer_preco * quantidade)
    elif codigo == '105':
        refrigerante_preco = 8.00
        valor_total = (refrigerante_preco * quantidade)
    else:
        print ('Opção inválida!')
    
    total_lanches = total_lanches + valor_total

    continuar = input ('Quer adicionar algo a mais no seu lanche (S/N)? ').upper()

    if continuar == 'N':
        print ('Saindo...')
        break

print (f'Seu lanche custa R$ {total_lanches} e ficará pronto em 10 minutos!')
