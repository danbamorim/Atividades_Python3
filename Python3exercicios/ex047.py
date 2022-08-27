soma = 0
cont = 0
for impar in range (1,500,2):
    if impar % 3 ==0:
     soma = soma + impar
    cont = cont + 1
    print('o numero {} dá {}'.format(cont,soma))