lista = []
maior = 0
menor = 0
for l in range(0,6):
    lista.append(int(input(f'Digite um valor na posicao {l} :')))
    if l == 0:
       maior = menor= lista[l]
    else:
     if lista[l] > maior:
        maior = lista[l]
     if lista[l] < menor:
         menor = lista[l]
print(f'voce digitou os valores {lista}')
print(f'o maior numero é {maior} e suas posição é ',end='')
for c, v in enumerate(lista):
    if v == maior:
      print(f'{c}.....',end='')

print(f'o menor numero é {menor} e suas posição é ', end='')

for c, v in enumerate(lista):
    if v == menor:
        print(f'{c}.....',end='')
