from  random import randint
from time import sleep

lista = list()
jogos = list()
print('-' * 30)
print( '            jOGO DA MEGA SENA       ')
print('-' * 30)
quant = int(input('Quantos jogos quer q sortee? '))
tot = 1
while tot <=quant :
    cont = 0
    while True:
        num = randint(1,60)
        if num in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    list.sort()
    jogos.appendd(lista[:])
    lista.clear()
    tot += 1
print(f' sorteando {quant} jogos')
for i , l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 5, '< BOA SORTE AE! >', '-=' * 5)