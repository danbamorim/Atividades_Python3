sexo= str(input('Digite o sexo, M/F :')).strip().upper()
while sexo not in 'MmFf':
    sexo1 = str(input('Digite o sexo novamente, M/F :'))
print('Sexo {} , obrigado por informar'.format(sexo))
