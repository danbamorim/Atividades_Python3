def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16 :
        return 'Vota nâo'
    elif 16 <= idade < 18 or idade > 67:
        return 'Voto não obrigatorio'
    elif idade > 18:
        return 'VOto obrigatorio porra'


pergunte = int(input('Que ano tu nasceu?  '))
print(voto(pergunte))
