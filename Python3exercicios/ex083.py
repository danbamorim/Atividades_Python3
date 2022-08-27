numeros  = [[] , []]
valor = 0

for num in range(0,8):
    valor = int(input(f'Digite o {num}| valor: '))
    if valor % 2 == 0:
       numeros[0].append(valor)
    else:
        numeros[1].append(valor)

print(f'Os numeros pares foram {numeros[0]}')
print(f'Os numeros impares foram {numeros[1]}')
print('Acabou')