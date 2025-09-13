r1 = float(input('Dig. um segmento: '))
r2 = float(input('Dig. mais um segmento: '))
r3 = float(input('Dig.  mais um segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Analisando...')
    print('os segmentos acima PODEM FORMAR um triângulo!!')
else:
    print('Analisando...')
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!!')