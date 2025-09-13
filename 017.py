import math
n1 = float(input('Dig. o compromento do cateto oposto: '))
n2 = float(input('Dig. o comprimento do cateto adjacente: '))
calc = math.sqrt(n1 ** 2 + n2 ** 2)
print('O valor da hipotenusa é: {}'. format(calc))