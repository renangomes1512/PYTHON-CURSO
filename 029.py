car = int(input('Dig. a velocidade do carro: '))
if car > 80:
    print('vc foi multado!! por anadr em alta velocidade em uma via de 80Km/h')
    calc = (car - 80) * 7
    print(f'o valor da multa a ser paga é de R${calc}!!')
elif car <= 80:
    print('Vc está dentro dos limites de velocidade!! dirija com segurança!!')