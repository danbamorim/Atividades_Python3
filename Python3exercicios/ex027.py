nome = str(input('Digite seu nome completo: ')).lower().strip()
dividido = nome.split()
print('Muito prazer em conhecer!!')
print('Seu primeiro nome é {}'.format(dividido[0]))
print('Seu ultimo nome é {}'.format(dividido[len(nome)-1]))

