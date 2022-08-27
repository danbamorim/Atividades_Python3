salario = float(input('Informe seu salario: R$'))
aumento = salario * 1.10
aumento_mais = salario * 1.15

if salario <= 1250.00:
    print('Vai receber um aumento de 15% e ficará com R$ {:.2f}'.format(aumento_mais))
else:
    print('Vai receber aumento de 10% e ficará com R$ {:.2f}'.format(aumento))