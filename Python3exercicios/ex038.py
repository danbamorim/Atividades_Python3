nasce = int(input('ANo de nascimento: '))
idade = 2022 - nasce
falta = 18 - idade
sera = 2022 - (idade - 18)
saldo = idade - 18
print('Quem nasceu em {} tem {} anos em 2022'.format(nasce,idade))

if idade <18:
    print('Ainda falta {} anos para alistamento'.format(falta))
    print('O seu alistamento será em {}'.format(sera))
elif idade == 18:
    print('Precisará se alistar esse ano')
else:
    print('Voce teria que está alistado há {} atrás'.format(saldo))