from ex108 import moeda

num = float(input('Digite um preço:$  '))
print(f'Aumentando em 10%, o valor {moeda.moeda(num)} fica {moeda.moeda (moeda.aumentar(num,10))}')
print(f'o dobro de {moeda.moeda(num)} é {moeda.moeda( moeda.dobro(num))}')
print(f'Metade de {moeda.moeda(num)} é {moeda.moeda (moeda.metade(num))}')