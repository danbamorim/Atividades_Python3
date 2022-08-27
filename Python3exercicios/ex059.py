calcular = int(input('Calcular seu fatorial: '))
c = calcular
f = 1
print('Calculando:{}! = '.format(calcular, end = ''))
while c > 0:
    print('{}'.format(c),end='')
    print('x' if c > 1 else '=',end = '')
    f *= c
    c -= 1
print('{}'.format(f))

