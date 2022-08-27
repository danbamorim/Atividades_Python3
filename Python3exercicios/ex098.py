from random import randint

def sorteio(lista):
    print(f'Sorteando 5 valores da lista: {numeros}')
    for cont in range(0,5):
        lista.append(randint(0,10))

def somaPAr(lista):
       soma = 0
       for valor in lista:
           if valor % 2 == 0:
              soma += valor
       print(f'Somando os valores pares de {lista} dá {soma}')




numeros = list()
sorteio(numeros)
somaPAr(numeros)



