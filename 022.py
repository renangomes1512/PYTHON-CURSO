name = str(input('Dig. seu nome: ')).strip()
print('Seu nome em letras maiúcuslas é: {}'. format(name.upper()))
#nome com todas as letras maiucuslas
print('Seu nome em letras minúcuslas é: {}'. format(name.lower()))
#nome com todas as letras minusculas
print('O seu nome tem ao todo {} letras'. format(len(name) - name.count(' ')))
#quantas letras tem sem espaço
print('O seu primeiro nome tem ao todo {} letras'. format(name.find(' ')))
#quantas letras tem o primeiro nome
