preço = float(input('Preço das compras: R$ '))

print('Formas de pagamento')
print('[1] à vista dinheiro/cheque ')
print('[2] à vista cartão')
print('[3] 2x no cartão ')
print('[4] 3x no cartão ')

opção = int(input('Qual é a opção? '))

if opção == 1:
    desconto = preço - (preço * 10 / 100)
    print('O preço de R${}, irá receber o desconto de 10% e ficará R${}'.format(preço,desconto))
elif opção == 2:
    desconto = preço - (preço * 5 / 100)
    print('O preço de R${}, irá receber o desconto de 5% e ficará : R${}'.format(preço, desconto))
elif opção == 3:
    desconto = preço / 2
    print('O preço será de R${:.2f}'.format(desconto))
elif opção == 4:
    parcela = int(input('Qual é a parcela? '))
    total = preço + (preço * 20 / 100)
    desconto = total / parcela
    print("A parcela de {} terá R${} com juros ".format(parcela,desconto))
    print('Sua compra de R${} no final ficará com R${} '.format(preço,total))