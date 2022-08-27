num = int(input('Digite um numero: ')),int(input('Digite um numero: ')),int(input('Digite mais um numero: ')),int(input('Digite o ultimo numero: '))

print(num)

print(f'O numero 9 apareceu {num.count(9)}')
if 3 in num:
     print(f'O numero 3 apareceu em {num.index(3)+1} posicao')
else:
    print('Nao tem')
print(f'Os pares são: ', end='')
for n in num:
    if n % 2 == 0:
        print(n,',' , end='')