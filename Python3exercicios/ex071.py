brasileirao =('Flamengo', 'Santos', 'Palmeiras', 'Gremio','AthleticoParanaense', 'SãoPaulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'VascodaGama', 'AtléticoMG', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'Csa', 'Chapecoense', 'Avaí')

print('Lista dos times no brasileirao:', end = '')
print(brasileirao)

print(f'Os 5 primeiros são:{brasileirao[0:5]}')

print(f'Os 4 últimos são {brasileirao[-4:]}')

print('Em ordem alfabetica é:', end=' ')
print(sorted(brasileirao))

print('A posicao do Chapecoence é ',end=' ')

print(brasileirao.index('Chapecoense'))