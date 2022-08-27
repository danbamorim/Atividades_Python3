nome = str(input('Digite seu nome: ')).strip()

print('Analisando seu nome ...')
print('Seu nome em maiuscula é {}'.format(nome.upper()))
print('Seu nome em minuscula é {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {}  letras'.format( nome.find(' ')))