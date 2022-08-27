primeiro = int(input('Primeiro Termo: '))
segundo = int(input('Razão: '))
decimo = primeiro + (10 - 1) * segundo
for termo in range(primeiro,decimo,segundo):
     print('{}'.format(termo), end='->')
print('Acabou')
