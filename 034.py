n1 = float(input('Dig. o salario: '))
if n1 > 1250:
    calc = n1 + (n1 * 10 / 100)
    print(f' o seu salrio era {n1} depois do aumento ficou {calc}')
elif n1 <= 1250:
    calc = n1 + (n1 * 15 / 100)
    print(f' o seu salrio era {n1} depois do aumento ficou {calc}')

