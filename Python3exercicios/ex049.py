soma = 0
cont = 0
for n in range(1,7):
    num = int(input('Digite um valor {}:'.format(n)))
    if num % 2 == 0:
     soma = soma + num
     cont = cont + 1
    print('AQui ohh {} e a soma deles é par {}'.format(cont ,soma))