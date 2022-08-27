num = int(input('Digite o numero ai: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('O número {}'.format(num))
print('Unidade é {}'.format(u))
print('Dezena é {}'.format(d))
print('centena é {}'.format(c))
print('milhar é {}'.format(m))
