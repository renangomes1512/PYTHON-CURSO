import random
h1 = str(input('Primeiro aluno: '))
h2 = str(input('Segundo aluno: '))
h3 = str(input('Terceiro aluno: '))
h4 = str(input('Quarto aluno: '))
lista = [h1, h2, h3, h4]
escolhido = random.choice(lista)
print('O escolhido é {}'. format(escolhido))
