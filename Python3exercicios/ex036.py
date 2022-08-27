numero = int(input('Digite um numero inteiro: '))

print('Escolha uma das bases para conversão: ')
print('[1] converter para Binario ')
print('[2] converter para octal ')
print('[3] converter para hexadecimal ')

opção = int(input('Sua opção é: '))

if opção == 1:
    print('O número {} convertendo para binario é {}'.format(numero,bin(numero)))
elif opção == 2:
    print('O número {} convertendo para octal é {}'.format(numero,oct(numero)))
elif opção == 3:
    print('O número {} convertendo para hexadecimal é {}'.format(numero,hex(numero)))
else:
    opção = int(input('Sua opção é: '))




