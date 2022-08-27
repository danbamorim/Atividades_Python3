numero = list()

while True:
    n = int(input('Digite um valor: '))
    if n not in numero:
        numero.append(n)
        print('Valor adicionado')
    else:
        print('Valor duplicado..adiciono não')
    continua = str(input('Quer continuar? S/N '))
    if continua in 'Nn':
       break
print('=' * 30)
print(f'Vocẽ adicionou os numeros {numero}')