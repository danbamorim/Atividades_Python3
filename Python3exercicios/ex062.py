NINE = 0
cont = 0
soma = 0
NINE = int(input('Digite um número [999 para parar]:  '))
while NINE != 999:
    cont += 1
    soma += NINE
    NINE = int(input('Digite um número [999 para parar]:  '))
print('Você escreveu {} números  e a soma deles é {}'.format(cont,soma))

