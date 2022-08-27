viagem = int(input('digite uma viagem em Km: '))
passagem = viagem * 0.50
passagem_cara = viagem * 0.45

if viagem <= 200:
    print('Você vai pagar R$ {:.2f}'.format(passagem))
else:
    print('Voce vai pagar R$ {:.2f}'.format(passagem_cara))