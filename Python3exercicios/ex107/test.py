from ex107 import moeda

num = float(input('Digite um preço:$  '))
print(f'Aumentando em 10%, o valor {num} fica {moeda.aumentar(num,10)}')
print(f'o dobro de {num} é {moeda.dobro(num)}')
print(f'Metade de {num} é {moeda.metade(num)}')