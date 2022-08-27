casa = float(input('Valor da casa: '))
salario = float(input('Salario do comprador: '))
anos = int(input('Anos de financiamento: '))
prestacao = (anos * 12) / casa
minimo = salario * 30 / 100

print('Para pagar uma casa de R$ {} em {} anos'.format(casa,anos))
print('A prestacao sera  R$ {}'.format(prestacao))

if prestacao <= minimo:
    print('Emprestimo pode ser concedido!')
else:
    print('Emprestimo negado!')
