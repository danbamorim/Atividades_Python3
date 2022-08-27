multa = float(input('Qual é a velocidade atul do carro? '))
pagar = (multa-80) * 7
if multa <= 80:
    print("Voce nao precisa pagar a multa")
    print('Tenha um bom dia')
else:
    print("Você passou do limite de 80km")
    print('Voce deve pagar a multa de:R${:.2f}'.format(pagar))


