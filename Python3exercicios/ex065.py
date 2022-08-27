while True:
    tabuada = int(input('Quer tabuada de qual valor? '))
    if tabuada < 0:
        break
    print('-' * 30)
    for c in range(1,11):
         print(f'{tabuada} x {c} = {tabuada * c}')
    print('-' * 30)
print('Falou Menor')