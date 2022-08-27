dado = []
galera = []
cont = 0
maiorpeso = 0
menor = 0

while True:
    dado.append(str(input('Qual your name? ')))
    dado.append(float(input('Qual sua Peso? ')))
    if len(dado) == 0:
        maiorpeso = menor = dado[1]
    else:
        if dado[1] > maiorpeso:
            maiorpeso = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    galera.append(dado[:])
    dado.clear()
    continua = str(input('Quer continuar S/N? '))
    cont += 1
    if continua in 'Nn':
        break
print(f'Ao todo vc digitou {cont} pessoas')
print(f'o maior peso foi {maiorpeso} de ', end ='')
for p in galera:
    if p[1] == maiorpeso:
        print(f'{p[0]}', end='')
print()
print(f'o menor peso foi {menor} de ', end ='')
for p in galera:
    if p[1] == menor:
        print(f'{p[0]}', end='')