from operator import itemgetter
from random import randint
from time import sleep

valores = {'jogador 1' : randint(1,6),
           'jogador 2' : randint(1,6),
           'jogador 3' : randint(1,6),
           'jogador 4' : randint(1,6)
           }
for k , v in valores.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
sleep(2)
print('=' * 30)

print('=========== Ranking ===============')

ranking = sorted(valores.items(), key = itemgetter(1), reverse= True)

for i , v in enumerate(ranking):
    print(f'{i+1} posicao : {v[0]} com valor {v[1]}')


