n1 = float(input('Dig. a largura da parede:'))
n2 = float(input('Dig. a altura da parede:'))
area = n1 * n2
quant = area / 2
print('A sua parede tem a dimensão de {} x {}, a sua área é de {}m²\n para pintar sua parede, você precisará de {}l de tinta.'. format(n1, n2, area, quant))