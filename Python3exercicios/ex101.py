def ficha(jog='<desconhecido>',gol= 0):
    print(f'O jogador {jog} fez {gol} gols no campeonato')


nome = str(input('Qual nome do jogador? '))
gols = str(input('Quantos gols ele fez?  '))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome.strip() == '':
    ficha(gol=gols)
else:
    ficha((nome,gols))
