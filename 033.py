n1 = int(input('Dig. um valor: '))
n2 = int(input('Dig. outro valor: '))
n3 = int(input('Dig. outro valor: '))
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

menor = n1
if n2 < n3 and n2 < n1:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print(f'o maior valor é {maior} e o menor valor é {menor}!!')