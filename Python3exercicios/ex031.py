from datetime import date
ano = int(input('Que ano quer analisar ? coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano= date.today().year
if ano % 4 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano{} Não  BISSEXTO'.format(ano))