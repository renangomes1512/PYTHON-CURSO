viagem = float(input('Dig. a distância da sua viagem: '))
if viagem <= 200:
    print('o valor da passagem será cobrado a R$0.50 por km!!')
    print('calculando...')
    print(f'o valor da passagem ficou de R$ {[viagem *0.50]}')
else:
    print('o valor da passagem será cobrado a R$0.45 por km!!')
    print('calculando...')
    print(f'o valor da passagem ficou de R$ {[viagem *0.45]}')
