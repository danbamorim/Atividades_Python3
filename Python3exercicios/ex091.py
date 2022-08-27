futebol = dict()
partidas = list()
futebol['nome'] = str(input('Qual o nome do jogador?  '))
total = int(input('Quantas partidas ele jogou?  '))

for l in range(total):
    partidas.append(int(input(f'Quantos gols ele fez na partida{l}? ')))
futebol['gols'] = partidas [:]
futebol['total'] = sum(partidas)

print(futebol)


print('=' * 30)

for k, v in futebol.items():
  print(f'O campo {k} tem o valor {v}')

print('=' * 30)

print(f'O jogador{futebol["nome"]} jogou {total} partidas')

for i,v in enumerate(futebol['gols']):
    print(f'Na partida {i} ele  fez {v} gols')
print(f'No total ele fez {futebol["total"]} gols')