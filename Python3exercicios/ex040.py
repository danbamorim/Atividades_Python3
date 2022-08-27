from datetime import date
nascimento = int(input('Ano de Nascimento: '))
ano = date.today().year
atual = ano - nascimento

print('O atleta tem {} anos'.format(atual))

if atual <= 9:
    print('Classificacao: mirim')
elif atual <= 14:
    print('Classificacao: infantil')
elif atual <= 19:
    print('Classificacao: junior')
elif atual <= 25:
    print('Classificacao: senior')
elif atual > 25:
        print('Classificacao: Master')