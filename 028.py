from random import randint
comp = randint(0, 5)
print('--=--=' * 10)
print('Vou pensar em número entre 0 e 5. tente adivinhar...')
print('--=--=' * 10)
n1 = int(input('Em qual número eu pensei?? '))
print('processando...')
if n1 == comp:
    print('vc ganhou!!! parabéns meu amigo!!')
else:
    print('vc perdeu, tente novamente!!')
    print(f'o número era {comp} e não {n1}!!')