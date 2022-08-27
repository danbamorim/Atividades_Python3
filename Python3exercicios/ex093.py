jogadores = list()
futebol = dict()
partidas = list()
futebol['nome'] = str(input('Qual o nome do jogador?  '))
total = int(input('Quantas partidas ele jogou?  '))
for l in range(total):
     partidas.append(int(input(f'Quantos gols ele fez na partida {l}? ')))
     futebol['gols'] = partidas [:]
     futebol['total'] = sum(partidas)
while True:
       contin = str(input('Quer continuar? S/N  ')).upper()[0]
       if contin in 'SN':
           break
       print('Erro! digite novamente : apenas S/N').upper()[0]
       if contin == 'N':
         break
print('=' * 30)
for i in futebol.keys():
    print(f'{i:<15}',end='')
print()
print('=' * 30)
for k, v in enumerate(jogadores):
    print(f'{k}>3', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('=' * 30)


while True:
    busca = int(input('Qual jogador vc quer ver?999 para encerrar.....   '))
    if busca in 999:
        break
    if busca >= len(jogadores):
        print('Erro! digite novamente : apenas jogadores existentes ').upper()[0]
