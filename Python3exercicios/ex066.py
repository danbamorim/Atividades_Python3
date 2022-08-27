from random import randint
v = 0
while True:
    num = int(input('diga um numero: '))
    computador = randint(0, 10)
    total = computador + num
    tipo = ' '
    while tipo not in 'PI':
        resultado = str(input('P ou I: ')).strip().upper()[0]
    print(f'O jogador jogou {num} e o computador {computador}. Total de {total}')
    if tipo in 'P':
        if total % 2 == 0:
           print('Você ganhou')
           v+= 1
        else:
           print('Perdeste')
           break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você ganhou')
            v+= 1
        else:
            print('Perdeste')
            break
print('Tenta de novo')
print(f'Voce ganhou {v} vezes')