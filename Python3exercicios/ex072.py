from random import randint

tuplas = (randint(0,5),randint(0,5),randint(0,5),randint(0,5),randint(0,5))

print(f'eu sorteei 5 números:')
print(tuplas)

print(f'O maior valor sorteado foi {max(tuplas)}')
print(f'O maior valor sorteado foi {min(tuplas)}')