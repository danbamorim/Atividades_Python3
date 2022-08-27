from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('O computador escolheu {}'.format(itens[computador]))
print('''Suas opções:
[0]Pedra
[1] Papel      
[2] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')

print('Computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))

if computador == 0:
    if jogador == 0:
     print('Empate')
    elif jogador == 1:
     print('jogador vence')
    elif jogador == 2:
     print('computador ganha')
elif computador == 1:
    if jogador == 0:
     print('Computador vence')
    elif jogador == 1:
     print('empate')
    elif jogador == 2:
     print('jogador ganha')
elif computador == 2:
    if jogador == 0:
     print('jogador vence')
    elif jogador == 1:
     print('computador vence')
    elif jogador == 2:
     print('empate')
else:
    print('Jogada invalida')
