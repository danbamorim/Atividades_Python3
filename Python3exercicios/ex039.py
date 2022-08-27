primeira = float(input('Primeira nota: '))
segunda = float(input('Segunda nota: '))

media = (primeira + segunda) / 2

print('Tirando {} e {}, a sua média será: {}'.format(primeira,segunda,media))

if media >=6:
    print('O aluno está aprovado')
elif media >=4.0 and 5:
    print('EStá de recuperação')
else:
    print('Está reprovado kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')